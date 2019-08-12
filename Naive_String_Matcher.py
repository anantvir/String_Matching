"""Author - Anantvir Singh, concept reference:= CLRS Page 988"""

# We will insert None at index 0 of array T and P to keep the program simple and understandable as per CLRS
def Naive_String_Matcher(T,P):
    n = len(T)
    m = len(P)
    # In CLRS, arrays P and T are assumed to start from index 1, so s starts from 0, but in python index starts from 0, so 's' starts from -1, so that s+1 = 0, which is 1st element of array
    for s in range(-1,n-m):      # for s=0 to n-m, s here means shift. If s=0, it means that the pattern starts at index s+1 i.e the 1st element of array
        if P[:m+1] == T[s+1:s+m+1]:
            print("Pattern occurs with shift : ",s)



text = ['a','b','c','a','b','a','a','b','c','a','b','a','c']
pattern = ['a','b','a','a']

Naive_String_Matcher(text,pattern)
