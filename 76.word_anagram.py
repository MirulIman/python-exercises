# Create a program that reads two words and checks if the
# second word is an anagram of the first.


word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

# convert both word to lowercase and remove whitespace
word1 = word1.lower().replace(" ", "")
word2 = word2.lower().replace(" ", "")

# check if the lengths of the words are equal
if len(word1) != len(word2):
    print("The second word is not an anagram of the fisrt.")
else:
    # sort the characters of both words
    sorted_word1 = sorted(word1)
    sorted_word2 = sorted(word2)
    
    # check if the sorted words are equal
    if sorted_word1 == sorted_word2:
        print("The second word is an anagram of the first.")
    else:
        print("The second word is not an anagram of the first.")