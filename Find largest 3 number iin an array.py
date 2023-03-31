def MaxNum(arr):
    n = len(arr)
    if (n<3):
        print("Invalid Input")
        return
    third=second=first=float('-inf')
    for i in range(n):
        if arr[i]>first:
            third = second
            second = first
            first = arr[i]
        elif arr[i]>second:
            third = second
            second = arr[i]
        elif arr[i]>third:
            third = arr[i]
    print(first,second,third)
arr = [5,20,70,87,1,0,2]
MaxNum(arr)
