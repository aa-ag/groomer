############------------ IMPORTS ------------############
import os


############------------ GLOBAL VARIABLES ------------############

############------------ FUNCTIONS ------------############
def rename_files():
    '''
     reads files in a directory, and
     renames them.
    '''
    # testing os.listdir() function
    for image in os.listdir('images'):
        print(image)


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    rename_files()
