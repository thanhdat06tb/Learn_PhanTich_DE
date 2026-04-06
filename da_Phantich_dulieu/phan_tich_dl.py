import requests
import csv
import pandas as pd

def market_data():
    # Đỉa chỉ chứa dữ liệu cần phân tích
    url = "https://jsonplaceholder.typicode.com/posts/"

    try:
    # Gửi yêu cầu để lấy dữ liệu
        response = requests.get(url)

    # Kiểm tra máy chủ có trả lời thành công hay không?
        if response.status_code == 200:

    # Chuyển dữu liệu về dạng từ điển văn bản
            data = response.json()

    # Trích xuất thông tin cụ thể 
            print("Kết quả trả về:")
        for i in data[:5]:
            print("-" * 30)
            print(f"ID bai viet thu {i}: {i['id']}")
            print(f"Tieu de: {i['title']}")
            print(f"Noi dung: {i['body']}")
            print("-" * 30)
                
        else:
            print(f"Loi roi! Ma loi:{response.status_code}")
    except  Exception as error:
        print(f"Không thể kết nối internet hoặc đường link bị hỏng:{error}")

market_data()