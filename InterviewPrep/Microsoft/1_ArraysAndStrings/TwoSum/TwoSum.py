def TwoSum(input, target):
    L = len(input)
    for i in range(L):
        for j in range(i+1,L):
            sum = input[i] + input[j]
            #print(f"[{i}][{j}] = {sum}")
            if (sum == target):
                return [i,j]
    return [-1,-1]

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
