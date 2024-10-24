import os
import shutil

# Danh sách các thư mục đầu vào (có thể chứa nhiều đường dẫn)
input_folders = [
    '/home/hanhphan/model_v3_5_3_test_profile/20240901_D0109_CRACK_MARKING_raw',
    '/home/hanhphan/model_v3_5_3_test_profile/20240901_D0109_DO_LAI_CRACK_raw',
    '/home/hanhphan/model_v3_5_3_test_profile/20240901_N_0109_CRACK_LATMAT_raw',
    '/home/hanhphan/model_v3_5_3_test_profile/20240901_N_0109_CRACK_raw',
    '/home/hanhphan/model_v3_5_3_test_profile/20240902_D0209_CRACK_DO_LAI_raw',
    '/home/hanhphan/model_v3_5_3_test_profile/20240902_D0209_CRACK_MARKING_raw',
    '/home/hanhphan/model_v3_5_3_test_profile/20240902_N_0209_LAT_MAT_raw',
    '/home/hanhphan/model_v3_5_3_test_profile/20240902_N_0209_raw',
    # Thêm nhiều đường dẫn khác tại đây nếu cần
]

# Thư mục gốc đầu ra (nó sẽ tự động tạo thư mục con cho mỗi thư mục đầu vào)
output_root_folder = '/home/hanhphan/model_v3_5_3_test_profile/output_test'
os.makedirs(output_root_folder, exist_ok=True)

# Hàm xử lý từng thư mục đầu vào
def process_input_folder(input_folder, output_root_folder):
    # Lấy tên thư mục đầu vào để tạo thư mục đích tương ứng
    input_folder_name = os.path.basename(input_folder.rstrip('/'))
    output_folder = os.path.join(output_root_folder, input_folder_name)
    os.makedirs(output_folder, exist_ok=True)

    # Duyệt qua tất cả các thư mục con
    for root, dirs, files in os.walk(input_folder):
        for sub_dir in dirs:
            if sub_dir.isdigit():  # Kiểm tra nếu thư mục con là số (0, 1, 2,...)
                crack_dir = os.path.join(root, sub_dir, 'CRACK')
                if os.path.exists(crack_dir):  # Kiểm tra nếu thư mục "CRACK" tồn tại
                    # Tạo thư mục đích trong thư mục đầu ra
                    dest_dir = os.path.join(output_folder, sub_dir)
                    os.makedirs(dest_dir, exist_ok=True)
                    
                    # Lấy danh sách các tệp trong thư mục "CRACK"
                    for file_name in os.listdir(crack_dir):
                        # Kiểm tra nếu tên tệp không chứa số hoặc ký tự sau dấu gạch dưới cuối cùng
                        if not any(file_name.endswith(f"_{i}.png") for i in range(10)):
                            source_file = os.path.join(crack_dir, file_name)
                            destination_file = os.path.join(dest_dir, file_name)
                            shutil.copy(source_file, destination_file)

    print(f'Files from {input_folder} have been copied and organized in: {output_folder}')


# Lặp qua danh sách các thư mục đầu vào và xử lý chúng
for input_folder in input_folders:
    process_input_folder(input_folder, output_root_folder)
