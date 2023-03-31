def PushZero(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        if arr[i]!=0:
            arr[count]=arr[i]
            count+=1
    while count<n:
        arr[count] = 0
        count+=1
    print(arr) 
arr = [1,0,9,0,6,5,7,8,0,9,0]
PushZero(arr)
