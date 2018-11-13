"""
@Time    : 2018-11-12 16:02:49
@Author  : xionzhi
@File    : runserver.py
@Software: vscode
"""
from service import app


if __name__ == '__main__':
    app.run(port=8080, debug=True)


# from tornado.wsgi import WSGIContainer
# from tornado.httpserver import HTTPServer
# from tornado.ioloop import IOLoop
# from service import app

# http_server = HTTPServer(WSGIContainer(app))
# http_server.listen(8080, address="127.0.0.1")
# IOLoop.instance().start()
