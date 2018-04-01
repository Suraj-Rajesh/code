def bubble_sort(numlist):
    """ Standard bubble sort algorithm """

    # (n-1) outer passes
    for i in range(len(numlist)-1):
        index = 0

        # No of comparisons per pass (reduces every pass)
        for j in range(len(numlist)-1, 0, -1):
            if numlist[index] > numlist[index + 1]:
                # swap
                numlist[index], numlist[index + 1] = numlist[index + 1], \
                                                     numlist[index]
            index += 1

    return numlist
