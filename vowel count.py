def count_vowels(sentence):
    count = 0
    vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
    for char in sentence:
        if char in vowels:
            count += 1
    return count
        
print(count_vowels("aware where you stand in the pain to power chart.  This is half the battle won.ur life‐ work, relationships, environment"))
#note to self: strings can't exist over more than one line?

