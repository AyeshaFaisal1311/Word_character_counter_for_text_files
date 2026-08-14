text = input("Enter your text:")

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

for char in text:
    if char == " ":
        continue
    
    char_count[char]=char_count.get(char,0) + 1
print(f" Character count: {char_count}")    