def TwoSum(input, target):
    hashmap = {}
    for i in range(len(input)):
        compliment = target - input[i]
        if compliment in hashmap:
            return [hashmap[compliment], i]
        hashmap[input[i]] = i


if __name__ == '__main__':
    # EX1
    nums = [2,7,11,15]
    target = 9
    ans = TwoSum(nums, target)  # output = [0,1]
    print(f"nums = {nums} | target = {target}")
    print(f"answer = {ans}\n")
    # EX2
    nums = [3,2,4]
    target = 6
    ans = TwoSum(nums, target)  # output = [0,1]
    print(f"nums = {nums} | target = {target}")
    print(f"answer = {ans}\n")
    # EX3
    nums = [3,3]
    target = 6
    ans = TwoSum(nums, target)  # output = [0,1]
    print(f"nums = {nums} | target = {target}")
    print(f"answer = {ans}\n")
