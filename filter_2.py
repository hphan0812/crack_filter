import os
import cv2

ref_path = '/media/HDD0/hanhphan/20240906'
list_subfolder = []

list_subfolder = [f"{ref_path}/{subfolder}" for subfolder in os.listdir(ref_path)]

list_subsubfolder =  []
for subfolder in list_subfolder:
    for subsubfolder in os.listdir(subfolder):
        if "DS_Store" not in subsubfolder:
            list_subsubfolder.append(f"{subfolder}/{subsubfolder}")

profile_path = "/media/HDD0/hanhphan/model_v3_5_3_test_profile"

profile_subfolder = ""

# Code link thư mục giữa thư mục ref và profile
for subsubfolder in list_subsubfolder:
    # Tách subsubfolder thành các thành phần nhỏ thông qua dấu "/"
    subsubfolder_split = subsubfolder.split("/")
    date = subsubfolder_split[-2]
    folder_name = subsubfolder_split[-1]

    # Chuyển 0109 thành 0901
    new_date = date[-2:] + date[:2]
    mew_folder_name = f"2024{new_date}_" + folder_name.replace(" ", "_") + "_raw"
    print(mew_folder_name)
