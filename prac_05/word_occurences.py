"""
CP1404 - Ashton Stewart
word occurences
Time taken to write all code: 42:43.38
Time to add commens: 44:46:23
"""

#projected time: 45mins to an hour (including commenting and debugging)
#actual time:

user_input = []
user_input = str(input("What do you want to say?"))
input_string = user_input.split()

word_checker = [] #acts as a list of all unique words in the sentence
word_counter = {} #empty dictionary

for words in input_string: #loops through all words in the string
    word_recurrence = 0 #resets the count of that word

    if words not in word_checker: #checks if the current word is in word_counter

        for current_word in input_string: #loops through the list again to get how many times that word is seen

            if current_word == words: #checks if the currently looked at word matches the other currently looked at word
                word_recurrence +=1 #increases the count if it matches

        word_checker.append(words) #adds to the list of words that have been counted so they are not recounted
        word_counter[words] = word_recurrence #adds to the dictionary

#sets a new variable
max_length = 0

for length_to_check in word_checker: #goes through the previously created list of unique words

    new_length = len(length_to_check) #sees how long each word is

    if new_length > max_length: #sets the max length to anything bigger than it currently is
        max_length = int(new_length)

#prints each word and it's count.
for word_to_print, number in word_counter.items():

    #uses the max_length to format the text
    print(f"{word_to_print:{max_length}} : {number}")