import os
import sqlite3

db_path = '/home/hanhphan/model_v3_5_3_test_profile/database_20240906.db'

# Kiểm tra tệp có tồn tại không
if os.path.exists(db_path):
    print("Tệp cơ sở dữ liệu tồn tại.")
else:
    print("Tệp cơ sở dữ liệu không tồn tại. Kiểm tra lại đường dẫn.")

try:
    # Thiết lập kết nối
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Truy vấn để lọc các lỗi liên quan đến "CRACK" trong cột defects
    query = """
    SELECT slip_id, d_points
    FROM product
    WHERE defects LIKE '%CRACK%'
    """
    
    cursor.execute(query)
    results = cursor.fetchall()

    if results:
        # Tạo thư mục tên "crack" nếu chưa tồn tại
        folder_path = './crack'
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        
        # Mở tệp tin để ghi kết quả đã lọc
        file_name = os.path.join(folder_path, 'filtered_crack_errors.txt')
        with open(file_name, 'w') as file:
            for row in results:
                slipid, d_point = row
                
                # Ghi slipid và tọa độ của crack vào tệp tin
                file.write(f"Slip ID: {slipid}, Tọa độ CRACK: {d_point}\n")
        
        print(f"Đã lọc và lưu các lỗi CRACK vào thư mục '{folder_path}'.")
    else:
        print("Không tìm thấy lỗi CRACK nào.")

    # Đóng kết nối
    conn.close()

except sqlite3.Error as e:
    print(f"Đã xảy ra lỗi: {e}")
