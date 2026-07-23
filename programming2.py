l=[1,2,2,3,4,4,4,5]
for i in l[:]:
    if i in l:
        print(i,"=",l.count(i))
        while i in l:
            l.remove(i)

# Output:
# 1 = 1
# 2 = 2
# 3 = 1
# 4 = 3
# 5 = 1
