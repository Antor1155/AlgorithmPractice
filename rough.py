seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
seq2 = ['a', 'b', 'c', 'd', 'e', 'f']

a = [seq2[2 * j] for j in range(len(seq2)//2)]

print(a)