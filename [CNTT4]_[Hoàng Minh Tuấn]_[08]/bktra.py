car = [
    {
        "ID": "XE001",
        "info_car": "29C-12345",
        "Name": "Tai A",
        "Km": 12,
        "total_km": 500,
        "total_low": 65,
        "nber": 5.0,
        "status": "Tiêu hao cao"
    },
]
def find_id(car,car_id):
    car_id = car_id.strip().upper()

    for i ,v  in enumerate(car):
        if v['ID'] == car_id:
            return i
        
    return -1

def calculate_car(avg):
    if avg >= 8:
        return "Quá tải / Thất thoát"
    elif avg >= 2:
        return "Tiêu hao cao"
    elif avg >= 0 :
        return "Tiêu chuẩn"
    else:
        return "Tiết kiệm"
while True:
    choice = input('''
===============Car MANAGER===============
1. Hiển thị danh sách đội xe
2. Bổ sung xe mới vào đội
3. Cập nhật nhật ký hành trình
4. Xóa xe khỏi đội quản lý
5. Tìm kiếm phương tiện
6. Thống kê hiệu suất hạm đội
7. Thoat            
Moi ban nhap lua chon(1-7): ''')
    match choice:
        case "1":
            if(len(car) == 0):
                print("[LOI]: Danh sach rong!")
                continue
            
            print("="*120)
            print(f"{'ID':<8} | {'Bien so':<12} | {'Ten':<12} | {'Lít/100km':<10} | {'Tổng số km':<10} | {'tiêu thụ':<10} | {'Chênh lệch':<10} | {'Trạng thái':<15}")
            for i in car:
                print(f"{i['ID']:<8} | {i['info_car']:<12} | {i['Name']:<12} | {i['Km']:<10} | {i['total_km']:<10} | {i['total_low']:<10} | {i['nber']:<10} | {i['status']:<15}")

            print("="*120)
        
        case "2":
            while True:
                car_id = input("Nhập mã xe: ").strip().upper()
                if any(i["ID"] == car_id for i in car):
                    print("Mã xe đã tồn tại!")
                else:
                    break
            
            
            new_info = input("Nhap bien so xe moi: ").strip()
            if any(i["info_car"] == new_info for i in car):
                print("Biển số xe đã tồn tại!")
            else:
                break

            new_name = input("Nhap ten tai xe: ")
            new_km = int(input("Nhap dịnh mức lý thuyết(Lít/100km): "))
            new_total_km = int(input("Nhap so km ban dau: "))
            new_total_low = int(input("Nhap số nhiên liệu tiêu thụ thực tế (Lít)"))

            total = round((new_total_km * new_km) / 100, 2)
            new_nber = new_total_low - total
            new_status = calculate_car(new_nber)

            car.append({
                "ID": car_id,
                "info_car": new_info,
                "Name": new_name,
                "Km": new_km,
                "total_km": new_total_km,
                "total_low": new_total_low,
                "nber": new_nber,
                "status": new_status
            })
            print("Da them thanh cong")

        case "3":
            car_id = input("Nhap ID can cap nhat")
            check = find_id(car,car_id)

            if check == -1:
                print("Khong tim thay xe can cap nhap!!")
                continue

            while True:
                try:
                    upt_km = int(input("Nhap dinh mua ly thuyet can cap nhat: "))
                    if(upt_km < 0):
                        raise Exception()
                    break
                except:
                    print("Dinh muc ly thuyet khong duoc am!")

            while True:
                try:
                    upt_total_km = int(input("Nhap tong so km di chuyen can cap nhat: "))
                    if(upt_total_km < 0):
                        raise Exception()
                    break
                except:
                    print("Tong so km di chuyen khong duoc am!")

            while True:
                try:
                    upt_total_low = int(input("Nhap tong so nhien lieu tieu thu can cap nhat: "))
                    if(upt_total_low < 0):
                        raise Exception()
                    break
                except:
                    print("Tong so nhien lieu tieu thu khong duoc am!")

            avg = round((upt_km * upt_total_km) / 100, 2)
            upd_nber = upt_total_low - avg
            upd_status = calculate_car(upd_nber)
            car[check]['Km'] = upt_km
            car[check]['total_km'] = upt_total_km
            car[check]['total_low'] =  upt_total_low
            car[check]['nber'] = upd_nber
            car[check]['status'] = upd_status

            print("Cap nhat thanh cong!")

        case "4":
            car_id = input("Nhap Id can xoa: ")
            check = find_id(car,car_id)

            if check == -1:
                print("Khong tim ID can xoa!!")
                continue

            choose = input("Ban co xac nhan xoa khong(Y/N): ").strip().upper()
            if(choose == "Y"):
                car.remove(car[check])
                print("Da xoa xe thanh cong!")
            else:
                print("Yeu cau xoa khong thuc hien!")
                continue
        
        case "5":
            continue
        case "6":
            if(car == []):
                print("Danh sach rong!")
                continue

            count_1 = 0
            count_2 = 0
            count_3 = 0
            count_4 = 0
            for i in car:
                if(i["status"] == "Tiết kiệm"):
                    count_1 += 1
                elif(i["status"] == "Tiêu chuẩn"):
                    count_2 += 1
                elif(i["status"] == "Tiêu hao cao"):
                    count_3 += 1
                else:
                    count_4 +=1
            
            print(f"So luong xe tiet kiem {count_1} xe")
            print(f"So luong xe tieu chuan  {count_2} xe")
            print(f"So luong xe tieu hao cao {count_3} xe")
            print(f"So luong xe qua tai {count_4} xe")
        case "7":
            print("Thoat chuong trinh!")
            break
        case _:
            print("Lua chon khong hop le!")
