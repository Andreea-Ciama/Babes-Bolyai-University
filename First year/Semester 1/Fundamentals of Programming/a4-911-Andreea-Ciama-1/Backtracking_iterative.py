def generateParenthesis( n):
    parentheses = [[] for i in range(n + 1)]
    parentheses[0] += '',
    for i in range(1, n + 1):
        for j, k in zip(range(i), reversed(range(i))):
            for x in parentheses[j]:
                for y in parentheses[k]:
                    parentheses[i].append('(' + x + ')' + y)
    return parentheses[-1]

if __name__ == '__main__':
    n = int(input("the number:"))
    print(generateParenthesis(int(n/2)))