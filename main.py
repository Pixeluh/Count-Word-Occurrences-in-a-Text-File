user_file = str(input("What file would you like to search? (Ex: test_file.txt): "))
user_word = str(input("What word would you like to search for?: (Ex: butter): "))
word_count = 0

use_file = open(user_file, "r+")

for line in use_file:
    use_file.readline()
    for character in line.split():
        if character == user_word.upper():
            word_count += 1
        elif character == user_word.lower():
            word_count += 1
        elif character == user_word.capitalize():
            word_count += 1


use_file.close()

print("'" + user_word + "'", "occurs", word_count, "times.")
