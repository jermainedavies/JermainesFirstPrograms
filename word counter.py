text = 'i love to count words'
count = 0
for char in text:
    if char == ' ':
        count = count + 1
#must add one extra line for the last word
count = count + 1
print(count)