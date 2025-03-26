# Creating A function to open and Read text files:
def read_the_file(filename):
    with open(filename, 'r') as file:
        return file.read()
content = read_the_file('sample.txt')
#Counting the Number of Lines....
def count_lines(content):
    return len(content.split('\n')) #Use \ instead of /
num_of_lines = count_lines(content)
print(f"The number of Lines in The Text file is: {num_of_lines} ") 
#Counting Total Number of words in the text
def number_of_words(content):
    return len(content)
total_words = number_of_words(content.split())
print(f"The total number of words is: {total_words}")
#Finding the most common words in the text
from collections import Counter
def common_words_in_text(content):
    words = content.lower().split()
    common_words_to_count = Counter(words)
    return common_words_to_count.most_common(1)[0] #[1] for only count and (0) for only the most common word
common_word , count = common_words_in_text(content)
print (f"Most common words is: '{common_word}' and it appear {count} number of times! ")
#Calculate Average Word Length
def Average_word_length(content):
    words = content.split()
    total_words = sum(len(words) for words in words)
    return total_words / len(words)
Avg_words = Average_word_length(content)
print (f"The average number of words in the Text is: {Avg_words:.2f} characters")
def analyze_text(filename):
    content = read_the_file(filename)
    
    num_lines = count_lines(content)
    num_words = number_of_words(content)
    common_word, count = common_words_in_text(content)
    avg_length = Average_word_length(content)
    
    print(f"File: {filename}")
    print(f"Number of lines: {num_lines}")
    print(f"Number of words: {num_words}")
    print(f"Most common word: '{common_word}' (appears {count} times)")
    print(f"Average word length: {avg_length:.2f} characters")

# Run the analysis
analyze_text('sample.txt')
