import requests
import csv
import pandas as pd 
# Import thư viện Pandas để xử lý bảng dữ liệu

def market_data():
    # Địa chỉ chứa dữ liệu cần phân tích
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1&sparkline=false"

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
            df_final = df[['id', 'symbol', 'current_price', 'market_cap', 'price_change_percentage_24h']]

            # Chuyển tên thuộc tính tương ứng với dữ liệu
            mapping = {
                'id': 'mã',
                'symbol': 'ký hiệu',
                'current_price': 'giá hiện tại',
                'market_cap': 'vốn hóa thị trường',
                'price_change_percentage_24h': '% Thay đổi trong 24h'
            }

            df_final = df_final.rename(columns=mapping)

            # Tạo thêm cột Nhóm vốn hóa:
            bins = [0, 10_000_000_000, 100_000_000_000, float('inf')]
            labels = ['Small-cap (<10B)', 'Mid-cap (10-100B)', 'Large-cap (>100B)']

            df_final['nhóm vốn hóa'] = pd.cut(df_final['vốn hóa thị trường'], bins=bins, labels=labels)

            # In ra 
            print(df_final[['mã', 'ký hiệu', 'vốn hóa thị trường', 'nhóm vốn hóa']].head())


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