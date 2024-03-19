def is_user_authenticated():
    return False


def check_user_auth(fn):
    def wrapper(*args, **kwargs):
        if is_user_authenticated():
            print("User is authenticated!")
            return fn(*args, **kwargs)
        else:
            print("Error: User is NOT authenticated!")

    return wrapper


@check_user_auth
def do_sensitive_job():
    # Do some tasks only if user is authenticated
    print("Results of some sensetive tasks.")


try:
    do_sensitive_job()
except ValueError as e:
    print(e)
