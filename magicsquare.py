def magic_square(mat):
 row_sum=col_sum=diag1_sum=diag2_sum=0
 l=[]
 for i in range(len(mat)):
   row_sum=col_sum=0
   for j in range(len(mat)):
     row_sum=row_sum+mat[i][j]
     col_sum=col_sum+mat[j][i]
     if i==j:
       diag1_sum=diag1_sum+mat[i][j]
     if (i+j)==(n-1):
       diag2_sum=diag2_sum+mat[i][j]
   l=l+[row_sum]+[col_sum]
 l=l+[diag1_sum]+[diag2_sum]
 if min(l)==max(l):
    return l,'YES'
 else:
    return l,'NO'

n=int(input())
line = input()
mat=[]
for i in range(n):
 num_str = line.split(' ')
 numbers = [ ]                   
 for item in num_str:
     numbers.append(int(item))
 mat.append(numbers)
 line = input()
print(magic_square(mat))