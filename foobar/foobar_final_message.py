import base64

MESSAGE = '''
NmNdNC03KiFCFhUPbWNJMys1O3UdERJWIihCJC8zOjcWEQ8VaiFdNSsxIjdVFhkVaiFIJyEmOyEW EQ8Vai1AIjwxKztTXVASYWQJIC08JjdHVFhQIzAJYXR0aCdfXVpWJiFKZmJ0aCBQU1dcOTcJYXR0 aCFQV1ASYWQJJyE7aHILERJCJCoPZjM=
'''

KEY = 'MD.ANTOR1155'

result = []
for i, c in enumerate(base64.b64decode(MESSAGE)):
    result.append(chr(ord(c) ^ ord(KEY[i % len(KEY)])))

print (''.join(result))