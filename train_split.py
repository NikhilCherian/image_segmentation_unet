import os, os.path, shutil, glob
folder1="jpg"
for i in range(2,17):
    folder_path=os.path.join(folder1, str(i))
#folder_path = "jpg/0"
#new_path="jpg/train"
    images = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    for f in images:
        image_name= f.split('.')[0]
        image2=image_name.split('_')[1]
        print(image2)
        b=int(image2)
       # c= 
        if b<= (80*i+60):
            old_image_path = os.path.join(folder_path, f.rstrip("\n"))
            image3 = os.path.join("jpg/train", str(i))
            new_image_path = os.path.join(image3, f.rstrip("\n"))
            print(new_image_path)
            shutil.move(old_image_path, new_image_path)
        else:
            old_image_path = os.path.join(folder_path, f.rstrip("\n"))
            image3 = os.path.join("jpg/valid", str(i))
            new_image_path = os.path.join(image3, f.rstrip("\n"))
            shutil.move(old_image_path, new_image_path)
 
#old_image_path = os.path.join(folder_path, line.rstrip("\n"))
#new_image_path = os.path.join(new_path, line.rstrip("\n"))
#shutil.move(old_image_path, new_image_path)


