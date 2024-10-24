import os

def count_png_files_in_folder(folder_path):
    png_count = 0
    # Walk through the directory and subdirectories
    for root, dirs, files in os.walk(folder_path):
        # Count .png files in the current directory
        png_count += len([file for file in files if file.lower().endswith('.png')])
    return png_count

folder_path = '/media/HDD0/hanhphan/output_crack'
png_file_count = count_png_files_in_folder(folder_path)
print(f"Số file .png tìm thấy: {png_file_count}")
