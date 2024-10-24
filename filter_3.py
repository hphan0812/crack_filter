import os

# Đường dẫn tới thư mục output_test và crack_true
source_folder = '/Users/hanhphan/Documents/crack_filter/output_test'  # Thay đổi đường dẫn của bạn
destination_folder = '/Users/hanhphan/Documents/crack_filter/output_crack/crack_true'  # Thay đổi đường dẫn của bạn

# Lấy danh sách tất cả các thư mục con trong output_test
folders_in_source = [f for f in os.listdir(source_folder) if os.path.isdir(os.path.join(source_folder, f))]

# Lặp qua tất cả các thư mục con trong output_test
for folder_name in folders_in_source:
    # Đường dẫn của thư mục tương ứng trong crack_true
    destination_path = os.path.join(destination_folder, folder_name)
    
    # Kiểm tra xem thư mục tương ứng có tồn tại trong crack_true không
    if os.path.exists(destination_path):
        # Nếu thư mục tồn tại, tạo các thư mục con 0, 1, 2,... trong đó
        for i in range(25):  # Thay đổi phạm vi số lượng thư mục con nếu cần
            subfolder_name = str(i)
            subfolder_path = os.path.join(destination_path, subfolder_name)
            
            # Tạo thư mục con nếu chưa tồn tại
            os.makedirs(subfolder_path, exist_ok=True)
            print(f"Đã tạo thư mục: {subfolder_path}")
    else:
        print(f"Thư mục {folder_name} không tồn tại trong crack_true")

print("Hoàn thành việc tạo thư mục con.")



