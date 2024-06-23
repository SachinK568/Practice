Keyword = input("Enter keyword : ")


def name(word):
    return word[::-1]


revname = name(Keyword)
if revname == Keyword:
    print("True")
else:
    print("False")
