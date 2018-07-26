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


def add(*args):
    """ Returns a STRING with the sum of the arguments """
    arg_1 = args[0]
    arg_2 = args[1]
    # TODO: Fill sum with the correct value, based on the
    # args provided.

    numbers = [int(i) for i in args]
    result = str(sum(numbers))

    return result


def multiply(*args):
    """ Returns a STRING with the sum of the arguments """

    # TODO: Fill sum with the correct value, based on the
    # args provided.
    # i = 0
    # result = 0

    result = 1
    for i in args:
        result = result * i

    return result


def divide(*args):
    arg_1 = args[0]
    arg_2 = args[1]
    pass


def subtract(*args):
    arg_1 = args[0]
    arg_2 = args[1]

    return


# TODO: Add functions for handling more arithmetic operations.


def resolve_path(path):
    """
    Should return two values: a callable and an iterable of
    arguments.
    """
    # QA:
    # TODO: Provide correct values for func and args. The
    # examples provide the correct *syntax*, but you should
    # determine the actual values of func and args using the
    # path.

    # path is something like add/3/5
    # or 'multiply/2/10/''
    # path = [1, 2, 3]

    routes = {"add": add, "multiply": multiply, "subtract": subtract, "divide": divide}

    path = path.strip("/").split("/")
    func_name = path.pop(0)
    if func_name is None:
        raise NameError
    func = routes.get(func_name)

    # args = ["25", "32"]
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
    except NameError:
        status = "404 Not Found"
        body = "<h1>Not Found</h1>"
        print(traceback.format_exc())
    except Exception:
        status = "500 Internal Server Error"
        body = "<h1>Internal Server Error</h1>"
        print(traceback.format_exc())
    finally:
        headers.append(("Content-length", str(len(body))))
        start_response(status, headers)
        return [body.encode("utf8")]


if __name__ == "__main__":
    # TODO: Insert the same boilerplate wsgiref simple
    # server creation that you used in the book database.
    from wsgiref.simple_server import make_server

    srv = make_server("localhost", 8080, application)
    srv.serve_forever()
