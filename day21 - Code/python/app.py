from tornado import web
import tornado
import datetime
import socket
from tornado.options import define, options, parse_command_line



define('port', default=8008, help="run on the given port", type=int)
define('debug', default=True, help="set tornado debug mode", type=bool)

class MainHandler(web.RequestHandler):
    async def get(self, *args, **kwargs):
        access_datatime = datetime.datetime.now()
        access_datatime = str(access_datatime)
        host_name = socket.gethostname()
        return_data = {
            'code': 200,
            'status': 'ok',
            'host_name': host_name,
            'access_time': access_datatime,
        }
        self.write(json.dumps(return_data))





class MainHandler2(web.RequestHandler):
    async def get(self, *args, **kwargs):
        self.write("Hello World2")

urls = [
    tornado.web.URLSpec("/", MainHandler, name="index"),
]

if __name__ == "__main__":
    app = web.Application(urls, debug=options.debug)
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
