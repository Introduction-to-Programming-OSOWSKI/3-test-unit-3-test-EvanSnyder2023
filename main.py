def countB(w):
    count = 0
    for i in range(0, len (w)):
        if w[i] == "b":
            count = count + 1

    return count

print(countB("bat"))

def removeLast(x, w):

    word = 0
    for i in range(0, w[-1]):
        w[i] == word

    return word



def sumBetweenOdd(x, y):
    total = 0

    for i in range (x + 1, y):
        total = total + i

    return total

print(sumBetweenOdd(5, 13))

def firstLast(w):
    if w[0] == w[-1]:
        return True
    else:
        return False

print (firstLast("alph"))