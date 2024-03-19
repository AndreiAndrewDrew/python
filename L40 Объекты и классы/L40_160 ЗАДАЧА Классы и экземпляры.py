class Image:
    def __init__(self, init_resolution, init_title, init_extension):
        self.resolution = init_resolution
        self.title = init_title
        self.extension = init_extension

    def resize(self, new_resolution):
        self.resolution = new_resolution

    def title_upper(self,new_title):
        self.title = new_title.upper()


image1 = Image('1920x1080', 'Image_1', '.jpg')
image2 = Image('1280x720', 'Image_2', '.png')
image3 = Image('640x480', 'Image_3', '.gif')

print(image1.__dict__)
print("Toate imaginile:")
print(image1.title, image1.extension, image1.resolution)
print(image2.title, image2.extension, image2.resolution)
print(image3.title, image3.extension, image3.resolution)

image1.resize('1024x786')
print("Imaginea 1 dupa 'resize':")
print(image1.title, image1.extension, image1.resolution)

image1.title_upper(image1.title)
print("Imaginea 1 dupa 'tiitle_upper':")
print(image1.title, image1.extension, image1.resolution)

image3.title_upper(image3.title)

print("Toate imaginile:")
print(image1.title, image1.extension, image1.resolution)
print(image2.title, image2.extension, image2.resolution)
print(image3.title, image3.extension, image3.resolution)


