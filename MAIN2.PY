lst=[10,19,7,11]
print(lst)


count=0
for i in lst:
    count+=i


average=count/len(lst)
print("the sum is ",count)
print("average is ",average)


lst.sort()
print(lst)