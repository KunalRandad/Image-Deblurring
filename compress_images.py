sharp_dir = r"C:\Users\91702\Desktop\Sem_8\gnr638\train_downscaled\train_sharp"
blurred_image_dir_1 = r"C:\Users\91702\Desktop\Sem_8\gnr638\train_downscaled\train_sharp_blur_1"
blurred_image_dir_2 = r"C:\Users\91702\Desktop\Sem_8\gnr638\train_downscaled\train_sharp_blur_2"
blurred_image_dir_3 = r"C:\Users\91702\Desktop\Sem_8\gnr638\train_downscaled\train_sharp_blur_3"
home_dir = r"C:\Users\91702\Desktop\Sem_8\gnr638"
import os
import shutil
# sharp and blurred dir have folders named 000 to 239. Go throughall the folders. Each folder has 100 png images. Read the 1st, 40th and 80th image from each folder and store them at home_dir\train_reduced_downscaled\train_sharp\folder_name\image_name, and so on
for i in range(240):
    folder_number = i
    folder_name = str(folder_number).zfill(3)
    sharp_folder_path = os.path.join(sharp_dir, folder_name)
    blurred_folder_path_1 = os.path.join(blurred_image_dir_1, folder_name)
    blurred_folder_path_2 = os.path.join(blurred_image_dir_2, folder_name)
    blurred_folder_path_3 = os.path.join(blurred_image_dir_3, folder_name)

    # In the list of files in sharp_folder_path, read the 1st, 40th and 80th image
    sharp_files = os.listdir(sharp_folder_path)
    sharp_files.sort()
    sharp_image_1 = sharp_files[0]
    sharp_image_40 = sharp_files[39]
    sharp_image_80 = sharp_files[79]
    sharp_image_1_path = os.path.join(sharp_folder_path, sharp_image_1)
    sharp_image_40_path = os.path.join(sharp_folder_path, sharp_image_40)
    sharp_image_80_path = os.path.join(sharp_folder_path, sharp_image_80)
    # Copy the 1st, 40th and 80th image to home_dir\train_reduced_downscaled\train_sharp\folder_name
    sharp_folder_path_new = os.path.join(home_dir, "train_reduced_downscaled", "train_sharp", folder_name)
    if not os.path.exists(sharp_folder_path_new):
        os.makedirs(sharp_folder_path_new)
    shutil.copy(sharp_image_1_path, sharp_folder_path_new)
    shutil.copy(sharp_image_40_path, sharp_folder_path_new)
    shutil.copy(sharp_image_80_path, sharp_folder_path_new)

    # Do same for blurred_folder_path_1, blurred_folder_path_2, blurred_folder_path_3
    blurred_folder_path_1_new = os.path.join(home_dir, "train_reduced_downscaled", "train_sharp_blur_1", folder_name)
    blurred_folder_path_2_new = os.path.join(home_dir, "train_reduced_downscaled", "train_sharp_blur_2", folder_name)
    blurred_folder_path_3_new = os.path.join(home_dir, "train_reduced_downscaled", "train_sharp_blur_3", folder_name)

    blurred_image_1_1 = sharp_files[0]
    blurred_image_1_40 = sharp_files[39]
    blurred_image_1_80 = sharp_files[79]
    blurred_image_1_1_path = os.path.join(blurred_folder_path_1, blurred_image_1_1)
    blurred_image_1_40_path = os.path.join(blurred_folder_path_1, blurred_image_1_40)
    blurred_image_1_80_path = os.path.join(blurred_folder_path_1, blurred_image_1_80)

    blurred_image_2_1 = sharp_files[0]
    blurred_image_2_40 = sharp_files[39]
    blurred_image_2_80 = sharp_files[79]
    blurred_image_2_1_path = os.path.join(blurred_folder_path_2, blurred_image_2_1)
    blurred_image_2_40_path = os.path.join(blurred_folder_path_2, blurred_image_2_40)
    blurred_image_2_80_path = os.path.join(blurred_folder_path_2, blurred_image_2_80)

    blurred_image_3_1 = sharp_files[0]
    blurred_image_3_40 = sharp_files[39]
    blurred_image_3_80 = sharp_files[79]
    blurred_image_3_1_path = os.path.join(blurred_folder_path_3, blurred_image_3_1)
    blurred_image_3_40_path = os.path.join(blurred_folder_path_3, blurred_image_3_40)
    blurred_image_3_80_path = os.path.join(blurred_folder_path_3, blurred_image_3_80)

    if not os.path.exists(blurred_folder_path_1_new):
        os.makedirs(blurred_folder_path_1_new)

    shutil.copy(blurred_image_1_1_path, blurred_folder_path_1_new)
    shutil.copy(blurred_image_1_40_path, blurred_folder_path_1_new)
    shutil.copy(blurred_image_1_80_path, blurred_folder_path_1_new)

    if not os.path.exists(blurred_folder_path_2_new):
        os.makedirs(blurred_folder_path_2_new)

    shutil.copy(blurred_image_2_1_path, blurred_folder_path_2_new)
    shutil.copy(blurred_image_2_40_path, blurred_folder_path_2_new)
    shutil.copy(blurred_image_2_80_path, blurred_folder_path_2_new)

    if not os.path.exists(blurred_folder_path_3_new):
        os.makedirs(blurred_folder_path_3_new)

    shutil.copy(blurred_image_3_1_path, blurred_folder_path_3_new)
    shutil.copy(blurred_image_3_40_path, blurred_folder_path_3_new)
    shutil.copy(blurred_image_3_80_path, blurred_folder_path_3_new)

# Now we have the required images in the required folders.