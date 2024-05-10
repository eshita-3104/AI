def is_safe(arr,x,y,n):
    for row in range(x):
        if arr[row][y]==1:
            return False

    row = x
    column = y

    while row>=0 and column>=0:
        if arr[row][column]==1:
            return False
        row-=1
        column-=1

    row = x
    column = y

    while row>=0 and column<n:
        if arr[row][column]==1:
            return False
        row-=1
        column+=1

    return True

def n_queen(arr,x,n):
    if x>=n:
        return True

    for col in range(n):
        if is_safe(arr,x,col,n):
            arr[x][col]=1

            if n_queen(arr,x+1,n):
                return True
            arr[x][col]=0

    return False

def main():
    n=int(input("Entre the number of queens: "))
    arr = [[0]*n for i in range(n)]

    if n_queen(arr,0,n):
        for i in range(n):
            for j in range(n):
                print(arr[i][j],end = " ")
            print()


if __name__=="__main__":
    main()






    
