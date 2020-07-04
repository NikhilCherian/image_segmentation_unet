import os, os.path, shutil

folder_path = "jpg"

images = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
filename= "jpg/files.txt"
myimages=[]

with open(filename) as f:
    for line in f:
        #count=count+1
        image_name= line.split('.')[0]
        image2=image_name.split('_')[1]
        print(image2)
        b=int(image2)/80
        a=int(b)
        new_path = os.path.join(folder_path, str(a))
        if not os.path.exists(new_path):
            os.makedirs(new_path)
        old_image_path = os.path.join(folder_path, line.rstrip("\n"))
        new_image_path = os.path.join(new_path, line.rstrip("\n"))
        shutil.move(old_image_path, new_image_path)
#        myimages.append()

#print(count)

#for image in images:
 #   print(image)
  #  image_name= image.split('.')[0]
 #   folder2= image_name.split('_')[1]
   # print(folder2)
