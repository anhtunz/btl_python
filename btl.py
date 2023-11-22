from datetime import datetime

class HangHoa:
    def __init__(self, ma_hang, ten_hang, gia_ban, gia_nhap, so_luong_ton_kho, ngay_san_xuat, han_su_dung):
        self.ma_hang = ma_hang
        self.ten_hang = ten_hang
        self.gia_ban = gia_ban
        self.gia_nhap = gia_nhap
        self.so_luong_ton_kho = so_luong_ton_kho
        self.ngay_san_xuat = ngay_san_xuat
        self.han_su_dung = han_su_dung

    # # Getter và setter cho mã hàng
    # def get_ma_hang(self):
    #     return self.ma_hang

    # def set_ma_hang(self, ma_hang):
    #     self.ma_hang = ma_hang

class DonNhapHang:
    def __init__(self, ma_don, ngay_nhap_hang):
        self.ma_don = ma_don
        self.ngay_nhap_hang = ngay_nhap_hang
        self.danh_sach_hang_hoa = []

    def them_hang_hoa(self, hang_hoa, so_luong, thanh_tien):
        self.danh_sach_hang_hoa.append({
            'ma_hang': hang_hoa.ma_hang,
            'ten_hang': hang_hoa.ten_hang,
            'so_luong_nhap': so_luong,
            'gia_nhap': hang_hoa.gia_nhap,
            'thanh_tien': thanh_tien
        })

    def tinh_tong_tien(self):
        return sum(item['thanh_tien'] for item in self.danh_sach_hang_hoa)

# Ví dụ sử dụng:
# Tạo đối tượng hàng hoá
hang_hoa_1 = HangHoa("HH001", "Bánh quy", 5000, 3000, 100, "01/01/2023", "01/01/2024")
hang_hoa_2 = HangHoa("HH001", "Bánh quy1", 8000, 2000, 100, "01/01/2023", "01/01/2024")

hang_hoa_3 = HangHoa("HH001", "Bánh quy3", 5000, 3000, 100, "01/01/2023", "01/01/2024")
hang_hoa_4 = HangHoa("HH001", "Bánh quy4", 8000, 2000, 100, "01/01/2023", "01/01/2024")
# Tạo đối tượng đơn nhập hàng
don_nhap_hang_1 = DonNhapHang("DNH001", datetime.now().strftime("%d/%m/%Y"))
don_nhap_hang_2 = DonNhapHang("DNH002", datetime.now().strftime("%d/%m/%Y"))

# Thêm hàng hoá vào đơn nhập hàng
so_luong_nhap_1 = 50
thanh_tien_1 = so_luong_nhap_1 * hang_hoa_1.gia_nhap 
so_luong_nhap_2 = 30
thanh_tien_2 = so_luong_nhap_2 * hang_hoa_2.gia_nhap 

so_luong_nhap_3 = 40
thanh_tien_3 = so_luong_nhap_3 * hang_hoa_3.gia_nhap 
so_luong_nhap_4 = 10
thanh_tien_4 = so_luong_nhap_4 * hang_hoa_4.gia_nhap 


don_nhap_hang_1.them_hang_hoa(hang_hoa_1, so_luong_nhap_1, thanh_tien_1)
don_nhap_hang_1.them_hang_hoa(hang_hoa_2, so_luong_nhap_2, thanh_tien_2)

don_nhap_hang_2.them_hang_hoa(hang_hoa_3, so_luong_nhap_3, thanh_tien_3)
don_nhap_hang_2.them_hang_hoa(hang_hoa_4, so_luong_nhap_4, thanh_tien_4)

# Tính tổng tiền của đơn nhập hàng
tong_tien_don_nhap_hang_1 = don_nhap_hang_1.tinh_tong_tien()
tong_tien_don_nhap_hang_2 = don_nhap_hang_2.tinh_tong_tien()

# In thông tin đơn nhập hàng
print(f"Mã Đơn Nhập Hàng: {don_nhap_hang_1.ma_don}")
print(f"Ngày Nhập Hàng: {don_nhap_hang_1.ngay_nhap_hang}")
print("Danh sách hàng hoá trong đơn nhập hàng:")
for item in don_nhap_hang_1.danh_sach_hang_hoa:
    print(f"  - Mã Hàng Hoá: {item['ma_hang']}, Tên Hàng Hoá: {item['ten_hang']}, Số Lượng Nhập: {item['so_luong_nhap']}, Thành Tiền: {item['thanh_tien']}")

print(f"Tổng Tiền Đơn Nhập Hàng: {tong_tien_don_nhap_hang_1}")


print(f"Mã Đơn Nhập Hàng: {don_nhap_hang_2.ma_don}")
print(f"Ngày Nhập Hàng: {don_nhap_hang_2.ngay_nhap_hang}")
print("Danh sách hàng hoá trong đơn nhập hàng:")
for item in don_nhap_hang_2.danh_sach_hang_hoa:
    print(f"  - Mã Hàng Hoá: {item['ma_hang']}, Tên Hàng Hoá: {item['ten_hang']}, Số Lượng Nhập: {item['so_luong_nhap']}, Thành Tiền: {item['thanh_tien']}")

print(f"Tổng Tiền Đơn Nhập Hàng: {tong_tien_don_nhap_hang_2}")