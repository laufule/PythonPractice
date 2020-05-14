# loops for python
bickles = ['one','two','three','four','five']
for bickle in bickles:
    print(bickle)

# 循环中赋值
car = []
for value in range(1,10):
    car.append(value**2)
print(car)

# list中使用循环赋值
moto = [value**2 for value in range(1,15)]
print(moto)

linux = list(range(1,20,2))

