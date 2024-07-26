def twoSum(nums, target):
    pass



if __name__ == "__main__":
    nums = [
        [2,7,11,15],
        [3,2,4],
        [3,3]
    ]
    target = [
        9,
        6,
        6
    ]
    for i in range(len(nums)):
        print(f"nums = {nums[i]} | target = {target[i]}")
        print(twoSum(nums[i],target[i]))
