"""Author - Anantvir Singh, concept reference:= CLRS Page 993"""


# Inputs to algorithm are text T, the pattern P, the radix d (number of unique digits in the system), prime q

# It basically crates a hashcode for the pattern P, then for window size = length of pattern, it slides the window on the text array
# and for each window of size = m, it compares the hashcode of window with the hashcode of patter p. If both match, then individual characters are compared
# to verify if both window and pattern have same characters, if they dont match then move to next window. 
# When pattern p's hashcode and window's hashcode dont match, it is similar to collision in hashmaps


def Rabin_Karp_Matcher(T,P,d,q):
    n = len(T)
    m = len(P)
    h = d**(m-1) % q
    p = 0
    t_prev = 0
    t_s_plus_1 = None
    for i in range(m):                    # for i = 1 to m          // Preprocessing , here it is 0 to m-1 because arrays in python start from 0
        p = (d*p + P[i]) % q              # This line generates the hashcode for pattern P, Trace example on CLRS Page 992 for i =1,2,3,4,5 to understand the logic. Basically in each iteration, we are multiplying by 10 and adding a new member from P array into the result.
        t_prev = (d*t_prev + T[i]) % q    # Generates t_0 which is length 'm' substring from T[s+1,.....,s+m]
        t_s_plus_1 = t_prev
    for s in range(-1,n-m):               # for s = 0 to n-m        // Matching      , s starts from -1 because s+1 = 0 ==> pattern starts from 1st element of array which is at 0th index
        t_prev = t_s_plus_1
        if p == t_s_plus_1:
            if P[:m] == T[s+1:s+m+1]:
                print('Pattern occurs with shift :',s)
        if s < n-m-1:
            t_s_plus_1 = (d*(t_prev - T[s+1]*h) + T[s+m+1]) % q

text = [2,3,5,9,0,2,3,1,4,1,5,2,6,7,3,9,9,2,1]          # Will print only once
text1 = [2,3,5,9,0,2,3,1,4,1,5,2,6,7,3,1,4,1,5]         # Will print twice
pattern = [3,1,4,1,5]
radix = 10
prime_num = 13
Rabin_Karp_Matcher(text,pattern,radix,prime_num)

