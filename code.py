text=input("Enter your text:")

print(f"Characters Count with spaces: {len(text)}")
#Without spaces
space_counter = 0
for char in text:
    if char ==' ':
        space_counter += 1

characters = len(text) - space_counter
print(f"Characters Count without spaces: {characters}")


# word count 
words_list=text.split()
print(f"words in a text: {len(words_list)}")

#character occurence
char_count={}
print(char_count)
for char in text:
    if char == " ":
        continue
    else:
        if char in char_count:
         char_count[char] +=1
print(char_count)