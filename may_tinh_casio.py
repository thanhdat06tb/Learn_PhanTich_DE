import customtkinter as ct

ct.set_appearance_mode("Dark")
ct.set_default_color_theme("blue")

class App(ct.CTk):
    def __init__(self):
        super().__init__()

        #Cau hinh cua so chinh
        self.title("MAY ANH CASSIO")
        self.geometry("300x400")
        self.resizable(False, False)

        #Bien luu tru phep tinh
        self.bieu_thuc = ""

        #1. O hien thi (Display)
        self.man_hinh = ct.CTkEntry(self, width=280, height=50, font=("Arial", 24), justify="right")
        self.man_hinh.grid(row=0, column=0, columnspan=4, padx=10,pady=20)

        # 2. Danh sach cac nut ( Text, Row, Column)
        nut_bam = [
            ('7', 1, 0),('8', 1, 1), ('9', 1, 2), ('Chia', 1, 3),
            ('4', 2, 0),('5', 2, 1), ('6', 2, 2), ('Nhan', 2, 3),
            ('1', 3, 0), ('2',3, 1), ('3', 3, 2), ('Tru', 3, 3),
            ('0', 4, 0), ('Xoa',4, 1), ('=', 4, 2), ('Cong', 4, 3),
        ]

        # Tao cac nut bam tu dong bang vong lap
        for (text, row, col) in nut_bam:
            # Dung lambda de truyn tham so vao khi bam nut
            button = ct.CTkButton(self, text = text, width=60, height=50,
                                  command = lambda t=text: self.xu_ly_su_kien(t))
            button.grid(row=row, column=col, padx=5, pady=5)

    def xu_ly_su_kien(self, loai_nut):
        if loai_nut == "=":
            self.tinh_ket_qua()
        elif loai_nut == "Xoa":
            self.xoa_man_hinh()
        else:
            # Thay the ten tieng viet bang toan tu toan hoc
            mapping = {"Cong":"+", "Tru":"-", "Nhan":"*", "Chia":"/"}
            gia_tri =  mapping.get(loai_nut, loai_nut)

            self.bieu_thuc += str(gia_tri)
            self.cap_nhat_man_hinh()

    def cap_nhat_man_hinh(self):
        self.man_hinh.delete(0, ct.END)
        self.man_hinh.insert(0, self.bieu_thuc)

    def xoa_man_hinh(self):
        self.bieu_thuc = ""
        self.cap_nhat_man_hinh()

    def tinh_ket_qua(self):
        try:
            #Ham eval() se tu dong tinh toan cac phep tinh
            ket_qua = str(eval(self.bieu_thuc))
            self.man_hinh.delete(0, ct.END)
            self.man_hinh.insert(0, ket_qua)
            self.bieu_thuc = ket_qua

        except Exception:
            self.man_hinh.delete(0, ct.END)
            self.man_hinh.insert(0, "Loi")
            self.bieu_thuc = ""

if __name__ == "__main__":
    app = App( )
    app.mainloop()