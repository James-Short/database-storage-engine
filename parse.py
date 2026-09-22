
query = input('Input your query: ')

query = query.split(' ')

def formatConditions(conditions):
    conditions = ['CustomerID', '=', '1;']
    
def tokenizeSelect(query):
    keywords = {'SELECT', 'FROM', 'WHERE'}
    if len(query) <= 1:
        return
    left, right = 0, 1
    currKeyword = 'SELECT'
    chunks = {}
    while right < len(query):
        if query[right] in keywords:
            chunks[currKeyword] = query[left+1:right]
            left = right
            print(currKeyword)
            currKeyword = query[right]
        right += 1
    chunks[currKeyword] = query[left+1: right]
    print(chunks)
        

def tokenizeDelete(query):
    keywords = { 'DELETE', 'FROM', 'WHERE'}
    if len(query) <= 1:
        return
    left, right = 0, 1
    currKeyword = 'DELETE'
    chunks = {}
    while right < len(query):
        if query[right] in keywords:
            chunks[currKeyword] = query[left+1:right]
            left = right
            print(currKeyword)
            currKeyword = query[right]
        right += 1
    chunks[currKeyword] = query[left+1: right]
    print(chunks)

def tokenizeUpdate(query):
    keywords = {'UPDATE', 'SET', 'WHERE'}
    if len(query) <= 1:
        return
    left, right = 0, 1
    currKeyword = 'UPDATE'
    chunks = {}
    while right < len(query):
        if query[right] in keywords:
            chunks[currKeyword] = query[left+1:right]
            left = right
            print(currKeyword)
            currKeyword = query[right]
        right += 1
    chunks[currKeyword] = query[left+1: right]
    print(chunks)

if query[0] == 'SELECT':
    tokenizeSelect(query)
elif query[0] == 'DELETE':
    tokenizeDelete(query)
elif query[0] == 'UPDATE':
    tokenizeUpdate(query)
