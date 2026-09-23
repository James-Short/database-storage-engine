from ExpressionNode import ExpressionNode

query = input('Input your query: ')


chunks = []

start, end, prevStart = 1, 1, 0

keywords = {'SELECT', 'UPDATE', 'DELETE', 'FROM', 'WHERE', 'SET'}

while end < len(query):
    if query[end] == ' ':
        if(query[start:end].upper() in keywords):
            chunks.append(query[prevStart:start-1])
            prevStart = start
            start += 1
        else:
            start = end + 1
    end += 1
chunks.append(query[prevStart:end+1])
print(start, end, prevStart)
print(chunks)

whereInd = None
whereChunk = None

for index, chunk in enumerate(chunks):
    if len(chunk) >= 5 and chunk[0:5].upper() == 'WHERE':
        whereInd = index
        whereChunk = chunk[6:]

print(whereChunk)

def traverseWhereChunk(chunk):
    start, end = 0, 0
    currNode = ExpressionNode()
    while end < len(chunk):
        if chunk[end] == ' ':
            if chunk[start:end] == 'OR':
                currNode.type = 'logical'
                currNode.operator = 'OR'
                currNode.left = traverseWhereChunk(chunk[:start-1])
                currNode.right = traverseWhereChunk(chunk[end+1:])
                return currNode
            else:
                start = end + 1
        end += 1
    start, end = 0, 0
    while end < len(chunk):
        if chunk[end] == ' ':
            if chunk[start:end] == 'AND':
                currNode.type = 'logical'
                currNode.operator = 'AND'
                currNode.left = traverseWhereChunk(chunk[:start-1])
                currNode.right = traverseWhereChunk(chunk[end+1:])
                return currNode
            else:
                start = end + 1
        end += 1

    currNode.type = 'comparison'
    for index, c in enumerate(chunk):
        if c in {'<', '>', '=', '!=', '<=', '>='}:
            currNode.operator = c
            if chunk[0] == "'":
                currNode.left = ExpressionNode('literal', None, None, chunk[1:index-2])
            else:
                currNode.left = ExpressionNode('literal', None, None, chunk[:index-1])
            if chunk[-1] == "'":
                currNode.right = ExpressionNode('literal', None, None, chunk[index+2:-1])
            else:
                currNode.right = ExpressionNode('literal', None, None, chunk[index+1:])
    return currNode

print(traverseWhereChunk(whereChunk).operator)
print(traverseWhereChunk(whereChunk).left.operator)
print(traverseWhereChunk(whereChunk).right.operator)
            
            

    