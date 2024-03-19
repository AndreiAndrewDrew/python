grey_button = {
    'width': 200,
    'text': 'Buy',
    'color': 'grey'
}

red_button = {
    **grey_button,  # folosim operatorul de despachetare a dictionarului
    'color': 'red'
}

print(grey_button)
print(red_button)
