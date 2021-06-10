############------------ IMPORTS ------------############
import os


############------------ GLOBAL VARIABLES ------------############
test_brands = ['i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix']


############------------ FUNCTIONS ------------############
def rename_files():
    '''
     reads files in a directory, and
     renames them.
    '''
    # import test_brands list
    global test_brands

    # set source and destination of images
    # where to go get the images from/put them in
    source_path = 'images'
    destination_path = 'images'

    # create a list of images to iterate over
    images = os.listdir('images')

    # zip images & brands to combine the two
    # in creating new file names
    for brand, image_name in zip(test_brands, images):
        print(brand, image_name)

    # use enumerate to add count/n to new title
    # for i, image_name in enumerate(images):
    #     existing_name, file_extension = image_name.split('.')
    #     new_name = f"{i}_header.png"
    #     os.rename(os.path.join(source_path, image_name),
    #               os.path.join(destination_path, new_name))


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    rename_files()
