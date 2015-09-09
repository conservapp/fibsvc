import web

urls = ('/', 'fibsvc')

app = web.application(urls, globals(), True)

def fibonacci(n):
    c = [];
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        c.append(a)
    return c

class fibsvc:
   def GET(self):
        i = web.input(num = 'web')
        try:
            # insure that the user submitted an integer, not a character or a word
            j = int(i.num)
        except ValueError:
            return "ERROR: Character submitted, please input a positive integer"

        if j > 0:
            # insure that the user submitted a positive number
            fib = fibonacci(j)
            return web.websafe(fib)
        else:
            return "ERROR: Please input a positive integer"

if __name__ == "__main__":
    app.run()