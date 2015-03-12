#!/usr/bin/env python

import json
import requests
import urllib

class Marathon:
  """
  Create a new marathon client instance to deals with the Marathon API.

  :param host: Marathon URL.
  :type host: String
  :param user: Username required for the HTTP authentication.
  :type user: String
  :param password: Password required for the HTTP authentication.
  :type password: String
  """

  def __init__(self, host, user=None, password=None):
    self.host = host
    self.auth = (user, password)
    self.headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    }

  def endpoints(self, appId=None):
    """
    List tasks of all running applications if ``appId`` is not provided.
    List running tasks for app ``appId`` if provided.

    :param appId: The app you want to list the endpoints.
    :type appId: String
    :return: Response from the Marathon API
    :rtype: text/plain
    :raise: requests.exceptions.HTTPError
    """

    if appId:
      url = '/v2/apps/' + urllib.quote(appId, safe='') + '/tasks'
    else:
      url = '/v2/tasks'

    headers = {
      'Content-Type': 'text/plain',
      'Accept': 'text/plain'
    }
    r = requests.get(self.host + url,
      auth=self.auth,
      headers=headers)
    r.raise_for_status()
    return r.text

  def kill(self, appId):
    """
    Destroy app ``appId``.

    :param appId: The app you want to destroy.
    :type appId: String
    :return: Response from the Marathon API
    :rtype: application/json
    :raise: requests.exceptions.HTTPError
    """

    r = requests.delete(self.host + '/v2/apps/' + urllib.quote(appId, safe=''),
      auth=self.auth,
      headers=self.headers)
    r.raise_for_status()
    return r.text

  def list(self):
    """
    List all running apps.

    :return: Response from the Marathon API
    :rtype: application/json
    :raise: requests.exceptions.HTTPError
    """

    r = requests.get(self.host + '/v2/apps',
      auth=self.auth,
      headers=self.headers)
    r.raise_for_status()
    return r.text

  def list_tasks(self, appId):
    """
    List running tasks for app ``appId``.

    :param appId: The app you want to list the tasks.
    :type appId: String
    :return: Response from the Marathon API
    :rtype: application/json
    :raise: requests.exceptions.HTTPError
    """

    r = requests.get(self.host + '/v2/apps/' + urllib.quote(appId, safe='') + '/tasks',
      auth=self.auth,
      headers=self.headers)
    r.raise_for_status()
    return r.text

  def scale(self, appId, instances):
    """
    Scale the number of app instances for app ``appId``.

    :param appId: The app you want to scale.
    :type appId: String
    :param instances: The number of instances you want to have.
    :type instances: Integer
    :return: Response from the Marathon API
    :rtype: application/json
    :raise: requests.exceptions.HTTPError
    """

    r = requests.get(self.host + '/v2/apps/' + urllib.quote(appId, safe=''),
      auth=self.auth,
      headers=self.headers)
    r.raise_for_status()

    editable_attributes = ['cmd',
                           'constraints',
                           'container',
                           'cpus',
                           'env',
                           'executor',
                           'id',
                           'instances',
                           'mem',
                           'ports',
                           'uris']

    payload = dict([(attr, r.json()['app'][attr])
                            for attr in editable_attributes
                            if r.json()['app'][attr] is not None])
    payload['instances'] = int(instances)

    r = requests.put(self.host + '/v2/apps/' + urllib.quote(appId, safe=''),
      auth=self.auth,
      headers=self.headers,
      data=json.dumps(payload))
    r.raise_for_status()
    return r.text

  def search(self, appId=None, cmd=None):
    """
    List all running apps, filtered by appId and command.

    :param appId: The filter you want to use to search an app by appId.
    :type appId: String
    :param cmd: The filter you want to use to search an app by command.
    :type cmd: String
    :return: Response from the Marathon API
    :rtype: application/json
    :raise: requests.exceptions.HTTPError
    """

    params = {}
    if appId:
      params['id'] = appId
    if cmd:
      params['cmd'] = cmd

    r = requests.get(self.host + '/v2/apps',
      auth=self.auth,
      headers=self.headers,
      params=params)
    r.raise_for_status()
    return r.text

  def start(self, payload):
    """
    Create and start a new app.

    :param payload: The app definition.
    :type appId: dict
    :return: Response from the Marathon API
    :rtype: application/json
    :raise: requests.exceptions.HTTPError
    """

    r = requests.post(self.host + '/v2/apps',
      auth=self.auth,
      headers=self.headers,
      data=json.dumps(payload))
    r.raise_for_status()
    return r.text
