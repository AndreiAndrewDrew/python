class Comment:
    def __init__(self, text,
                 initial_votes_qty=0):  # Metoda magica constructor '__init__' de creearea exemplearelor ai claei 'Comment'
        # 'initial_votes_qty=0' 0 este valoare po default
        self.text = text  # Lui obiectul 'self' ii creem atributul 'text'
        self.votes_qty = initial_votes_qty  # la fel creem atributul 'votes_qty' pentru obiectul 'self'

    def upvote(self):  # metoda 'upvote' va fi accesabila tuturor exemplearelor clasei 'Comment'
        self.votes_qty += 1

    def upvote_quantity(self, qty):
        self.votes_qty += qty


my_comment = Comment("My Commment!")

print("Valoarea atributului 'text':", my_comment.text)
print("Valoarea atributului 'votes_qty':", my_comment.votes_qty)

my_comment.upvote()  # chemam metoda 'upvote()'
print("Valoarea atributului 'votes_qty':", my_comment.votes_qty)

my_comment.upvote()  # inca odata
print("Valoarea atributului 'votes_qty':", my_comment.votes_qty)

my_comment.upvote_quantity(4)  # chemam metoda 'upvote_quantity() cu valoarea 4'
print("Valoarea atributului 'votes_qty':", my_comment.votes_qty)  # 6, deoarce la 2 se adauga 4

my_comment.upvote_quantity = 10  # astfel se adauga un propriu atribut in clasa 'my_comment'

# my_comment.upvote_quantity() # Eroare, deoarec python cauta in atributele proprii intai,
# si exista asa atribut, rezulta mai departe nu cauta,
# daca este atribut local mai departe nu cauta!!

print(my_comment.__dict__)  # {'text': 'My Commment!', 'votes_qty': 6, 'upvote_quantety': 10}
# S-a adugat un atribut nou 'upvote_quantety': 10

second_comment = Comment("Second Comment")  # creeem obiect nou 'second_comment'

second_comment.upvote_quantity(2)  # chemam metoda 'upvote_quantity() cu valoarea 2'
print("Valoarea atributului 'votes_qty':", second_comment.votes_qty)  # 2

my_comment2 = Comment("Comentariu 2", 10) # creeem obiect nou 'second_comment'
                                                            # inidcam valoare 'initial_votes_qty'

print("Valoarea atributului 'votes_qty':",my_comment2.votes_qty)
