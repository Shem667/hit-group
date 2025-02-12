from PIL import Image

#For Loading the original image
original_image_path = 'C:/Users/Admin/Documents/GitHub/hit-group/chapter1.jpg'
original_image = Image.open('C:/Users/Admin/Documents/GitHub/hit-group/chapter1.jpg')

# To Get the dimensions of the image
width, height = original_image.size

# For Generate the number as per the given algorithm
import time
current_time = int(time.time())
generated_number = (current_time % 100) + 50 
if generated_number % 2 == 0:
    generated_number += 10

#  For Creating a new image with modified pixels
new_image = Image.new('RGB', (width, height))
for y in range(height):
    for x in range(width):
        # To Get the original pixel values
        original_pixel = original_image.getpixel((x, y))

        # To Modify the pixel values
        modified_pixel = tuple([val + generated_number for val in original_pixel])

        # To Set the modified pixel in the new image
        new_image.putpixel((x, y), modified_pixel)

# Save the new image
new_image_path = 'chapter1out.png'
new_image.save(new_image_path)

# For Calculate the sum of red pixel values in the new image
red_sum = sum(pixel[0] for pixel in new_image.getdata())

# For Print the sum to move to the next chapter
print("Sum of red pixel values:", red_sum)
