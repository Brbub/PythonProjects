from PIL import Image
import random



image = "Images/dog.jpg"
def openImage (image):
    im = Image.open(image)
    return im
OldImage = openImage(image)
def create_image(i, j):
  image = Image.new("RGB", (i, j), "white")
  return image

def get_pixel(image, i, j):
    # Inside image bounds?
    width, height = image.size
    if i > width or j > height:
      return None

    # Get Pixel
    pixel = image.getpixel((i, j))
    return pixel


newImage = create_image(OldImage.size[0], OldImage.size[1])


OldImagePixelValues = []

print(OldImage)
print(newImage)
for i in range(OldImage.size[0]):
    for j in range(OldImage.size[1]):
        pixel = get_pixel(OldImage, i, j)
        OldImagePixelValues.append(pixel)
        

#for i in emptyList:

def hexConverter(c):
  return((c[0] << 16) + (c[1] << 8) + c[2])
def hexToInts(x):
  return( c >> 16, (c >> 8) & 0xff, c & 0xff)


def mergeSort(values):
    if len(values) <= 1:
        return values
    mid = len(values) // 2
    left = mergeSort(values[:mid])
    right = mergeSort(values[mid:])
    sort = []
    LIndex = 0
    RIndex = 0
    while LIndex < len(left) and RIndex < len(right):
        if left[LIndex] < right[RIndex]:
            sort.append(left[LIndex])
            LIndex += 1
        else:
            sort.append(right[RIndex])
            RIndex += 1
    sort += left[LIndex:]
    sort += right[RIndex:]
    return sort



#L = [[255,255,233],[233,155, 712]]
def ColorSort(L): 
  hexList = []
  for i in L:
    hexList.append(hexConverter(i))
  return(hexToInts(mergeSort(hexList))

ColorSort(OldImagePixelValues)


newImage = NewOldPixelValues

newImage.save()









