# Debugging Independent Warm-Up
# This loop should get a word from the user and
    # print out each individual letter of the word
    # until the user enters ‘stop’.
word = ""
while (word != "stop"):
    word = input("Enter a word (type 'stop' to quit):")
    # hello h = 0, e = 1, l = 2, l = 3, o = 4
    # list = ['a', 'b', 'c']
    # print(list[0]) # a

    for letter in word:
        print(letter)

    # for i in range(len(word)):
    #     print(word[i])