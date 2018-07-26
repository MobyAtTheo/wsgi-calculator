"""
For your homework this week, you'll be creating a wsgi application of
your own.

You'll create an online calculator that can perform several operations.

You'll need to support:

  * Addition
  * Subtractions
  * Multiplication
  * Division

Your users should be able to send appropriate requests and get back
proper responses. For example, if I open a browser to your wsgi
application at `http://localhost:8080/multiple/3/5' then the response
body in my browser should be `15`.

Consider the following URL/Response body pairs as tests:

```
  http://localhost:8080/multiply/3/5   => 15
  http://localhost:8080/add/23/42      => 65
  http://localhost:8080/subtract/23/42 => -19
  http://localhost:8080/divide/22/11   => 2
  http://localhost:8080/               => <html>Here's how to use this page...</html>
```

To submit your homework:

  * Fork this repository (Session03).
  * Edit this file to meet the homework requirements.
  * Your script should be runnable using `$ python calculator.py`
  * When the script is running, I should be able to view your
    application in my browser.
  * I should also be able to see a home page (http://localhost:8080/)
    that explains how to perform calculations.
  * Commit and push your changes to your fork.
  * Submit a link to your Session03 fork repository!


"""


def add(*args):
    """ Returns a STRING with the sum of the arguments """

    # TODO: Fill sum with the correct value, based on the
    # args provided.
    sum = "0"

    return my_sum


def multiply(*args):
    """ Returns a STRING with the sum of the arguments """

    # TODO: Fill sum with the correct value, based on the
    # args provided.
    product = "0"

    return product


def divide(*args):
    pass


def subtrace(*args):
    pass


# TODO: Add functions for handling more arithmetic operations.


def resolve_path(path):
    """
    Should return two values: a callable and an iterable of
    arguments.
    """

    # TODO: Provide correct values for func and args. The
    # examples provide the correct *syntax*, but you should
    # determine the actual values of func and args using the
    # path.

    # path is something like add/3/5
    # or 'multiply/2/10/''
    webpath = [1, 2, 3]

    webpath = path.split("/")
    func = webpath[0]
    # args = ["25", "32"]
    args = [webpath[1], webpath[2]]

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
    response_headers = [
        ("Content-Type", "text/html"),
        ("Content-Length", str(len(response_body))),
    ]
    path = environ.get

    start_response(status, response_headers)
    return [response_body.encode("utf8")]

    # TODO (bonus): Add error handling for a user attempting
    # to divide by zero.
    pass


if __name__ == "__main__":
    # TODO: Insert the same boilerplate wsgiref simple
    # server creation that you used in the book database.
    pass
