def order_by(nums):
    result_to_print = nums.sort()
    for i in result_to_print:
        print(i)


# order_by(input())

def for_num():
    for i in range(1, 10):
        print(round((10-i)/2) * " ", end="")
        for j in range(1, i+1):
            print(j, end="")
        print('')
    # print('')

for_num()