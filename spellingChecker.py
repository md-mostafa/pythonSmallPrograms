from textblob import TextBlob
import re

words = input("Enter Words : ")
words = re.split(', |\s', words) ##split base on comma and whitespace
print(words)

textBlob_word_List=[]
corrected_List =[]

for word in words:
    w = TextBlob(word);
    textBlob_word_List.append(TextBlob(word))

for word in textBlob_word_List:
    corrected_List.append(word.correct()) #adds the corrected word

for word in words:
    if (word) not in corrected_List:
        print('Spelling error => ',word, ' => Correct word =>', TextBlob(word).correct())
    else:
        print('Correct => ', word)




