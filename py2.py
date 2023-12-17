# Open T1.txt file for reading
with open("T1.txt", "r") as fileRead:
    # Read the content of T1.txt and split it into a list of words
    word_list = fileRead.read().split()

    # Sort the list of words lexicographically and by length
    word_list.sort(key=lambda item: (item, len(item)))

    # Print the sorted list of words
    print("List of sorted words is:")
    print(word_list)

    # Open T2.txt file for writing
    with open("T2.txt", "w") as fileWrite:
        # Write the sorted words to T2.txt, each on a new line
        for word in word_list:
            fileWrite.write(str(word) + "\n")
