import os

from better_profanity import profanity
profanity.load_censor_words()

# profanity filter is on by default
filtering = True

# whitelisted words; loaded from file. Will be loaded directly into profanity.
whitelist = []
# newly added words. Will be loaded directly into profanity.
newwhitelist = []
# commands
command_list = [] # needs to be separate so that it's possible to slice later. See saveCurrentWL

# list of words to censor; loaded from file
censorlist = []
# list of new words to censor
newcensorlist = []


# loads commands into the whitelist as a precaution.
def loadCommandWhitelist():
    profanity.load_censor_words(whitelist_words=whitelist)

# loads default whitelist. Includes commands. TODO
def loadDefaultWhitelist():

    #wl_set = set(whitelist)

    with open('default_whitelist.txt', 'r', encoding='UTF-8') as file:
        for line in file:
            thing = line.rstrip()
            whitelist.append(thing)
            #wl_set.add(thing)

    profanity.load_censor_words(whitelist_words=whitelist)




# loads saved whitelist. TODO
#def loadSavedWhitelist():
#    profanity.load_censor_words(whitelist_words=command_list)

        #file1 = open("profanity_files/whitelist.txt","a")
        #File_object.readlines()
        #file1.write("Today \n")
        #file1.close()

        # for each word in words:
        #   read and strip newline
        # if in array: skip, else: add to array

        # pass array to profanity whitelist?

# saves the current whitelist to the existing list (excluding commands): TODO
#def saveCurrentWhitelist():
    #ex = len(command_list)
    #saveList = whitelist[ex:] # remove commands...
    # convert to set to prevent duplicates...
    # return? save it?

# clears the current whitelist but leaves the saved list untouched (excluding commands): TODO
#def clearCurrentWhitelist():
    # ex = len(command_list)
    # saveList = whitelist[ex:]
    # convert to set to prevent duplicates...
    # return? save it?
    # how to handle newly added words if the user decides to load saved words?

# to prevent duplication, reconstruct the list...
#def loadSavedWL():
#    profanity.load_censor_words(whitelist_words=command_list)


#TODO
#def censorWord(word):
#    if word.startswith("$"):
#        pass
        #cannot censor a command

    # if all white space: do nothing
    # cannot censor words < 2 chars
    # if word is on command list: cannot censor command.
    # if word is on whitelist: remove from list and add to censor

# load saved words into an array from a file
#def loadSavedBadWords():
#    pass
