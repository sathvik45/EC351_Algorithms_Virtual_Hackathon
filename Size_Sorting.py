#!/usr/bin/env python
# coding: utf-8

# # Algorithm Project - EC351
# 
# ***
# 
# ## To do tasks: 
# 
# * **Write an Algorithm to SORT the image array using any suitable Sorting algorithms**
# 
# * **Sort them in an Ascending Order of their Size**
# 
# * **Given a new unknown image, search the new image in the array and display the result as found or not along with the image.**
# 
# * **Write a Program and find out the Time complexity for Searching and Sorting algorithm implementation of selected IMAGE Arrays**
# 
# * **No HARD code is allowed in the Program**
# 
# ***

# 
# # Implementation:
# 
# ***
# ***
# 
# # Sequence of steps followed for implementation:
# ***
# ![Untitled%20Diagram%20%281%29.png](attachment:Untitled%20Diagram%20%281%29.png)
# 
# 

# # Program
# ***
# ## Step:1 - Storing images into an array

# In[ ]:


get_ipython().run_cell_magic('time', '', 'import cv2\nimport glob\nimport matplotlib.pyplot as plt\nimport  numpy as np\n\n# Creating an empty list for storing images\nimg_data = []\n\n#Providing path of the image folder\nfiles = glob.glob("D:\\Pictures\\cats\\*.JPG")\n\nfor myFile in files:\n    print(myFile)\n    image = cv2.imread(myFile)                   # Here imread is used to load an image from provided path\n    img_data.append(image)                       # Appends image to the list\n    print("Image shape: ", image.shape)          # shape command gives the dimensions of the image [(height,width,color(3))]\n    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # In Opencv, by default image is displayed in BGR format,hence changing it to RGB format\n    plt.imshow(img)                              # For plotting image\n    plt.show()                                \n    #print(np.array(img))\n    ')


# ## Step:2 - Storing image sizes into another array

# In[ ]:


get_ipython().run_cell_magic('time', '', 'from PIL import Image\n\n# Declaring an empty list to store image sizes\nimg_size = []\n\nfiles = glob.glob("D:\\Pictures\\cats\\*.JPG")\nfor myFile in files:\n    im = Image.open(myFile)                 #path to image file\n    width, height = im.size                 #Storing width and height of each image into variables called \'width\',\'height\' \n    resolution = width*height               #Calculating resolution for each image\n    img_size.append(resolution)             #Adding resolution values into our created list\n    \nprint(img_size)')


# ## Step:3 - Creating a dictionary with image sizes and image arrays

# In[ ]:


get_ipython().run_cell_magic('time', '', "#Creating a dictionary which takes multiple values for same key and stores in a list corresponding to that key\n\nfrom collections import defaultdict\n\nres_dict = defaultdict(list)                  # defaultdict is created with the values that are 'list'\nfor Key, Value in zip(img_size,img_data):     # zip(a,b) pairs elements in a with elements in b\n    res_dict[Key].append(Value)               # Adding key and values into our created dictionary\n    \nprint(dict(res_dict))")


# ## Step:4 - Sorting image sizes using Quick sort

# In[ ]:


get_ipython().run_cell_magic('time', '', 'def partition(arr, low, high):\n    i = (low-1)          # index of smaller element\n    pivot = arr[high]    # pivot as last element\n\n    for j in range(low, high):\n\n        # If current element is smaller than or equal to pivot\n        if arr[j] <= pivot:\n\n            # increment index of smaller element\n            i = i+1\n            arr[i], arr[j] = arr[j], arr[i]\n\n    arr[i+1], arr[high] = arr[high], arr[i+1]\n    return (i+1)\n\n\n# The main function that implements QuickSort\n# arr[] --> Array to be sorted,\n# low --> Starting index,\n# high --> Ending index\n\ndef quickSort(arr, low, high):\n    if len(arr) == 1:\n        return arr\n    if low < high:\n\n        # pi is partitioning index, arr[p] is now at right place\n        pi = partition(arr, low, high)\n\n        # Separately sort elements before partition and after partition\n        quickSort(arr, low, pi-1)\n        quickSort(arr, pi+1, high)\n\n        \n#Main code to sort image sizes\nn = len(img_size)\nquickSort(img_size, 0, n-1)\nprint("Sorted size of images is:")\nfor i in range(n):\n    print("%d" % img_size[i]),')


# ## Step:5 - Remove duplicate elements from image sizes array

# In[ ]:


get_ipython().run_cell_magic('time', '', '#Remove duplicate sizes from image sizes\ndef remove(duplicate):\n    final = []                       # Creating an empty list to store final result\n    for size in duplicate:           # Loop for iterating through sizes and stores only unique elements\n        if size not in final:\n            final.append(size)\n    return final\n\n\nfinal_size = remove(img_size)\nprint("Image sizes after removing duplicates:\\n", final_size)')


# ## Step:6 - Compare sorted array of image sizes with the keys in dictionary and display images in                    sorted fashion

# In[ ]:


get_ipython().run_cell_magic('time', '', '# Sorting images and displaying\n\n#Seperating keys and values from our created dictionary\nkey = list(res_dict.keys())\nval = list(res_dict.values())\n\n#print("Printing keys: ", key)\n#print("Printing values: ", val)\n\nprint("Images after sorting:\\n\\n")\nfor j in range(len(final_size)):                           \n    for k in range(len(key)):\n        if final_size[j] == key[k]:              # If the size in \'j\' location in the sorted size array is matched with a key in \'k\'th position\n            print("Image size: ", final_size[j]) \n            print("Size matched")\n            for item in val[k]:                  # Retrieve the list of images from the values stored in that matched key size\n                Img = cv2.cvtColor(item, cv2.COLOR_BGR2RGB)\n                plt.imshow(Img)\n                plt.show()            ')


# # Searching an image : 
# ***
# ## Flowchart:
# 
# ![Untitled%20Diagram%20%283%29.png](attachment:Untitled%20Diagram%20%283%29.png)

# In[ ]:


get_ipython().run_cell_magic('time', '', 'import matplotlib.pyplot as plt \nimport glob\nimport cv2\n\nnew_image = cv2.imread(\'Pictures/image3.jpg\')    #Loads new image to be searched\nprint("Image to be seached is below:")\nprint("Dimensions of image: ", new_image.shape)\nimg = cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB) #Converts the image to be searched from BGR to RGB\nplt.imshow(img)                                  #Plots the image\nplt.show()\n\n\n# Declaring a variable flag to break from the loop if the searched item is found\nflag = 0\nprint("Searching started:\\n")\nfiles = glob.glob("D:\\Pictures\\cats\\*.JPG")\nfor myFile in files:\n    search = cv2.imread(myFile) \n    if search.shape == new_image.shape:                     #Checking if dimensions are same\n        print("\\nMatching dimensions found at: ", myFile)\n        print("Images have same shape...")\n        print("Let\'s check if they have same pixel values")\n        difference = cv2.subtract(search, new_image)        # Makes subtraction for each color(Red,Green,Blue) channel\n        b, g, r = cv2.split(difference)                     # Splitting colors from the subtracted image  \n        # Check if all the colors are black i.e..(0 - black ..... 255 - white)\n        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:     \n            flag = 1\n            print("\\nYES! The images are completely EQUAL")\n            found = cv2.cvtColor(search, cv2.COLOR_BGR2RGB)\n            plt.imshow(found)\n            plt.show()\n        else:\n            print("Pixel values are not same!\\n")\n    # If the searching image is found \n    elif flag == 1:\n        break\n    else:\n        print("Image not found at: ", myFile)\n')


# # Time Complexity analysis:
# ***
# ![Untitled%20Diagram%20%284%29.png](attachment:Untitled%20Diagram%20%284%29.png)

# # List of references:
# ***
# 1. <a href="https://www.geeksforgeeks.org/defaultdict-in-python/" target="_blank">https://www.geeksforgeeks.org/defaultdict-in-python/</a>
# 2. <a href="https://www.pluralsight.com/guides/importing-image-data-into-numpy-arrays" target="_blank">https://www.pluralsight.com/guides/importing-image-data-into-numpy-arrays</a>
# 3. <a href="https://www.kite.com/python/answers/how-to-convert-a-numpy-array-to-an-image-in-python" target="_blank">https://www.kite.com/python/answers/how-to-convert-a-numpy-array-to-an-image-in-python</a>
# 4. <a href="https://www.geeksforgeeks.org/how-to-use-glob-function-to-find-files-recursively-in-python/" target="_blank">https://www.geeksforgeeks.org/how-to-use-glob-function-to-find-files-recursively-in-python/</a>
# 5. <a href="https://pysource.com/2018/07/19/check-if-two-images-are-equal-with-opencv-and-python/" target="_blank">https://pysource.com/2018/07/19/check-if-two-images-are-equal-with-opencv-and-python/</a>
