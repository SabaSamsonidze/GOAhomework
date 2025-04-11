# დავალება 1

def filter_divisible_numbers(nums, divisors):
    result = []
    for i in nums:
        if i % divisor == 0:
            result.append(i)
    return result

numbers_list = [1, 23, 165, 2, 3, 92, 10, 34, 911]
divisor = 3
result_list = filter_divisible_numbers(numbers_list, divisor)
print(result_list)