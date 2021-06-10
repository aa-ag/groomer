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
    for i, image in enumerate(os.listdir('images')):
        file_name, file_extension = os.path.splitext(image)
        print(i, file_name, file_extension)


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    rename_files()
