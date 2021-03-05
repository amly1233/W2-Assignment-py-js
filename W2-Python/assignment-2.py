# 要求一:在函式中 使用迴圈 計算最小值到最大值之間，所有整數的總和
def calculate(min, max):
    sum=0
    for x in range(min,max+1):
        sum+=x
    print(sum)
calculate(1, 3) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8) # 你的程式要能夠計算 4+5+6+7+8，最後印出 30

print("--------------------")
# 要求二:正確計算出員工的平均薪資，請考慮員工數量會變動的情況。
def avg(data):
  sum=0
  for n in range(data["count"]):
      sum+=data["employees"][n]["salary"]
  print(sum/data["count"])

avg({
"count":3,
"employees":[
{
"name":"John",
"salary":30000
},
{
"name":"Bob",
"salary":60000
},
{
"name":"Jenny",
"salary":50000
}
]
}) # 呼叫 avg 函式

print("--------------------")
# 要求三:找出至少包含兩筆整數的列表 (Python)中，兩兩數字相乘後的最大值。
def maxProduct(nums):
    max=nums[0]*nums[1]
    for i in range(len(nums)-1):
        for k in range(i+1,len(nums)):       
            if (nums[i]*nums[k]>max):
                max=nums[i]*nums[k]
    print(max)  
maxProduct([5, 20, 2, 6]) # 得到 120 因為 20 和 6 相乘得到最大值
maxProduct([10, -20, 0, 3]) # 得到 30 因為 10 和 3 相乘得到最大值

print("--------------------")
# 要求四:Given an array of integers, show indices of the two numbers such that they add up to a
# specific target. You can assume that each input would have exactly one solution, and you
# can not use the same element twice.
def twoSum(nums, target):
    for i in range(len(nums)-1):
        for k in range(i+1,len(nums)):
            if (nums[i]+nums[k]==target):
                return ([i,k])
result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9

print("--------------------")
# 要求五:給定只會包含 0 或 1 兩種數字的列表 (Python)，計算連續出現 0 的最大長度。
# def maxZeros(nums):
# # 請用你的程式補完這個函式的區塊
# maxZeros([0, 1, 0, 0]) # 得到 2
# maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
# maxZeros([1, 1, 1, 1, 1]) # 得到 0
