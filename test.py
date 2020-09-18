def solution(A):
    # params: an array of integers
    # returns: smallest positiver integer, greater than 0

    sorted_a = sorted(A)

    most_max = 0
    less_max = 0

    for ele in sorted_a:
        if ele > most_max and ele > 0:
            less_max = most_max
            most_max = ele
        elif ele > less_max:
            less_max = ele

        # elif most_max > ele > less_max and ele > 0:
        #     less_max = ele

    print(most_max, less_max)
    if (most_max - less_max == 1) or (most_max == less_max):
        return most_max + 1
    elif less_max >= 0:
        return less_max + 1
    else:
        return 0


    pass


a = list(range(0, 100))

print(solution(a))

