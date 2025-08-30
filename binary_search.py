def binary_search(array_list, target):
    st =0
    et = len(array_list)-1

    while st<=et:
        mid = (st+et) // 2
        print(mid)
        if array_list[mid] == target:
            return mid
        elif array_list[mid]>target:
            et = mid-1
        else:
            st = mid+1
    return -1
        

if __name__ == "__main__":
    ar_l = [1,2,3,4,5,7,8,9,10,14]
    print(binary_search(ar_l, 9),"====")