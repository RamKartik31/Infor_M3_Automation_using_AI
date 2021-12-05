from PIL import Image, ImageFilter


# Opening the image (R prefixed to string
# in order to deal with '\' in paths)
image = Image.open(r"72Pages.jpeg")

# Converting the image to greyscale, as edge detection
# requires input image to be of mode = Greyscale (L)
image = image.convert("L")

# Detecting Edges on the Image using the argument ImageFilter.FIND_EDGES
image = image.filter(ImageFilter.FIND_EDGES)

# Saving the Image Under the name Edge_Sample.png
image.save(r"72Pages_Edge.jpeg")
