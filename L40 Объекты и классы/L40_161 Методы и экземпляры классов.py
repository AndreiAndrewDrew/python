class Comment:
    def __init__(self, text):
        self.text = text
        self.votes_qty = 0

    def upvote(self):
        self.votes_qty += 1


first_comment = Comment("First Comment")

print(first_comment.text)
print(first_comment.votes_qty)

first_comment.upvote()

print(first_comment.votes_qty)

print(first_comment)  # 'first_comment '- este exemplear lui 'Comment'
print(Comment)  # 'Comment '- este subclasa lui 'object'
print(object)
print(isinstance(first_comment, Comment))  # TRUE
print(isinstance(Comment, object))  # TRUE
print(isinstance(first_comment, object))  # TRUE
# Python intai cauta atributul in clasa exemplear 'first_comment', daca nul gaseste
# cauta in clasa principala 'Comment', daca nul gaseste cauta in clasa 'object'
# si daca si acolo nui- insaemna ca atributul cautat nu este disponibel clasei 'first_comment'
