button_info = {
    'text': 'Buy'
}
button_default = {
    'text': 'Ok',
    'color': 'black',
    'width': 0,
    'height': 0
}
button_style = {
    'color': 'yellow',
    'width': 200,
    'height': 300

}
print("Var.1 de Unire")
new_button = {
    **button_info,
    **button_style
}
print(new_button)

print("Var.2 deUnire")
new_button2 = button_info | button_style # rez la fel ca in var.1
print(new_button2)

new_button3 = button_default | button_style
rev_new_button3 = button_style | button_default

print(new_button3)
print(rev_new_button3)
