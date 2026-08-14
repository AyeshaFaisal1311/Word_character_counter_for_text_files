def count_chars(text):
    char_count=len(text)
    space_counter = 0
    for char in text:
        if char ==' ':
            space_counter += 1
    characters_count_without_spaces = len(text) - space_counter
          
    return char_count , characters_count_without_spaces

def count_words(text):
    words_list=text.split()
    words=len(words_list)
    return words

def char_frequency(text):
    char_count={}
    for char in text:
        if char == " ":
            continue
        char_count[char]=char_count.get(char,0) + 1
    
    return char_count

def main():
    text=input("Enter your text")
    total_chars, chars_no_spaces = count_chars(text)
    print(f'Character (with spaces): {total_chars}')
    print(f"Characters without spaces: {chars_no_spaces}")
    print(f"Words Count: {count_words(text)}")
    print(f"Characters occurrence: {char_frequency(text)}")
    
main()    
