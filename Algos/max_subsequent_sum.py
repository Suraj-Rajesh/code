def get_max_sum(array):
    max_sum = array[0]
    running_sum = max_sum
    for index in range(1, len(array)-1):
        running_sum += array[index]
        # If individual element itself overpowers running sum, then running sum
        # changes to be the element(running sum starts from the element). Else,
        # running sum continues. 
        if array[index] > running_sum:
            running_sum = array[index]

        max_sum = running_sum if running_sum > max_sum else max_sum
    return max_sum

if __name__ == '__main__':
    print get_max_sum([1,2,3,-2,5,-4])
