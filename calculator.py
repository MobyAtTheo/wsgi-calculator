#! /usr/bin/env python3

# """
# For your homework this week, you'll be creating a wsgi application of
# your own.
#
# You'll create an online calculator that can perform several operations.
#
# You'll need to support:
#
#   * Addition
#   * Subtractions
#   * Multiplication
#   * Division
#
# Your users should be able to send appropriate requests and get back
# proper responses. For example, if I open a browser to your wsgi
# application at 'http://localhost:8080/multiple/3/5' then the response
# body in my browser should be '15'.
#
# Consider the following URL/Response body pairs as tests:
#
# '''
#   http://localhost:8080/multiply/3/5   => 15
#   http://localhost:8080/add/23/42      => 65
#   http://localhost:8080/subtract/23/42 => -19
#   http://localhost:8080/divide/22/11   => 2
#   http://localhost:8080/               => <html>Here's how to use this page
# ...</html>
# '''
#
# To submit your homework:
#
#   * Fork this repository (Session03).
#   * Edit this file to meet the homework requirements.
#   * Your script should be runnable using '$ python calculator.py'
#   * When the script is running, I should be able to view your
#     application in my browser.
#   * I should also be able to see a home page (http://localhost:8080/)
#     that explains how to perform calculations.
#   * Commit and push your changes to your fork.
#   * Submit a link to your Session03 fork repository!
#
#
# """
import traceback
import math


def add(*args):
    """ Returns a STRING with the sum of the arguments """
    # DONE: Fill sum with the correct value, based on the
    # args provided.

    numbers = [int(i) for i in args]
    result = str(sum(numbers))

    return result


def multiply(*args):
    """ Returns a STRING with the sum of the arguments

    *see subtract function logic for a more 'pythonic' way of solving the
    setting of the default variable "result"
    """

    # DONE: Fill sum with the correct value, based on the
    # args provided.
    # i = 0
    # result = 0

    i = 1
    result = 1
    for i in args:
        result *= float(i)

    return str(int(result))


def divide(*args):

    if len(args) > 2:
        print("sorry only 2 inputs")
    result = 1
    for i in args:
        try:
            result = int(float(args[0]) / float(args[1]))
        except ZeroDivisionError:
            result = "Cannot Divide by Zero"

    return str(result)


def subtract(*args):
    i = 1.0
    result = float(args[0])
    for i in args[1:]:
        result -= float(i)

    return str(int(result))


# TODO: Add functions for handling more arithmetic operations.


def cos(*args):
    """Get cosine, input is in degrees"""
    if len(args) > 1:
        print("[*] cos: sorry only 1 inputs")
    result = round(math.cos(math.radians(float(args[0]))), 3)

    return str(result)


def tan(*args):
    """Get tangent, input is in degrees"""
    if len(args) > 1:
        print("[*] cos: sorry only 1 inputs")
    result = round(math.tan(math.radians(float(args[0]))), 3)

    return str(result)


def sin(*args):
    """Get sine, input is in degrees"""
    if len(args) > 1:
        print("[*] cos: sorry only 1 inputs")
    result = round(math.sin(math.radians(float(args[0]))), 3)

    return str(result)


def resolve_path(path):
    """
    Should return two values: a callable and an iterable of
    arguments.
    """
    # DONE: Provide correct values for func and args. The
    # examples provide the correct *syntax*, but you should
    # determine the actual values of func and args using the
    # path.

    # path is something like add/3/5
    # or 'multiply/2/10/''
    # path = [1, 2, 3]

    routes = {
        "add": add,
        "multiply": multiply,
        "subtract": subtract,
        "divide": divide,
        "cos": cos,
        "sin": sin,
        "tan": tan,
    }

    path = path.strip("/").split("/")
    func_name = path.pop(0)

    func = routes.get(func_name)
    if func_name is None:
        raise NameError

    args = path

    return func, args


def application(environ, start_response):
    # TODO wip: Your application code from the book database
    # work here as well! Remember that your application must
    # invoke start_response(status, headers) and also return
    # the body of the response in BYTE encoding.
    #

    # response_body = body % (
    #      environ.get('SERVER_NAME', 'Unset'), # server name
    #         ...
    #      )
    # status = '200 OK'
    headers = [("Content-type", "text/html")]
    try:
        path = environ.get("PATH_INFO", None)
        if path is None:
            raise NameError
        func, args = resolve_path(path)
        body = func(*args)
        status = "200 OK"
    # except TypeError:
    #     pass
    except NameError:
        status = "404 Not Found"
        body = "<h1>Not Found</h1>"
        print(traceback.format_exc())
    except Exception:
        status = "500 Internal Server Error"
        body = "<h1>Internal Server Error</h1>"
        print(traceback.format_exc())
    except ZeroDivisionError:
        status = "500 Internal Server Error"
        body = "<h1>Cannot divide by zero, please try again.</h1>"
        pass
    finally:
        headers.append(("Content-length", str(len(body))))
        start_response(status, headers)
        return [body.encode("utf8")]


if __name__ == "__main__":
    # TODO: Insert the same boilerplate wsgiref simple
    # server creation that you used in the book database.
    print("multiply: {}".format(multiply(3, 2.5)))
    print("divide: {}".format(divide(10, 2)))
    print("divide: {}".format(divide(0, 2)))
    print("divide: {}".format(divide(2, 0)))
    print("divide: {}".format(divide(0, 2)))
    print("subtract: {}".format(subtract(0, 2)))
    print("subtract: {}".format(subtract(-2, 1)))
    print("subtract: {}".format(subtract(-2.3, 0, 8, 1, 1)))
    print("cos: {}".format(cos(45, 30)))
    print("cos: {}".format(cos(45)))
    print("sin: {}".format(sin(45)))
    print("tan: {}".format(tan(45)))

    from wsgiref.simple_server import make_server

    srv = make_server("localhost", 8080, application)
    srv.serve_forever()
