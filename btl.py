from datetime import datetime
class HangHoa:
    ma_hang: str
    ten_hang: str
    gia_ban: float
    gia_nhap: float
    so_luong_ton_kho: int

    def __init__(self, ma_hang: str, ten_hang: str, gia_ban: float, gia_nhap: float, so_luong_ton_kho: int,
                 ngay_san_xuat, han_su_dung):
        self.ma_hang = ma_hang
        self.ten_hang = ten_hang
        self.gia_ban = gia_ban
        self.gia_nhap = gia_nhap
        self.so_luong_ton_kho = so_luong_ton_kho
        self.ngay_san_xuat = ngay_san_xuat
        self.han_su_dung = han_su_dung
    def get_ma_hang(self):
        return self.ma_hang

    def get_ten_hang(self):
        return self.ten_hang

    def set_ten_hang(self, ten):
        self.ten_hang = ten

    def get_gia_ban(self):
        return self.gia_ban

    def set_gia_ban(self, gia):
        self.gia_ban = gia

    def get_gia_nhap(self):
        return self.gia_nhap

    def set_gia_nhap(self, gia_nhap):
        self.gia_nhap = gia_nhap

    def get_so_luong_ton_kho(self):
        return self.so_luong_ton_kho

    def set_so_luong_ton_kho(self, so_luong):
        self.so_luong_ton_kho = so_luong

    def get_ngay_san_xuat(self):
        return self.ngay_san_xuat

    def set_ngay_san_xuat(self, ngay_san_xuat):
        self.ngay_san_xuat = ngay_san_xuat

    def get_han_su_dung(self):
        return self.han_su_dung

    def set_han_su_dung(self, han_su_dung):
        self.han_su_dung = han_su_dung


class DonNhapHang:
    def __init__(self, ma_don, ngay_nhap_hang):
        self.ma_don = ma_don
        self.ngay_nhap_hang = ngay_nhap_hang
        self.danh_sach_hang_hoa = []

    def them_hang_hoa(self, ma_hang_hoa, so_luong, gia_nhap, thanh_tien):
        self.danh_sach_hang_hoa.append({
            'ma_hang': ma_hang_hoa,
            'so_luong_nhap': so_luong,
            'gia_nhap': gia_nhap,
            'thanh_tien': thanh_tien
        })

    def tinh_tong_tien(self):
        return sum(item['thanh_tien'] for item in self.danh_sach_hang_hoa)

    def get_ma_don(self):
        return self.ma_don

    def get_ngay_nhap_hang(self):
        return self.ngay_nhap_hang

    def get_danh_sach_hang_hoa(self):
        return self.danh_sach_hang_hoa

    # def tinh_tong_tien(self):
    #     return sum(item['thanh_tien'] for item in self.danh_sach_hang_hoa)


class ManageProduct:
    danh_sach_hang_hoa: list[HangHoa]
    danh_sach_don_hang: list[DonNhapHang]

    def __init__(self):
        self.danh_sach_hang_hoa = []
        self.danh_sach_don_hang = []

    def them_hang_hoa(self):
        try:
            while True:
                try:
                    ma_hang = input("Nhập mã hàng hoá: ")
                    if self.is_product_code_unique(ma_hang):
                        break
                    else:
                        print("Lỗi: Mã hàng đã tồn tại. Vui lòng nhập lại.")
                except ValueError:
                    print("Lỗi: Mã hàng đã tồn tại")

            ten_hang = input("Nhập tên hàng hoá: ")
            while True:
                try:
                    gia_ban = float(input("Nhập giá bán: "))
                    if gia_ban >= 0:
                        break
                    else:
                        print("Lỗi: Giá bán không thể là số âm. Vui lòng nhập lại.")
                except ValueError:
                    print("Lỗi: Vui lòng nhập một số cho giá bán.")

            while True:
                try:
                    gia_nhap = float(input("Giá nhập: "))
                    if gia_nhap >= 0:
                        break
                    else:
                        print("Lỗi: Giá nhập không thể là số âm. Vui lòng nhập lại.")
                except ValueError:
                    print("Lỗi: Vui lòng nhập một số cho giá nhập.")
            # Kiểm tra ràng buộc số lượng không âm
            while True:
                try:
                    so_luong_ton_kho = int(input("Số lượng tồn kho: "))
                    if so_luong_ton_kho >= 0:
                        break
                    else:
                        print("Lỗi: Số lượng không thể là số âm. Vui lòng nhập lại.")
                except ValueError:
                    print("Lỗi: Vui lòng nhập một số nguyên cho số lượng tồn kho.")
            try:
                ngay_san_xuat = datetime.strptime(input("Nhập ngày sản xuất (YYYY-MM-DD): "), "%Y-%m-%d")
            except ValueError:
                print("Lỗi: Vui lòng nhập đúng định dạng")
            while True:
                try:
                    han_su_dung = datetime.strptime(input("Nhập hạn sử dụng (YYYY-MM-DD): "), "%Y-%m-%d")
                    if han_su_dung > ngay_san_xuat:
                        break
                    else:
                        print("Lỗi: Hạn sử phải lớn hơn ngày sản xuất. Vui lòng nhập lại.")
                except ValueError:
                    print("Lỗi: Vui lòng nhập đúng định dạng")

        except ValueError:
            raise ValueError
        new_product = HangHoa(ma_hang, ten_hang, gia_ban, gia_nhap, so_luong_ton_kho, ngay_san_xuat, han_su_dung)
        self.danh_sach_hang_hoa.append(new_product)

    def is_product_code_unique(self, ma_hang):
        for product in self.danh_sach_hang_hoa:
            if product.get_ma_hang() == ma_hang:
                return False
        return True

    def tim_hang_hoa(self, keyword):
        result = []
        for hang_hoa in self.danh_sach_hang_hoa:
            if keyword.lower() in hang_hoa.get_ten_hang().lower():
                result.append(hang_hoa)
        return result

    def hien_hang_hoa(self):
        if not self.danh_sach_hang_hoa:
            print("Danh sách hàng hoá trống.")
        else:
            print("\nDanh sách hàng hoá:")
            for hang_hoa in self.danh_sach_hang_hoa:
                print(
                    f"Mã hàng: {hang_hoa.get_ma_hang()}\t Tên: {hang_hoa.get_ten_hang()}\t "
                    f"Giá bán: {hang_hoa.get_gia_ban()}\t Giá Nhập: {hang_hoa.get_gia_nhap()}\t  Số lượng tồn kho: {hang_hoa.get_so_luong_ton_kho()}")

    def them_don_hang(self):
        try:
            while True:
                try:
                    ma_don_hang = input("Nhập mã đơn hàng: ")
                    if self.is_bill_code_unique(ma_don_hang):
                        break
                    else:
                        print("Lỗi: Mã đơn hàng đã tồn tại. Vui lòng nhập lại.")
                except ValueError:
                    print("Lỗi: Mã đơn hàng đã tồn tại")

            ngay_nhap_hang = datetime.now()
            new_don = DonNhapHang(ma_don_hang, ngay_nhap_hang)

            while True:
                try:
                    ma_hang_nhap = input("Nhập mã hàng hoá: ")
                    hang_hoa = self.get_hang_hoa_theo_id(ma_hang_nhap)
                    if hang_hoa is not None:
                        gia_nhap = hang_hoa.get_gia_nhap()
                        so_luong_nhap = int(input("Nhập số lượng nhập: "))
                        thanh_tien = so_luong_nhap * gia_nhap
                        hang_hoa.set_so_luong_ton_kho(hang_hoa.get_so_luong_ton_kho() + so_luong_nhap)
                        new_don.them_hang_hoa(ma_hang_nhap, so_luong_nhap, gia_nhap, thanh_tien)
                        break
                    else:
                        print("Lỗi: Mã hàng không tồn tại. Vui lòng nhập lại.")
                except ValueError:
                    print("Lỗi: Vui lòng nhập lại số lượng nhập.")

            self.danh_sach_don_hang.append(new_don)

        except ValueError:
            raise ValueError

    def sua_hang_hoa(self):
        try:
            while True:
                try:
                    ma_hang_hoa_sua = input("Nhập mã hàng hoá muốn sửa: ")
                    if not self.is_product_code_unique(ma_hang_hoa_sua):
                        break
                    else:
                        print("Lỗi: Mã hàng chưa tồn tại. Vui lòng nhập lại.")
                except ValueError:
                    print("Lỗi: Mã hàng chưa tồn tại")
            hang = self.get_hang_hoa_theo_id(ma_hang_hoa_sua)
            while True:
                choose = input("Bạn muốn sửa thông tin nào: 1.Tên | 2.Gía bán | 3.Gía nhập | 4.Số lượng tồn kho | Nhấn bất kì để thoát\n Lựa chọn của bạn: ")
                if choose == '1':
                    ten_hang_sua = input("Nhập tên hàng hoá: ")
                    hang.set_ten_hang(ten_hang_sua)
                elif choose == '2':
                    while True:
                        try:
                            gia_ban_sua = float(input("Nhập giá bán: "))
                            if gia_ban_sua >= 0:
                                hang.set_gia_ban(gia_ban_sua)
                                break
                            else:
                                print("Lỗi: Giá bán không thể là số âm. Vui lòng nhập lại.")
                        except ValueError:
                            print("Lỗi: Vui lòng nhập một số cho giá bán.")
                elif choose == '3':
                    while True:
                        try:
                            gia_nhap_sua = float(input("Giá nhập: "))
                            if gia_nhap_sua >= 0:
                                hang.set_gia_nhap(gia_nhap_sua)
                                break
                            else:
                                print("Lỗi: Giá nhập không thể là số âm. Vui lòng nhập lại.")
                        except ValueError:
                            print("Lỗi: Vui lòng nhập một số cho giá nhập.")
                    # Kiểm tra ràng buộc số lượng không âm
                elif choose == '4':
                    while True:
                        try:
                            so_luong_ton_kho_sua = int(input("Số lượng tồn kho: "))
                            if so_luong_ton_kho_sua >= 0:
                                hang.set_so_luong_ton_kho(so_luong_ton_kho_sua)
                                break
                            else:
                                print("Lỗi: Số lượng không thể là số âm. Vui lòng nhập lại.")
                        except ValueError:
                            print("Lỗi: Vui lòng nhập một số nguyên cho số lượng tồn kho.")
                else:
                    break
                    # try:
                    #     ngay_san_xuat_sua = datetime.strptime(input("Nhập ngày sản xuất (YYYY-MM-DD): "), "%Y-%m-%d")
                    #     hang.set_ngay_san_xuat(ngay_san_xuat_sua)
                    # except ValueError:
                    #     print("Lỗi: Vui lòng nhập đúng định dạng")
                    # while True:
                    #     try:
                    #         han_su_dung_sua = datetime.strptime(input("Nhập hạn sử dụng (YYYY-MM-DD): "), "%Y-%m-%d")
                    #         if han_su_dung_sua > ngay_san_xuat_sua:
                    #             hang.set_han_su_dung(han_su_dung_sua)
                    #             break
                    #         else:
                    #             print("Lỗi: Hạn sử phải lớn hơn ngày sản xuất. Vui lòng nhập lại.")
                    #     except ValueError:
                    #         print("Lỗi: Vui lòng nhập đúng định dạng")

        except ValueError:
            raise ValueError

    def is_bill_code_unique(self, ma_don_hang):
        for product in self.danh_sach_don_hang:
            if product.get_ma_don() == ma_don_hang:
                return False
        return True

    def check_ten_theo_ma(self, ma_don_hang, ten_hang):
        for product in self.danh_sach_hang_hoa:
            if product.get_ma_hang() == ma_don_hang:
                if product.get_ten_hang == ten_hang:
                    return True
        return False

    def get_hang_hoa_theo_id(self, ma_hang_hoa):
        for product in self.danh_sach_hang_hoa:
            if product.get_ma_hang() == ma_hang_hoa:
                return product
        return None


def main():
    manager = ManageProduct()
    san_pham_1 = HangHoa("SP001", "Sữa tươi Vinamilk", 15000, 12000, 100, datetime(2022, 1, 1), datetime(2023, 1, 1))
    san_pham_2 = HangHoa("SP002", "Bánh mì tươi", 5000, 3000, 200, datetime(2022, 2, 1), datetime(2023, 2, 1))
    san_pham_3 = HangHoa("SP003", "Coca Cola", 12000, 8000, 150, datetime(2022, 3, 1), datetime(2023, 3, 1))
    san_pham_4 = HangHoa("SP004", "Mì gói", 5000, 3000, 300, datetime(2022, 4, 1), datetime(2023, 4, 1))

    manager.danh_sach_hang_hoa.extend([san_pham_1, san_pham_2, san_pham_3, san_pham_4])

    while True:
        print("\n----- Menu -----")
        print("1. Thêm mới hàng hoá")
        print("2. Tìm kiếm hàng hoá")
        print("3. Hiển thị danh sách hàng hoá")
        print("4. Thêm đơn hàng")
        print("5. Sửa thông tin hàng hoá")
        print("6. Thoát")
        choice = input("Chọn chức năng (1-4): ")

        if choice == '1':
            try:
                manager.them_hang_hoa()
            except ValueError:
                print("Loi nhap du lieu cho hang hoa")
        elif choice == '2':
            search_keyword = input("Nhập từ khóa tìm kiếm: ")
            search_result = manager.tim_hang_hoa(search_keyword)

            if not search_result:
                print(f"Không tìm thấy sản phẩm với từ khóa '{search_keyword}'.")
            else:
                print(f"Kết quả tìm kiếm với từ khóa '{search_keyword}':")
                for product in search_result:
                    print(
                        f"Mã hàng: {product.get_ma_hang()}\t Tên: {product.get_ten_hang()}\t "
                        f"Giá bán: {product.get_gia_ban()}\t Số lượng tồn kho: {product.get_so_luong_ton_kho()}")
        elif choice == '3':
            manager.hien_hang_hoa()
        elif choice == '4':
            manager.them_don_hang()
        elif choice == '5':
            manager.sua_hang_hoa()
        elif choice == '6':
            print("Thoát chương trình. Hẹn gặp lại!")
            break
        else:
            print("Chọn không hợp lệ. Vui lòng chọn lại.")


if __name__ == "__main__":
    main()

# # Ví dụ sử dụng:
# # Tạo đối tượng đơn nhập hàng
# don_nhap_hang_1 = DonNhapHang("DNH001", datetime.now().strftime("%d/%m/%Y"))
# don_nhap_hang_2 = DonNhapHang("DNH002", datetime.now().strftime("%d/%m/%Y"))
#
# # Thêm hàng hoá vào đơn nhập hàng
# so_luong_nhap_1 = 50
# thanh_tien_1 = so_luong_nhap_1 * hang_hoa_1.gia_nhap
# so_luong_nhap_2 = 30
# thanh_tien_2 = so_luong_nhap_2 * hang_hoa_2.gia_nhap
#
# so_luong_nhap_3 = 40
# thanh_tien_3 = so_luong_nhap_3 * hang_hoa_3.gia_nhap
# so_luong_nhap_4 = 10
# thanh_tien_4 = so_luong_nhap_4 * hang_hoa_4.gia_nhap
#
#
# don_nhap_hang_1.them_hang_hoa(hang_hoa_1, so_luong_nhap_1, thanh_tien_1)
# don_nhap_hang_1.them_hang_hoa(hang_hoa_2, so_luong_nhap_2, thanh_tien_2)
#
# don_nhap_hang_2.them_hang_hoa(hang_hoa_3, so_luong_nhap_3, thanh_tien_3)
# don_nhap_hang_2.them_hang_hoa(hang_hoa_4, so_luong_nhap_4, thanh_tien_4)
#
# # Tính tổng tiền của đơn nhập hàng
# tong_tien_don_nhap_hang_1 = don_nhap_hang_1.tinh_tong_tien()
# tong_tien_don_nhap_hang_2 = don_nhap_hang_2.tinh_tong_tien()
#
# # In thông tin đơn nhập hàng
# print(f"Mã Đơn Nhập Hàng: {don_nhap_hang_1.ma_don}")
# print(f"Ngày Nhập Hàng: {don_nhap_hang_1.ngay_nhap_hang}")
# print("Danh sách hàng hoá trong đơn nhập hàng:")
# for item in don_nhap_hang_1.danh_sach_hang_hoa:
#     print(f"  - Mã Hàng Hoá: {item['ma_hang']}, Tên Hàng Hoá: {item['ten_hang']}, Số Lượng Nhập: {item['so_luong_nhap']}, Thành Tiền: {item['thanh_tien']}")
#
# print(f"Tổng Tiền Đơn Nhập Hàng: {tong_tien_don_nhap_hang_1}")
#
#
# print(f"Mã Đơn Nhập Hàng: {don_nhap_hang_2.ma_don}")
# print(f"Ngày Nhập Hàng: {don_nhap_hang_2.ngay_nhap_hang}")
# print("Danh sách hàng hoá trong đơn nhập hàng:")
# for item in don_nhap_hang_2.danh_sach_hang_hoa:
#     print(f"  - Mã Hàng Hoá: {item['ma_hang']}, Tên Hàng Hoá: {item['ten_hang']}, Số Lượng Nhập: {item['so_luong_nhap']}, Thành Tiền: {item['thanh_tien']}")
#
# print(f"Tổng Tiền Đơn Nhập Hàng: {tong_tien_don_nhap_hang_2}")