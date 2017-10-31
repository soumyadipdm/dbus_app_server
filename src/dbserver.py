import sys
import json
import site
import logging

from gi.repository import GLib
import pydbus
from pydbus import SystemBus


class MyDBService:
    """
    <node>
      <interface name='net.local.MyDBService'>
        <method name='get'>
          <arg type='s' name='key' direction='in'/>
          <arg type='s' name='response' direction='out'/>
        </method>
      </interface>
    </node>
    """
    # docstring should contain the D-bus retrospect xml

    def __init__(self):
        self.db = {"key1": 1, "key2": 2, "key3": 3}
        self.log = logging.getLogger()

    def get(self, key):
        data = {"message": "No key found", "result": None}
        value = self.db.get(key)
        if not value:
            response = json.dumps(data)
            return response
        data["message"] = "Key retrieved"
        data["result"] = value
        self.log.debug("Data: {0}".format(data))
        response = json.dumps(data)
        return response


def setup_log():
    log = logging.getLogger()
    log.setLevel(logging.DEBUG)
    sh = logging.StreamHandler(sys.stdout)
    log.addHandler(sh)


def main():
    setup_log()
    log = logging.getLogger()

    loop = GLib.MainLoop()
    bus = SystemBus()
    bus.publish("net.local.MyDBService", MyDBService())
    log.info("Starting event loop")
    loop.run()


if __name__ == "__main__":
    main()
