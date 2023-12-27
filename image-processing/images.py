from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
filtered_image = img.filter(ImageFilter.BLUR)
converted_image = img.convert('L')
converted_image.save('convert.png', 'png')
filtered_image.save('blur.png', 'png')
