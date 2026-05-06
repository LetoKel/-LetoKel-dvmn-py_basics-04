from PIL import Image

image = Image.open("monro.jpg")

# print ("Ширина —", image.width)
# print ("Длина —", image.height)
# print ("Цветовая модель —", image.mode)

# rgb_image = image.convert("RGB")
# print(rgb_image.mode)
# print(image.mode)

red, green, blue = image.split()

coordinates_red_crop_1 = (50, 0, image.width, image.height)
coordinates_red_crop_2 = (25, 0, (image.width - 25), image.height)
coordinates_blue_crop_1 = (0, 0, (image.width - 50), image.height)
coordinates_blue_crop_2 = (25, 0, (image.width - 25), image.height)
coordinates_green_crop = (25, 0, (image.width - 25), image.height)


red_cropped_left = red.crop(coordinates_red_crop_1)
red_cropped_middle = red.crop(coordinates_red_crop_2)
red_blended = Image.blend(red_cropped_left, red_cropped_middle, 0.5)

blue_cropped_left = blue.crop(coordinates_blue_crop_1)
blue_cropped_middle = blue.crop(coordinates_blue_crop_2)
blue_blended = Image.blend(blue_cropped_left, blue_cropped_middle, 0.5)

green_cropped = green.crop(coordinates_green_crop)

result_image = Image.merge("RGB", (red_blended, blue_blended, green_cropped))
result_image.thumbnail((80, 80)) 
result_image.save("result_image.jpg")