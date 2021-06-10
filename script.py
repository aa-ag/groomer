############------------ IMPORTS ------------############
import os


############------------ GLOBAL VARIABLES ------------############

############------------ FUNCTIONS ------------############
def rename_files():
    '''
     reads files in a directory, and
     renames them.
    '''
    # set source and destination of images
    # where to go get the images from/put them in
    source_path = 'images'
    destination_path = 'images'

    # create a list of images to iterate over
    images = os.listdir('images')

    # use enumerate to add count/n to new title
    for i, image in enumerate(images):
        existing_name, file_extension = image.split('.')
        new_name = f"test_{i}.{file_extension}"
        os.rename(os.path.join(source_path, image),
                  os.path.join(destination_path, new_name))


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    rename_files()
