import tornado.ioloop
import tornado.web
from pywebio.platform.tornado import webio_handler
from Bmi import bmi

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")
    



if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/bmi", webio_handler(bmi)),  # bmi 即为上文计算BMI指数的函数
    ])
    application.listen(port=80, address='localhost')
    tornado.ioloop.IOLoop.current().start()

    