
"""
Generate all sequences of n parentheses that close correctly.
Example: for n=4 there are two solutions: (()) and ()()
"""
def printParenthesis(str, pos, n,
                      open, close):
    if n>0:
        if close == n/2:
            for i in str:
                print(i, end="")
            print()
            return
        else:
            if (open > close):
                str[pos] = ')'
                printParenthesis(str, pos + 1, n,
                                  open, close + 1)
            if (open < n/2):
                str[pos] = '('
                printParenthesis(str, pos + 1, n,
                                  open + 1, close)


if __name__ == '__main__':
    n = int(input("the number:"))
    str = [""]  * n
    printParenthesis(str, 0,
                      n, 0, 0)
