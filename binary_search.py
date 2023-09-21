def binary_search(my_list, item):
    if my_list != sorted(my_list):
        return 'unsorted list'
    else:
        low = 0
        high = len(my_list)-1
        
        while low <= high:
            mid = (low+high)//2
            guess = my_list[int(mid)]
            if guess == item:
                return mid
                break
            elif guess > item:
                high = mid - 1
            else:
                low = mid + 1
        else:
            return 'not in list'