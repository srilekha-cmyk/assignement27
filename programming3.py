l=[1,2,2,3,4,4,4,5]
m=0
e=0
for i in l:
    if l.count(i)>m:
        m=l.count(i)
        e=i
print("Most Frequent Element:",e)

# Output:
# Most Frequent Element: 4
