# 3.2
s = [2,5,6,7, 2]
a = set(s)
print( len(a))
# 3.3
print(s[::-1])
# 3.4
x = 2
print([i for i in range(len(s))  if s[i] == 2 ])
# 3.5
print(sum(s[::2]))
#3.6
s = ["ajdjdj", "dhhd", "ueisjdbdjdhvd"]
print(max(s, key=len))
#3.7
s = 120
print(s if(s % sum(int(d) for d in str(s) )) == 0 else 0)
#3.8
from itertools import groupby

def rle_encode(x):
    return [(l, len(list(g))) for l, g in groupby(x)]
print(rle_encode('ABBCCCDEF'))
 
# [('A', 1), ('B', 2), ('C', 3), ('D', 1), ('E', 1), ('F', 1)] 

#4.1
def multiply_ad(A, B):
 mul = list()
 for i in range(len(A)):
  m = list()
  for j in range(len(B)):
   m.append(A[i][j]*B[i][j])
  mul.append(m)
 return mul
 
print(
multiply_ad(
[[0,2],
[3,0]],

[[1,4],
[2,0]])
 ) # = [[0, 8], [6, 0]] 
'''
a = (0 2)   b = (1 4)
      (3 0)          (2 0)
'''

# 4.2
A = [
[0,2,1],
[1,0,3],
[0,1,1]
]
def transpose(A):
 C = list()
 for i in range(len(A)):
  C_str = []
  for j in range(len(A[i])):
   C_str.append(A[j][i])
  C.append(C_str)
 return C
C = transpose( [[0,2,1],[1,0,3],[0,1,1]]) 
print(C)

# 4.3
def multiply(A, B):
 mul = []
 
 for i in range(len(A)):
  m_lev_1 = list()
  for j in range(len(B[0])):
   su = 0
   for k in range(len(B)):
    su += A[i][k] * B[k][j]
   m_lev_1.append(su)
  mul.append(m_lev_1)
 return mul
 
print(

(multiply(
[[1,2],
[3,4],  # A
[5,6]],

[[1,2,3],  # B
[4,5,6]])) 

) # = dot(A, B) = [[9, 12, 15], [19, 26, 33], [29, 40, 51]]

# 5.1
