def validate_args(fn):
    def wrapper(*args, **kwargs):
        for arg in [*args, *kwargs.values()]:  # asa controlam si pozitionie argumente dar iminovie argumente
            if not isinstance(arg, int) and not isinstance(arg, float):
                raise ValueError(f"Type of the {arg} is {type(arg)}",
                                 "All arguments must be 'int' or 'float'")

        return fn(*args, **kwargs)

    return wrapper


@validate_args
def sum_nums(a, b):
    return a + b


try: # Prelucrarea corecta a Eoroarei cu 'try except'
    print(sum_nums(7, 2))
    print(sum_nums(2.32, 4.12))
    print(sum_nums(2.32, 4))
    # print(sum_nums('str', 4.12))
    # print(sum_nums(a='2.0', b=4.12))
    print(sum_nums([1,2,3],'rind'))

except ValueError as e:
    print(e)
