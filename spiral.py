
#size initial
n  = 5
cnt_el = n*n

res = []
for i in range(1, cnt_el+1,1):
    res.append(i)


def spiral(list_res, r,c):

    top = 0
    bottom = r-1
    left = 0
    right = c -1

    
    res_mat = [ [0 for i in range(n)] for i in range(n)]

    cnt = 0
    while top <= bottom and left <=right:

        for i in range(left, right+1):
            res_mat[top][i] = list_res[cnt]
            cnt +=1

        top +=1

        for i in range(top, bottom+1):
            res_mat[i][right] = list_res[cnt]
            cnt +=1

        right = right-1

        
        if top<=bottom:
            for i in range(right, left-1, -1):
                res_mat[bottom][i] = list_res[cnt]
                cnt +=1 

            bottom -=1

        if left <= right:
            for i in range(bottom, top-1, -1):
                res_mat[i][left] = list_res[cnt]
                cnt +=1

            left += 1 

    
    return res_mat
    


fin_mat = spiral(res,n,n)

for row in fin_mat:
    print(row)







