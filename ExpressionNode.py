
class ExpressionNode:
    def __init__(self, type=None, left=None, right=None, value=None, operator=None):
        #Types are logical, comparison, column, and literal
        #Logical is AND/OR, comparison is =/<, column is Name/Age, Literal is "John Smith"/"Jane Doe"
        self.type = type
        self.left = left
        self.right = right
        self.value = value
        self.operator = operator