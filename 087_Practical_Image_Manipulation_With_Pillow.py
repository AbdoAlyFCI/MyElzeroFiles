# -------------------------------------------------
# -- Practical => Image Manipulation With Pillow --
# -------------------------------------------------

from PIL import Image

# Open The Image
myImage = Image.open("tg.jpg")

# Show The Image
myImage.show()

# My Cropped Image
myBox = (300,300,800,800)
myNewImage = myImage.crop(myBox)

# Show The New Image
myNewImage.show()

# My Converted Mode Image
myConverted = myImage.convert("L")
myConverted.show()