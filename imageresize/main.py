from PIL import Image
import os
import glob


def main():

  image_path = '/Users/ryanc/Pictures/cave.jpg'

  im = Image.open(image_path)
  print("{}".format(im.format))
  print('size: {}'.format(im.size))
  print('image mode: {}'.format(im.mode))
  # im.show()

  # empty lists
  image_list = [] 
  resized_image_list = []

  # append iamges to list
  for filename in glob.glob('/Users/ryanc/Pictures/*.jpg'):
    print(filename)
    img = Image.open(filename)
    image_list.append(img)
  image_list = image_list[:10]

  # append resized images to list
  for image in image_list:
    # image.show()
    image = image.resize((500,300))
    resized_image_list.append(image)

  # save resized images to a new folder
  # could also use os module to create a new folder
  # first curly: put the path and new image name prefix
  # second curly: add a number to that image name. ex, shape1, shape2, shape3, etc.
  # third curly: .png for the image type
  for (i, new) in enumerate(resized_image_list):
    new.save('{}{}{}'.format('/Users/ryanc/Pictures/Resized_folder/hello', i+i,'.jpg'))

if __name__ == '__main__':
  main()
  