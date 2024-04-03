from PIL import Image

size = (100000, 100000)
saved = "/home/faxriddin/Pictures/Webcam/jsC0Hi16281644277129_o.jpg"
img = Image.open("/home/faxriddin/Pictures/Webcam/jsC0Hi16281644277129_o.jpg")
img.thumbnail(size)
# img.save(saved)
img.show()