############------------ IMPORTS ------------############
import os
import PIL


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
    test_image = '/Users/aaronaguerrevere/Documents/portfolio/dadjokes/project/static/media/thomas-jensen-h3vT1Kp0FxA-unsplash.jpg'


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    # rename_files()
    resize_images()
