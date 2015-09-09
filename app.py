import web
import json


def notfound():
    #return web.notfound("Sorry, the page you were looking for was not found.")
    return json.dumps({'ok':0, 'errcode': 404})

def internalerror():
    #return web.internalerror("Bad, bad server. No donut for you.")
    return json.dumps({'ok':0, 'errcode': 500})

def returnFibonacci(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a

urls = (
    '/(.*)', 'handleRequest',
)


app = web.application(urls, globals())
app.notfound = notfound
app.internalerror = internalerror


class handleRequest:
    def GET(self, method_id):
        if not method_id:
            return web.notfound()
        else:
            fib=returnFibonacci(method_id)
            return json.dumps({'ok': '1'})

    def POST(self):
        i = web.input()
        data = web.data() # you can get data use this method
        #print data
        print returnFibonacci(5)
        pass

if __name__ == "__main__":
    app.run()
