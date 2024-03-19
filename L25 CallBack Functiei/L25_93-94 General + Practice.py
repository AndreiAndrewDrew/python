def other_fn():
    # someting operation...
    pass


def fn_with_callback(callback_fn):
    callback_fn()


fn_with_callback(other_fn) # functie callback
# aici nu chemam functia 'otehr_fn'
# dar trasnmite numele functiei

print("Ex.1")


def print_nummber_info(num):  # afla daca numaru este par sau impar
    if (num % 2) == 0:
        print("Entered number is even")
    else:
        print("Entered number is odd")


def print_square_num(num):  # ridicam numaraul la puterea a 2
    print("Square of the num is:", num * num)


def process_number(num, callback_fn):  # creem callback - functie
    callback_fn(num)


entered_num = int(input('Enter any number: ')) # Convertam in 'int'

process_number(entered_num, print_nummber_info)

process_number(entered_num, print_square_num)

print("Ex.2 Generalizat")


def send_data(data):
    # seding data to the remote server...
    pass


def process_data(input_data, send_data_fn):
    update_data = input_data.copy()
    # actiuni cu update_data
    send_data_fn(update_data)


process_data({'name': 'Andrew'}, send_data)

