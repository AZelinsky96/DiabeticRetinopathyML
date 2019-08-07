import os
import pandas as pd
import random
import shutil


classes_to_oversample = ["Moderate", "Mild", "Severe", 'Proliferative_Diabetic_Retinopathy']
classes_to_downsample = ['No_Diabetic_Retinopathy']
def sampling(sampler, goal = 1000):
    base = os.getcwd()
    print(base)
    if os.path.isdir("Balanced") == False:
        os.mkdir(base + "/Balanced")
        os.chdir("Balanced")
        classes = ["Moderate", "Mild", "Severe", 'Proliferative_Diabetic_Retinopathy','No_Diabetic_Retinopathy']
        for i in classes:
            if os.path.isdir(base + "/Balanced/{}".format(i)) == False:
                os.mkdir(i)
    os.chdir(base)
    destin_dir = base + "/Balanced"




    for i in sampler:
        print("Sampling: {}".format(i))
        os.chdir(i)
        for p in range(goal):
            #print(os.listdir()[random.randint(0,len(os.listdir()) -1 )])
            file = os.listdir()[random.randint(0,len(os.listdir()) -1 )]
            extension = file[file.find("."):]
            shutil.copy(file, destin_dir + "/{}".format(i))
            os.rename(destin_dir + "/{}/{}".format(i,file), destin_dir + "/{}/Image{}{}".format(i,p,extension) )
        os.chdir(base)
        print("Completed: {}".format(i))



#sampling(classes_to_oversample)
sampling(["Mild"], 1500)
sampling(["Proliferative_Diabetic_Retinopathy"], 1500)
sampling(["Severe"], 1500)
sampling(["Moderate"], 1500)


