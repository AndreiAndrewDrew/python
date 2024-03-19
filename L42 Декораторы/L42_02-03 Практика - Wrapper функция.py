def decorator_function(original_fn):  # Creeem decorator
    def wrapper_function(*args, **kwargs):
        # careva actiuni INAINTE de executia functiei 'original_fn'
        print("Executat ianinte de functia 'original_fn'")

        result = original_fn(*args, **kwargs)
        print("Rezultatul Functiei:", result)

        # careva actiuni DUPA de executia functiei 'original_fn'
        print("Executat dupa functia 'original_fn'")

        return result

    return wrapper_function


@decorator_function  # Utilizam decoratarul '@decorator_function'
def my_function(a, b):
    print("Hello")
    return [a, b]


res = my_function(100, 50)
print(res)

