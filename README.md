# marathon-client.py

Client for the Marathon scheduler written in Python.

Inspired by the [gem marathon client](https://github.com/mesosphere/marathon_client).

## Requirements

* Python 2.6+ for using the `marathon` package.
* Python 2.7+ for using `marathon-client`.

## Installation

```
git clone https://github.com/Wizcorp/marathon-client.py.git
cd marathon-client.py
```

You can install `marathon-client.py` globally with:
```
sudo easy_install .
```

Or locally with:
```
pip install --user .
```
You may have to edit your `$PATH` environment variables.

## Usage

### marathon-client

```
marathon-client --help
```

### marathon package

List the apps running on Marathon:
```
from  marathon import Marathon

marathon = Marathon(host="http://127.0.0.1:8080")
print marathon.list()
```
