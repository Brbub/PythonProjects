from PIL import Image
import random



image = "Images/trump.jpg"


def create_image(i, j):
  image = Image.new("RGB", (i, j), "white")
  return image



def openImage (image):
    im = Image.open(image)
    return list(im.getdata())



OldImage = openImage(image)


NewImage = create_image(300, 168)



OldImage.sort()
for i in OldImage:
    i = list(i).sort()



NewImage.putdata(OldImage)



NewImage.save("NewTrump.jpg")


#def ColorSort(L): 
  #hexList = []
  #for i in L:
  #  hexList.append(hexConverter(i))
 # return(hexToInts(mergeSort(hexList))