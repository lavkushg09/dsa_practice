def merge_short(list):

    n = len(list)
    if n<=1:
        return list
    
    middle = n//2
    left = merge_short(list[:middle])
    right = merge_short(list[middle:])

    st=end=0
    res=[]
    while st<len(left) and end<len(right):
        if left[st] < right[end]:
            res.append(left[st])
            st+=1
        else:
            res.append(right[end])
            end+=1
    res+=left[st:]
    res+=right[end:]
    return res


if __name__ == "__main__":
    list = [5,3,6,2,10,1,4]
    print(merge_short(list))
    