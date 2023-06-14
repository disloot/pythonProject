
def bsearch(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if target<arr[mid]:
            high=mid-1
        elif target>arr[mid]:
            low=mid+1
        else:
            return mid
    return -1
if __name__ == '__main__':
    arr=[0, 6, 23, 30, 35, 46, 48, 57, 64, 66]
    print(bsearch(arr,66))