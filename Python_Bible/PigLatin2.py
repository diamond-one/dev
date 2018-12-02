#Get sentance from user
original = input("What would you like to translate?: ").strip().lower()
#Split sentance into words
words = original.split()

#loop though words and convert to pig latin
new_words = []

#if it starts with a vowel just add 'yay'
for listitem in words:
    if listitem[0] in "aeiou":
        new_word = listitem + "yay"
        new_words.append(new_word)

# Otherwise move the first consitnant cluster to the end and add 'ay'
    else:
        vowel_pos = 0
        for letter in listitem:
            if letter not in "aeiou":
                vowel_pos = vowel_pos + 1
            else:
                break
        cons = listitem[:vowel_pos]
        the_rest = listitem[vowel_pos:]
        new_word = the_rest + cons + "ay"
        new_words.append(new_word)

#Stick words back together
output = " ".join(new_words)

#Output the first sting
print (output)