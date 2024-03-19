class Comment:
    def __init__(self, text): # Metoda magica constructor '__init__' de creearea exemplearelor ai claei 'Comment'
        self.text = text  # Lui obiectul 'self' ii creem atributul 'text'
        self.votes_qty = 0  # la fel creem atributul 'votes_qty' pentru obiectul 'self'

    def upvote(self):  # metoda 'upvote' va fi accesabila tuturor exemplearelor clasei 'Comment'
        self.votes_qty += 1

first_comment = Comment("Hello Andrew!")

print(first_comment.text)
print(first_comment.votes_qty)
first_comment.upvote()
print(first_comment.votes_qty)

print(first_comment.__dict__) # Afisham atributele proprii ale clasei 'fisrt_comment'
print(dir(first_comment)) # metodele si atributele mostenite de la clasa 'Comment'