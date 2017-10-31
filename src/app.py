import json

from sanic import Sanic
import sanic.response
from pydbus import SystemBus


class Connector:
    busname = "net.local.MyDBService"
    def __init__(self):
        bus = SystemBus()
        self._obj = bus.get(self.busname)

    async def query(self, key):
        # would require a non-trivial effort to make below
        # async-await compatible
        # TODO: make that happen :)
        res = json.loads(self._obj.get(key))
        return res


conn = Connector()
app = Sanic()


@app.route("/")
async def root(request):
    return sanic.response.json({"hello": "world"})


@app.route("/api/v1/<key>")
async def get_key(request, key):
    res = await conn.query(key)
    return sanic.response.json(res)


def main():
    #app.run(host="0.0.0.0", port=8888, workers=4)
    app.run(host="0.0.0.0", port=8888)

if __name__ == "__main__":
    main()
