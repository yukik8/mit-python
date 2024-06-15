t = 1
nums = [0] * 10
while  t < 11:
    nums[t-1] = int(input('input plus number'))
    t=t+1

t=0
ans = -1
while t < 10:
    if nums[t]%2!=0 and nums[t] > ans:
        ans = nums[t]
    t=t+1

print('no odd number' if ans == -1 else ans)