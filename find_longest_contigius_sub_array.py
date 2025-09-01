


# a_list = []

a = [1,2,4,5,6,7,7]
target = 16

current_total=0

import copy
def find_non_repetitive_longest_sub_array(array_items, target):
    current_total = 0
    st=0
    nt=0
    new_target = copy.deepcopy(target)
    while nt <len(array_items):
        current_total = current_total+array_items[nt]
        if current_total == new_target:
            return [st, nt]
        elif current_total < new_target:
            new_target = new_target-array_items[nt]
            nt +=1
        else:
            while current_total > target:
                current_total = current_total-array_items[st]
                st +=1
            if current_total == target:
                return [st, nt]
            nt +=1
    return -1


res=find_non_repetitive_longest_sub_array(a, target)
print(res)
