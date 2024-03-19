class Comment:
    def __init__(self, text):
        self.text = text

    @staticmethod # se creeaza metodul static 'merge_comment'
    def merge_comment(first, second):
        return f"{first} {second}"


my_comment = Comment("My Comment")

m_1 = Comment.merge_comment("Thanks", "Excelent")
# metodul 'merge_comment' se poate de chemat si la nivelul clasei 'Comment'
print(m_1)

m_2 = my_comment.merge_comment("Great", "OK")
# si se poate de chemat si la nivelul exemplerului 'my_commnet'
print(m_2)


