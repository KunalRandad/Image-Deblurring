import os
from PIL import Image

# Set the input and output directories
input_dir = r"C:\Users\91702\Desktop\Sem_8\gnr638\train\train_sharp"
output_dir = r"C:\Users\91702\Desktop\Sem_8\gnr638\train_downscaled\train_sharp"

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Iterate over all subfolders in the input directory
for subfolder in os.listdir(input_dir):
    subfolder_path = os.path.join(input_dir, subfolder)
    
    # Iterate over all images in the subfolder
    for image_file in os.listdir(subfolder_path):
        image_path = os.path.join(subfolder_path, image_file)
        
        # Open the image
        image = Image.open(image_path)
        
        # Resize the image to (256, 448)
        # resized_image = image.resize((256, 448)) # THIS WORSENS THE ASPECT RATIO
        resized_image = image.resize((448, 256))
        
        # Save the resized image to the output directory
        output_path = os.path.join(output_dir, subfolder, image_file)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        resized_image.save(output_path)
    print(f"Finished downscaling images in {subfolder} subfolder")
print("Image downscaling complete!")