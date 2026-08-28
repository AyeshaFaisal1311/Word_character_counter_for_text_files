def count_chars(text):
    '''Count total number of Character with spaces and without spaces'''
    char_count=len(text)
    space_counter = 0
    for char in text:
        if char ==' ':
            space_counter += 1
    characters_count_without_spaces = len(text) - space_counter
          
    return char_count , characters_count_without_spaces

def count_words(text):
    ''' Count total number of words'''
    words_list=text.split()
    words=len(words_list)
    return words

def char_frequency(text):
    '''tells how many times a character occurs in text'''
    char_count={}
    for char in text:
        if char == " ":
            continue
        char_count[char]=char_count.get(char,0) + 1
    
    return char_count

def word_frequency(text):
    '''Returns the top 5 most occuring words excluding stopwords'''
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
    choice = input ("Enter your choice (1.type text, 2 read from file):")
    if choice == '1':
        text=input("Enter your text")
        
    else:
        while True: 
            file_path=input("Enter file path(if you copy the path please remove quotes):")
            try:       
                with open(file_path,'r') as file:
                    text= file.read()
                break    

            except FileNotFoundError:
                print(f"File not Found, try again")
    if text=="":
        print("text is empty. Nothing to analyze.")
        return            
    filename=input("Enter filename to save report (e.g. report.txt)") 
    with open(filename,'w') as file:
        total_chars, chars_no_spaces = count_chars(text)
        print(f'Character (with spaces): {total_chars}')
        file.write(f'Character (with spaces): {total_chars}\n')
        print((f"Characters without spaces: {chars_no_spaces}"))
        file.write(f"Characters without spaces: {chars_no_spaces}\n")
        total_words=count_words(text)
        print(f"Words Count: {total_words}")
        file.write(f"Words Count: {total_words}\n")
        total_occurrence=char_frequency(text)
        print(f"Characters occurrence: {total_occurrence}")
        file.write(f"Characters occurrence: {total_occurrence}\n")
        frequent_words=word_frequency(text)
        print((f"Frequent words: {frequent_words}"))
        file.write(f"Frequent words: {frequent_words}\n")
    print(f"Report save to {filename}")
main()    

