import os
import shutil
import random

base = "/home/zeski/Documents/PythonLessons/MachineLearning/Projects/DiabeticRetinopathy/ProjectData/Binary"

def train_test_split(test_size = 0.1):
    ## This is the list that the files are in for the directory
    directories  = ["No_Diabetic_Retinopathy", "Diabetic_Retinopathy"]

    ## Looping through the directories of the collected train images to split into train and test images
    for i in directories:
        os.chdir(i)

        ## Chaning dir above

        ## Finding the amount of images to pull and move to testing data
        test_nums = round(len(os.listdir()) * test_size)

        ## Instantiating a set to collect indexes, these will be the indexes for the test images
        random_selection = set()
        ## Looping over amount of test numbers per dir to generate random integers within the bound of the total
        ## Amount of files in the folder. These integers will be used as indexes to move the images to testing folders

        for k in range(test_nums):
            random_selection.add(random.randint(0,len(os.listdir()) -1 ))

        ## The directory set is a set of integers for each and every file in directory i for i in list directories
        directory_set = set(range(len(os.listdir())))

        ## The train_indexes will be the indexes for the training images
        train_image_indexes = directory_set - random_selection

        ## Finding the actual files per index
        test_images  = [os.listdir()[k] for k in random_selection]
        train_images =[os.listdir()[k] for k in train_image_indexes]

        ## Moving the test image selections


        os.chdir(base)
        ## Creating my paths
        total_path = base +"/{}/".format(i)
        destination_path_test = base + "/Train/{}/".format(i)
        destination_path_train = base + "/Test/{}/".format(i)

        print("Moving Test Images: {}".format(i))
        for img in test_images:
            if img not in train_images:
                shutil.copy(total_path+"{}".format(img), destination_path_test)
            else:
                print("ERROR THERE IS AN OVERLAP IN IMAGES!!")


        print("Moving Train Images: {}".format(i))
        for img in train_images:
            if img not in test_images:
                shutil.copy(total_path+"{}".format(img), destination_path_train)
            else:
                print("ERROR THERE IS AN OVERLAP IN IMAGES!!")
        print(i, "Complete\n")


    return None


def main():
    train_test_split(0.1)

main()
