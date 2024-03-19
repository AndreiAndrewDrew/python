# Exemplu de folosire a functiei Lambda
# se foloseste cind avem nevoie dintro functoi
# sa intorcem alta functie, atunci se folosete Lambda functii


def greeting(greet):
    return lambda name: f"{greet},{name}!"


morninig_greeting = greeting("Buna Dimineatsa")
print(morninig_greeting(' Andrew!!!'))

evening_greeting = greeting("Buna Seara")
print(evening_greeting(' Anastasia!!!'))

# Aceeasi functie fara lambda! folosim functie clasica


def greeting1(greet):
    def info(name):
        return f"{greet},{name}!"
    return info


morninig_greeting1 = greeting1("Buna Dimineatsa")
print(morninig_greeting1(' Andrew!!!'))

evening_greeting1 = greeting1("Buna Seara")
print(evening_greeting1(' Anastasia!!!'))