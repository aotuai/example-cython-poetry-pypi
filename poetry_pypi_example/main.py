print(f"Importing `{__name__}` module from {__file__}")


def hello_world():
    function_name = hello_world.__name__
    print(f"Running {function_name}() from {__file__}")
    print("Hello world!")
