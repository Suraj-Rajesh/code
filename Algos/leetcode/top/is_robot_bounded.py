# https://leetcode.com/problems/robot-bounded-in-circle/

def isRobotBounded(instructions):
    # directions
    # north - 0, east - 1, south - 2, west - 3
    #
    # note that we are setting directions based on how we rotate
    #
    # initially, it is facing north, hence 0
    # if rotated right, we are facing east, hence 0 + 1 = 1
    # similarly, again, right, we are south-facing, hence, 1 + 1 = 2
    # same for west, hence 3
    #
    # thus, if rotating right - we should do, (direction + 1) % 4
    # and rotating left - we should do, (direction - 1) % 4
    #
    # we do % 4 since we only have 4 directions from 0 - 3
    #

    #
    # SOLUTION:
    #
    # OPTIMAL: the idea here is that(math involved) - if after one instruction
    # set, robot is at origin (or) not-north facing, it is bound
    #
    #             (OR)
    #
    # another solution is that, if robot gets back to origin after 4 iterations
    # of instruction set, then, it is bound
    #
    north = 0
    east  = 1
    south = 2
    west  = 3

    x = y = 0
    direction = north

    # instructions can be one of 'G', 'L', 'R'
    for instruction in instructions:
        if instruction == 'G':
            if direction == north:
                y += 1
            elif direction == east:
                x += 1
            elif direction == south:
                y -= 1
            elif direction == west:
                x -= 1
        elif instruction == 'L':
            direction = (direction - 1) % 4
        elif instruction == 'R':
            direction = (direction + 1) % 4

    return (x == 0 and y == 0) or direction != north

print(isRobotBounded('GGLLGG'))
print(isRobotBounded('GG'))
print(isRobotBounded('GL'))
