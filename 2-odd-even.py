x=input("input number1：")
y=input("input number2：")
z=input("input number3：")
x=int(x)
y=int(y)
z=int(z)

answer = min(x,y,z)
if x%2!=0:
    answer = x
if y%2!=0 and y>x:
    answer = y
if z%2!=0 and z>answer:
    answer = z
print(answer)