"""
Determine the longest common subsequence of two given sequences.
Subsequence elements are not required to occupy consecutive positions.
For example, if X = "MNPNQMN" and Y = "NQPMNM",
the longest common subsequence has length 4, and can be one of "NQMN", "NPMN" or "NPNM".
Determine and display both the length of the longest common subsequence as well as at least one such subsequence.
"""


def LCS(s, t):
    sSub = ""
    tSub = ""
    if len(s) != 0:
        sSub = s[1:len(s)]
    if len(t) != 0:
        tSub = t[1:len(s)]
    if len(s) == 0 or len(t) == 0:
        return ""
    if s[0] == t[0]:
        firstOfS = ""
        firstOfS += s[0]
        firstOfS += LCS(sSub, tSub)
        return s[0] + LCS(sSub, tSub)
    else:
        a = LCS(sSub, t)
        b = LCS(s, tSub)
        if len(a) > len(b):
            return a
        else:
            return b


if __name__ == '__main__':
    x= input("the first string:")

    y= input("the second string:")
    print(LCS(x, y))
    print(len(LCS(x,y)))

