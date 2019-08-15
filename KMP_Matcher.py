"""Author - Anantvir Singh, concept reference:= CLRS Page 1005"""

# For theory refer ==> https://www.youtube.com/watch?v=V5-7GzOfADQ

def Compute_Prefix_Function(P):
    m = len(P)
    pi = [None] * m                         # create empty pi array of size m
    pi[1] = 0                          # make 1st index = 0  pi[1] = 0, but here make 0th index = 0 because array indices start from 0
    k = 0
    for q in range(2,m):                    # for q = 2 to m
        while k > 0 and P[k+1] != P[q]:
            k = pi[k]
        if P[k+1] == P[q]:
            k += 1                          # Increment k
        pi[q] = k
    return pi

def KMP_Matcher(T,P):
    n = len(T)
    m = len(P)
    pi = Compute_Prefix_Function(P)
    q = 0
    for i in range(1,n):
        while q > 0 and P[q+1] != T[i]:
            q = pi[q]
        if P[q+1] == T[i]:
            q += 1
        if q == m:
            print('Pattern occurs with shift :',i-m)
            q = pi[q]



text = [None,'a','b','a','b','c','a','b','c','a','b','a','b','a','b','d']
pattern = [None,'a','b','a','b','d']

KMP_Matcher(text,pattern)
