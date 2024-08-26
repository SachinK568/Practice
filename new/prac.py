num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = int(input('Enter num want to find:'))

i = 0
while i < len(num):
    if num[i] == x:
        print("found at index", i)
        break
    i = i + 1
