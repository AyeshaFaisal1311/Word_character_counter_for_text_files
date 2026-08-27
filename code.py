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

def word_frequency(text):
    stopwords=['the', 'is','a', 'an', 'and', 'on', 'in', 'to', 'of']
    frequent_words={}
    words=text.split()
    for word in words:
        word= word.strip('.,!~?";:\'').lower()
        if word not in stopwords:
            frequent_words[word]=frequent_words.get(word,0) +1
    sorted_list=sorted(frequent_words.items(), key=lambda x: x[1], reverse=True)
    sorted_words=sorted_list[:5]
    return sorted_words



def main():
    text=input("Enter your text")
    total_chars, chars_no_spaces = count_chars(text)
    print(f'Character (with spaces): {total_chars}')
    print(f"Characters without spaces: {chars_no_spaces}")
    print(f"Words Count: {count_words(text)}")
    print(f"Characters occurrence: {char_frequency(text)}")
    print(f"Frequent words: {word_frequency(text)}")
    
main()    
