
import pandas as pd
import os
import re
import shutil

class Allocator:
    directory = "/home/zeski/Documents/PythonLessons/MachineLearning/Projects/DiabeticRetinopathy"
    def __init__(self, file):
        self.file = file

    def file_locator(self):
        """
        This method will walk through the project Folder titled DiabeticRetinopathy. From there
        it will locate and create a file path to the file name passed into the constructor upon instantiation.
        """

        file_ = self.file
        locations = []
        print("Searching for {}".format(file_))
        for root, dirs, files in os.walk(Allocator.directory):
            for name in files:
                if name == file_:
                    file_loc = os.path.join(root,name)
                    locations.append(file_loc)

        file_location = min(locations)
        self.file_location = file_location
        print("Found {}.\n".format(file_))
        while True:
            correct_location_input = input("Location: {}\nIs Location Correct? [y/n]".format(file_location))

            if correct_location_input.lower() == "y":
                break
            elif correct_location_input.lower() == "n":
                print("Index: \t---\tLocation:")
                [print(str(i) + "\t---\t" + str(k)) for i,k in enumerate(locations)]
                index_ = input("Please Input the index for correct file location from collection above.")
                while True:
                    try:
                        index_ = int(index_)
                        break
                    except:
                        index_ = input("Enter Integer Value for index: ")
                self.file_location = locations[int(index_)]
                print("\n")
            else:
                print("Please enter either [y/n]")


    def open_file(self, ignore_class_map = False):
        ## Creating a class map with the descriptions of the categories to update the metadata
        class_map = {
        0 : "No_Diabetic_Retinopathy",
        1 : "Mild",
        2 : "Moderate",
        3 : "Severe",
        4 : "Proliferative_Diabetic_Retinopathy"
        }
        ## Creating my metadata
        self.df = pd.read_csv(self.file_location)
        self.df["Diagnosis_Description"] = self.df["diagnosis"].copy()
        self.df["Diagnosis_Description"] = self.df["Diagnosis_Description"].apply(lambda x: class_map[x])
        self.df.to_csv("{}_with_description.csv".format(self.file.split(".")[0]), index = False, encoding = "utf-8")


    def image_allocation(self, folder):

        ## Changing directory to location of stored images
        os.chdir(folder)
        ## Creating the folders to house each image belonging to a category.

        for i in self.df["Diagnosis_Description"].unique():
            if i not in os.listdir():
                os.mkdir(i)
        counter = 0
        for i,k in enumerate(self.df["id_code"]):
            if counter % 100 == 0:
                print(counter)
                #print(k, self.df.iloc[i, -1])
            for image in os.listdir():
                    #print(image)
                if re.match("{}.+".format(k), image):
                    image_file =  re.match("{}.+".format(k), image)

                    #print(image_file.group(), self.df.iloc[i, -1])
                    shutil.copy(image_file.group(), self.df.iloc[i, -1])
            counter += 1
        os.chdir("..")
        print("{} Data Allocated\n".format(self.file.split(".")[0]))
def main():
    ## Performing operations on the training data
    train_allocator = Allocator("train.csv")
    train_allocator.file_locator()
    train_allocator.open_file()
    train_allocator.image_allocation("train_images")



if __name__ == "__main__":
    main()
