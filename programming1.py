l=[1,2,2,3,4,4,5,6,6]
r=[]
for i in l:
    if i not in r:
        r.append(i)
print("Original List:",l)
print("After Removing Duplicates:",r)

# Output:
# Original List: [1, 2, 2, 3, 4, 4, 5, 6, 6]
# After Removing Duplicates: [1, 2, 3, 4, 5, 6]
