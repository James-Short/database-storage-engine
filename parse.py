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