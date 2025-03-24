def decorator_function(func):
    def wrapper():
        func()
    return wrapper