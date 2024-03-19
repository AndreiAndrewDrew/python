def decorator_function(original_fn):  # Creeem decorator
    def wrapper_function():
        result = original_fn()

        return result

    return wrapper_function


@decorator_function # Utilizam decoratarul '@decorator_function'
def my_function():
    print("Hello")


my_function()
