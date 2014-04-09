#!/usr/bin/python

import json
import requests
import urllib

class Marathon:

  def __init__(self, host, user=None, password=None):
    self.host = urllib.quote(host)
    self.auth = (user, password)
    self.headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    }

  def endpoints(self, appId=None):
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
    r = requests.delete(self.host + '/v2/apps/' + urllib.quote(appId, safe=''),
      auth=self.auth,
      headers=self.headers)
    r.raise_for_status()
    return r.text

  def list(self):
    r = requests.get(self.host + '/v2/apps',
      auth=self.auth,
      headers=self.headers)
    r.raise_for_status()
    return r.text

  def list_tasks(self, appId):
    r = requests.get(self.host + '/v2/apps/' + urllib.quote(appId, safe='') + '/tasks',
      auth=self.auth,
      headers=self.headers)
    r.raise_for_status()
    return r.text

  def scale(self, appId, instances):
    r = requests.get(self.host + '/v2/apps/' + urllib.quote(appId, safe=''),
      auth=self.auth,
      headers=self.headers)
    r.raise_for_status()

    payload = r.json()['app']
    payload['instances'] = instances

    r = requests.put(self.host + '/v2/apps/' + urllib.quote(appId, safe=''),
      auth=self.auth,
      headers=self.headers,
      data=json.dumps(payload))
    r.raise_for_status()
    return r.text

  def search(self, appId=None, cmd=None):
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
    print json.dumps(payload)
    r = requests.post(self.host + '/v2/apps',
      auth=self.auth,
      headers=self.headers,
      data=json.dumps(payload))
    r.raise_for_status()
    return r.text
