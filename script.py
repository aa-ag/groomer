############------------ IMPORTS ------------############
import os
from PIL import Image


############------------ GLOBAL VARIABLES ------------############
test_brands = ['brand_a', 'brand_b', 'brand_c', 'brand_d', 'brand_e',
               'brand_f', 'brand_g', 'brand_h', 'brand_i']


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
        file_extension = image_name.split('.')[1]
        new_name = f"{brand}_header.{file_extension}"
        os.rename(os.path.join(source_path, image_name),
                  os.path.join(destination_path, new_name))

    # use enumerate to add count/n to new title
    # for i, image_name in enumerate(images):
    #     file_extension = image_name.split('.')[1]
    #     new_name = f"{i}_header.{file_extension}"
    #     os.rename(os.path.join(source_path, image_name),
    #               os.path.join(destination_path, new_name))


def resize_images():
    '''
     uses functions from PIL to 
     manipulate image opened
    '''
    # logic to open one image,
    # set size expected, and resize and show
    # resized image

    # test_image_path = 'images/brand_a_header.jpeg'
    # test_image = Image.open(test_image_path)
    # (width, height) = (300, 250)
    # resized_image = test_image.resize((width, height))
    # resized_image.save('resized.jpg', 'JPEG', quality=90)

    # set source and destination of images
    # where to go get the images from/put them in
    # source_path = '<PATH WHERE IMAGES ARE>'

    source_path = '/Users/aaronaguerrevere/Documents/portfolio/groomer/images/'
    destination_path = '/Users/aaronaguerrevere/Documents/portfolio/groomer/resized_images/'

    for i, image in enumerate(os.listdir('images')):
        one_image = Image.open(source_path + image)
        (width, height) = (300, 250)
        resized_image = one_image.resize((width, height))
        resized_image.save(
            f'{destination_path}/{i+1}_resized.jpg', 'JPEG', quality=90)


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    # rename_files()
    resize_images()
