import cv2
import glob
import matplotlib.pyplot as plt
import  numpy as np
from PIL import Image
from colorthief import ColorThief
import statistics

img_data = []
files = glob.glob("C:\images\cats_with_different_bg\*.JPG")
for myFile in files:
    print(myFile)
    image = cv2.imread(myFile)
    img_data.append(image)
    print("Image shape: ", image.shape)
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.show()
    print(np.array(img))


img_dc = []
files = glob.glob("C:\images\cats_with_different_bg\*.JPG")
for myFile in files:
    print(myFile)
    color_thief = ColorThief(myFile)
    dominant_color = color_thief.get_color(quality=1)
    img_dc.append(statistics.mean(dominant_color))
    print(img_dc)



from collections import defaultdict
res_dict = defaultdict(list) # defaultdict is created with the values that are 'list'
for Key, Value in zip(img_dc,img_data): # zip(a,b) pairs elements in a with elements in b
      res_dict[Key].append(Value) # Adding key and values into our created dictionary

print(dict(res_dict))

def remove(duplicate):
    final = []
    for num in duplicate:
        if num not in final:
            final.append(num)
    return final
final_dc = remove(img_dc)
print("Image dominant colors after removing duplicates:\n", final_dc)
key = list(res_dict.keys())
val = list(res_dict.values())

print("Printing keys: ", key)
print("Printing values: ", val)

print("Images after sorting:\n\n")

def partition(arr, low, high):
    i = (low-1)          # index of smaller element
    pivot = arr[high]    # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:

            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
    return (i+1)
def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:

        # pi is partitioning index, arr[p] is now at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
n = len(final_dc)
quickSort(final_dc, 0, n-1)
print("Sorted dominant color of images is:")
for i in range(n):
    print("%d",final_dc[i])


for j in range(len(final_dc)):
    #print("j iteration: ", j)
    for k in range(len(key)):
        #print("k iteration: ", k)
        if final_dc[j] == key[k]:
            print("Image size: ", final_dc[j])
            print("Size matched")
            for item in val[k]:
                Img = cv2.cvtColor(item, cv2.COLOR_BGR2RGB)
                plt.imshow(Img)
                plt.show()            

    
