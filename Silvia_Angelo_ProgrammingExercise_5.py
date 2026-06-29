#Program will allow user to enter a paragraph, including sentences which begin with numbers.
#Display each individual sentence and the count of sentences in the paragraph.

#Import regex
import re

#Function splits passage into a list of individual sentences.
def split_into_sentences(passage):
    #Sentence pattern to recognize capitalized letters or numbers.
    sentence_pattern = r'\s(?=[A-Z]|[0-9])'
    #Look-ahead pattern to split up sentences.
    sentences = re.split(sentence_pattern, passage)
    return sentences

#Function driver that gathers user's passage, splits sentences, and prints results.
def main():
    #Prompt user to input paragraph.
    user_passage = input("Please enter your paragraph: ")
    sentence_list = split_into_sentences(user_passage)
    #Loop to display each individual sentence.
    for sentence in sentence_list:
        print(sentence)
    #Using len() to count total number of sentences.
    total_sentence_count = len(sentence_list)
    print(f"Your total number of sentences: {total_sentence_count}")

if __name__ == "__main__":
    main()



