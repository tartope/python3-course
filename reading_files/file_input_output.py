# File I/O (input/output)

# Reading Files:
# - You can read a file with the open() function
# - open() returns a file object to you (at bare minimum you must pass in the filename); the file doesn't just have data, it has metadata in it, therfore an object is returned
# - You can read a file object with the read() method
# - See the documentation: search built-in functions then search open()

# # run in REPL:
# f = open("story.txt")
# f  #//=> <_io.TextIOWrapper name='story.txt' mode='r' encoding='UTF-8'>
# # must use read(), to get contents; if a number is not passed as a parameter in read(), it will specify -1 and you get the entire file.
# f.read()  #//=> 'This short story is really short.\n' (the \n is because the file has an empty new line)
# f.read()  #//=>  '' (empty string is returned when we want to read it a second time)  <-- Cursor Movement explains this, see below

# # Cursor Movement:
# # - Python reads files by using a cursor
# # - This is like the cursor you see when you're typing (the cursor progresses through the file as you read/type)
# # - After a file is read, the cursor is at the end; so if you try to read from there, there's nothing left and you get the empty string.
# # - To move the cursor, use the seek() method (this is how we manipulate the position of the cursor, like reset it to the beginning, or the 10th character, or whatever we want)

# # run in REPL
# file = open("story.txt")
# file.read()  #=>  'This short story is really short.\n\n'
# file.read()  #//=> ''
# # "story.txt" file updated with lines 2-3. (the Python cursor is still at the end of where it last read the file, so reading again moves the cursor to the end of the updates)
# file.read() #//=>  "ow it's a little longer\nThe end."
# file.read() #//=> ''
# file.seek(0) #//=> 0  <-- moves the cursor to the beginning
# file.read() #//=>  "This short story is really short.\nNow it's a little longer\nThe end."
# file.read() #//=>  ''
# file.seek(1) #//=> 1  <-- moves the cursor to the character in the 1st index
# file.read()  #//=>  "his short story is really short.\nNow it's a little longer\nThe end."
# file.read()  #//=> ''
# file.seek(50)  #//=> 50  <-- moves cursor to the character in the 50th index
# file.read()  #//=>  'e longer\nThe end.'
# file.seek(0) #//=> 0

# # readline(): this reads in chunks or a single line at a time; this reads the first line and stops when it reaches the \n character
# file.readline() #//=>  'This short story is really short.\n'
# file.read()  #//=>  "Now it's a little longer\nThe end."
# file.seek(0)
# file.readline()  #//=>  'This short story is really short.\n'
# file.readline()  #//=>  "Now it's a little longer\n"
# file.readline()  #//=>  'The end.'
# file.readline()  #//=>  ''

# # readlines(): this preserves each line as a line in a list, instead of returning them as one big string.
# file.seek(0)
# file.readlines()  #//=>  ['This short story is really short.\n', "Now it's a little longer\n", 'The end.']
# file.read()  #//=> ''

# # Until the file is manually closed, any changes made in the file get read; the connection is still open.  So, it's important to Close Files  <-- see below

# # Closing a File:
# # - You can close a file with the close() method
# # - You can check if a file is closed with the closed attribute
# # - Once closed, a file can't be read again until you re-open it (basically start over), using open() function.
# file.closed  #//=> False
# file.close() #//=> nothing is returned; it just closes the file
# file.closed  #//=> True
# file.read() #//=> ValueError: I/O operation on closed file.
# file.seek(0) #//=> ValueError: I/O operation on closed file.
# #_____________________________________________________________

# # "with" Blocks (the "with" statement is popular because you don't have to manually close it, it's done automatically):
# # Same as above but with a slightly different syntax that's commonly used.

# # "with" "open(file)" as "whatever name you want here (as long as it's not a reserved word":
# #       read and assign to variable name
# with open("story.txt") as file:
#     data = file.read()

# f #//=> <_io.TextIOWrapper name='story.txt' mode='r' encoding='UTF-8'>
# f.closed #//=> True
# f.read() #//=> ValueError: I/O operation on closed file.
# data #//=>  "This short story is really short.\nNow it's a little longer\nThe end."
#_____________________________________________________________

# Writing to Text Files:
# - You can also use open() to write a file; you still have to use the open() function
# - Need to specify the "w" flag as the second argument; with open() we did not bass any flags because the default is read, so now we must pass "w" flaf to write

# after the file is run, you will see the new lines written in haiku.txt:
# with open("haiku.txt", "w") as file:
#     file.write("Writing files is great\n")
#     file.write("Here's another line of text\n")
#     file.write("Closing now, goodbye!")

# after the file is run, you will see the lines overwrote the old lines in haiku.txt; this is how "write" behaves, at least when working with the "w" flag:
# with open("haiku.txt", "w") as file:
#     file.write("Here's one more haiku\n")
#     file.write("What about the older one?\n")
#     file.write("Let's go check it out")

# you don't have to have an existing file to write to; running this creates and writes a new file in the directory:
# with open("lol.txt", "w") as file:
#     file.write("haha" * 100)

#_____________________________________________________________

# Modes for Opening Files:
# - See the documentation: search built-in functions then search open(), you will see a chart that shows the different modes to open files
# - r: read a file (no writing) - this is the default
# - w: write to a file (previous contents are removed) (can make a new file if it doesn't exist')
# - a: append to a file (previous contents are not removed; we don't have control where the cursor is, it appends always to the end no matter what) (can make a new file if it doesn't exist')
# - r+: read and write to a file (writing based on cursor; things will be overwritten) (only works with existing files; does not create new files)

# this appends to the haiku.txt file, without overwriting it
# with open("haiku.txt", "a") as file:
#     file.write("\nHere's one more haiku\n")
#     file.write("What about the older one?\n")
#     file.write("Let's go check it out")

# with open("haiku.txt", "a") as file:
#     file.write("\nAPPENDING LATER!!!!!")

# so things are not added to the end of old lines, add \n to end of new sentence:
# with open("haiku.txt", "a") as file:
#     file.write("APPENDING LATER!!!!!\n")

# now things will start on a new line
# with open("haiku.txt", "a") as file:
#     file.write(":)\n")

# to add something to the top, we think we can use seek() and it appends to the top, but because it's append mode, it just adds to the end:
# with open("haiku.txt", "a") as file:
#     file.seek(0)  #<-- doing this does not append it to the beginning of the file
#     file.write(":)\n")

# using "r+" (below starts the cursor at 0, and overwrote the file):
# with open("haiku.txt", "r+") as file:
#     file.write("ADDED USING r+")

# file changed manually to one sentence in file that said "I was here first!"
# with open("haiku.txt", "r+") as file:
#     file.write(":)")  #<-- overwrites the "I" at 0th place
#     file.seek(10)
#     file.write(":(")  #<-- overwrites the "f" at 10 place
#_____________________________________________________________

# Practice Example 1.
# copy
# Write a function called copy, which takes in a file name and a new file name and copies the contents of the first file to the second file. 
# (Note: we've provided you with the first chapter of Alice's Adventures in Wonderland to give you some sample text to work with. This is also the text used in the tests.
# copy('story.txt', 'story_copy.txt') # None
# # expect the contents of story.txt and story_copy.txt to be the same
def copy(file1, file2):
    with open(file1) as first_file:
        first_story = first_file.read()
        
    with open(file2, "w") as second_file:
        second_file.write(first_story)

# copy("alice_story.txt", "alice_story_copy.txt")
#_____________________________________________________________

# Practice Example 2.
# copy_and_reverse
# Write a function called copy_and_reverse, which takes in a file name and a new file name and copies the reversed contents of the first file to the second file.
# (Note: we've provided you with the first chapter of Alice's Adventures in Wonderland to give you some sample text to work with. This is also the text used in the tests.)
def copy_and_reverse(file1, file2):
    with open(file1) as first_file:
        first_story = first_file.read()
        
    with open(file2, "w") as second_file:
        second_file.write(first_story[::-1])

# copy_and_reverse("alice_story.txt", "alice_story_reversed.txt")
#_____________________________________________________________

# Practice Exercise 3.
# statistics
# Write a function called statistics, which takes in a file name and returns a dictionary with the number of lines, words, and characters in the file.
# (Note: we've provided you with the first chapter of Alice's Adventures in Wonderland to give you some sample text to work with. This is also the text used in the tests.)
# instructors code:
def statistics(file_name):
    with open(file_name) as file:
        # returs a list with each line as an element
        lines = file.readlines()
    return {
        # returns length of lines list
        "lines": len(lines),
        # for every line in lines, split the line, determine length, then sum it
        "words": sum(len(line.split(" ")) for line in lines),
        # for every line in lines, determine length of line, and sum it
        "characters": sum(len(line) for line in lines)
    }

# print(statistics("alice_story.txt"))  #//=>  {'lines': 172, 'words': 2145, 'characters': 11227}
#_____________________________________________________________

# Practice Exercise 4.
# find_and_replace
# Write a function called find_and_replace, which takes in a file name, a word to search for, and a replacement word. Replaces all instances of the word in the file with the replacement word.
# (Note: we've provided you with the first chapter of Alice's Adventures in Wonderland to give you some sample text to work with. This is also the text used in the tests.)
# instructors code:
def find_and_replace(file_name, old_word, new_word):
    # use "r+" to read and write a file (things will be overwritten)
    with open(file_name, "r+") as file:
        text = file.read()
        # create new text and use replace(old_item, new_item) method
        new_text = text.replace(old_word, new_word)
        # start cursor at 0th place in text
        file.seek(0)
        # write the newt text
        file.write(new_text)
        # this resizes the file to the given number of bytes, if no size is specified than the current position will be used
        file.truncate()

