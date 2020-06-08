s = 'bobobobobob'
bob = 'bob'
count = 0
i = 0
for char in s:
    if s[i:i + 3] == bob:
        print(s[i:i +3])
        count += 1
    i += 1
print('Number of times bob occurs is: ' + str(count))

#ans = 5
