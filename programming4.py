l=[1,2,2,3,4,4,4,5]
m=l.count(l[0])
e=l[0]
for i in l:
    if l.count(i)<m:
        m=l.count(i)
        e=i
print("Least Frequent Element:",e)

# Output:
# Least Frequent Element: 1
