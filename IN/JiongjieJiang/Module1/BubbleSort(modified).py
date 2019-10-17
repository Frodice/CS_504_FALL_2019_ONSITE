def bubble_sort(list, order):
    sorted_list = list[:]
    is_sorted = False
    while is_sorted == False:
        swaps = 0
        if(str(order) == "rise"):
            for i in range(len(list) - 1):
                if sorted_list[i] > sorted_list[i + 1]: # swap
                    # temp = sorted_list[i]
                    # sorted_list[i] = sorted_list[i + 1]
                    # sorted_list[i + 1] = temp
                    sorted_list[i], sorted_list[i + 1] = sorted_list[i + 1],sorted_list[i]
                    swaps += 1
                    print(swaps)
        elif(str(order) == "decline"):
            for i in range(len(list) - 1):
                if sorted_list[i] < sorted_list[i + 1]: # swap
                    sorted_list[i], sorted_list[i + 1] = sorted_list[i +1 ],sorted_list[i]
                    swaps += 1
                    print(swaps)
        if swaps == 0:
            is_sorted = True
    return sorted_list

print(bubble_sort([2, 1, 3, 7, 4, 6], "rise"))
print(bubble_sort([2, 1, 3, 7, 4, 6], "decline"))