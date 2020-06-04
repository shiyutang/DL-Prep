# Python program for KMP Algorithm
def KMPSearch(pat, txt):
    M,N = len(pat),len(txt)
    # create pi[] that will hold the longest prefix suffix values for pattern
    pi = [0] * M
    j = 0  # index for pat[]

    # Preprocess the pattern ()
    computeLPSArray(pat, M, pi) #calculate pi[] array

    i = 0  # index for txt[]
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1

        if j == M:
            print("Found pattern at index " + str(i - j))
            j = pi[j - 1]
            return i-j

            # mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            # Do not match pi[0..pi[j-1]] characters,
            # they will match anyway
            if j != 0:       # 在匹配了部分字符串之后不匹配，那么，变换模式指向位置，使得其右移j-π[j]位
                j = pi[j - 1]
            else:            # 一个也没有匹配上,pattern移向下一位
                i += 1


def computeLPSArray(pat, M, pi):
    len = 0  # length of the previous longest prefix suffix

    pi[0] = 0 # pi[0] is always 0
    j = 1
    # the loop calculates pi[i] for i = 1 to M-1
    while j < M:
        if pat[j] == pat[len]:
            len += 1
            pi[j] = len
            j += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similarto search step.
            if len != 0:
                len = pi[len - 1]
            else:
                pi[j] = 0
                j += 1

txt = "ABABDABACDABABCAdsdfBAB"
pat = "ABAB"
KMPSearch(pat, txt)
