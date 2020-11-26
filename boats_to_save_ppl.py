
def min_boats_num(ppl_list, limit):
    ppl_len = len(ppl_list)
    i = 0
    j = ppl_len - 1
    boats_c = 0
    ppl_list.sort()

    while i <= j:
        if i == j:
            boats_c += 1
            break

        p1 = ppl_list[i]
        p2 = ppl_list[j]

        if p1 + p2 <= limit:
            boats_c += 1
            i += 1
            j -= 1
        else:  # p2 < limit
            boats_c += 1
            j -= 1

    return boats_c


if __name__ == '__main__':

    my_ppl_list = [4, 3, 3, 2, 2, 2, 1, 1]
    min_num = min_boats_num(my_ppl_list, 5)  # answer should be 4
    ppl_list_2 = [5]
    min_num_2 = min_boats_num(ppl_list_2, 5)  # answer should be 1
    ppl_list_3 = [1, 3, 3, 2]
    min_num_3 = min_boats_num(ppl_list_3, 3)  # answer should be 3

    print(min_num)
    print(min_num_2)
    print(min_num_3)
