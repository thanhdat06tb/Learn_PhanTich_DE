import requests
import csv
import pandas as pd 
# Import thư viện Pandas để xử lý bảng dữ liệu

def market_data():
    # Địa chỉ chứa dữ liệu cần phân tích
    url = "https://jsonplaceholder.typicode.com/posts/"

    try:
        # --- BƯỚC 1: LẤY DỮ LIỆU (EXTRACT) ---
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            print("Kết nối thành công! Đang xử lý dữ liệu...")

            # ==========================================================
            # CODE CŨ (Dùng vòng lặp for - In thủ công)
            # ==========================================================
            # print("Kết quả trả về (Cách cũ):")
            # for i in data[:5]:
            #     print("-" * 30)
            #     print(f"ID bai viet thu {i}: {i['id']}")
            #     print(f"Tieu de: {i['title']}")
            #     print(f"Noi dung: {i['body']}")
            #     print("-" * 30)
            
            # ==========================================================
            # CODE MỚI (Dùng Pandas - Xử lý dạng bảng chuyên nghiệp)
            # ==========================================================
            
            # 1. Chuyển list dữ liệu JSON thành một bảng (DataFrame)
            df = pd.DataFrame(data)

            # 2. Trích xuất thông tin: Chỉ lấy các cột quan trọng
            # Thay vì dùng vòng lặp, ta chỉ định danh sách cột muốn giữ lại
            df_final = df[['id', 'title', 'body']]

            # 3. Hiển thị thử 5 dòng đầu tiên để kiểm tra (Thay cho vòng lặp for)
            print("\n--- 5 dòng đầu tiên xử lý bằng Pandas ---")
            print(df_final.head()) 

            # 4. Lưu kết quả ra file CSV (Bước Load trong DE)
            # index=False để không lưu cột số thứ tự mặc định của Pandas
            df_final.to_csv("ket_qua_phan_tich.csv", index=False, encoding='utf-8-sig')
            
            print("\n[SUCCESS] Đã lưu dữ liệu vào file: ket_qua_phan_tich.csv")

        else:
            print(f"Lỗi rồi! Mã lỗi: {response.status_code}")

    except Exception as error:
        print(f"Không thể kết nối internet hoặc đường link bị hỏng: {error}")

# Chạy hàm
market_data()