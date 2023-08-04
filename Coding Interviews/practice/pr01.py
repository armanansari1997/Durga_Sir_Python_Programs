# Input :
# Dice:2
# Num:628692

def sum_of_digits(dice, nums):
    nums = str(nums)
    result = 0
    if dice % 2 == 0:
        for num in nums[::2]:
            result += int(num)
    else:
        for num in nums[1::2]:
            result += int(num)
    return result


print(sum_of_digits(2, 628692))


# Output:
# 23
# Explanation:
# Sum of digits at odd positions =6+8+9 =23
# Sum of digits at even positions = 2+6+2 = 10
# Since,the dice is even , sum of digits at odd positions is returned. So, output is 23
