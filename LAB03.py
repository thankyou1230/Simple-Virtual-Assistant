from abc import ABC, abstractmethod
import random
class Human(ABC):
    def __init__(self):
        self.cmnd=''
        self.hoten=''
        self.diachi=''
        self.thunhap=''
    @abstractmethod
    def Nhapthongtin(self):
        pass
    @abstractmethod
    def Xuatthongtin(self):
        pass
    @abstractmethod
    def Thuephainop(self):
        pass

######################################################

class SinhVien(Human):
    def __init__(self, mssv, hoten, khoa):
        super(SinhVien, self).__init__()
        self.hoten=hoten
        self.mssv=mssv
        self.khoa=khoa
        self.mondahoc=[]
        self.diemtichluy=0
        self.diemtrungbinh=0
    #write later
    def Nhapthongtin(self):
        pass
    def Xuatthongtin(self):
        pass
    def Capnhatthongtin(self):
        pass
    def Capnhatdiem(self):
        pass
    def Xettonnghiep(self):
        pass
    def Thuephainop(self):
        pass

######################################################

class GiangVien(Human):
    def __init__(self,id,hoten,khoa,hocvi):
        super(GiangVien, self).__init__()
        self.hoten=hoten
        self.mgv=id
        self.khoa=khoa
        self.hocvi=hocvi
        self.hesoluong=''
    #write later
    def Nhapthongtin(self):
        pass
    def Xuatthongtin(self):
        pass
    def Capnhatthongtin(self):
        pass
    def Tinhtienluongthang(self):
        pass
    def Tietdaday(self):
        pass
    def Thuephainop(self):
        pass

########################################################

class MonHoc():
    def __init__(self,mamon, tenmon, sotinchi):
        self.mamon=mamon
        self.tenmon=tenmon
        self.sotinchi=sotinchi
    def Nhap(self):
        pass
    def Xuat(self):
        pass
    def Capnhat(self):
        pass


#######################################################

class BangDiem():
    def __init__(self,malop,magv,mamon,mssv,diem):
        self.malop=malop
        self.magv=magv
        self.mamon=mamon
        self.mssv=mssv
        self.diem=diem
    def Nhapdiem(self):
        pass
    def Xuatdiem(self):
        pass
    def Capnhatdiem(self):
        pass

########################################################
ho=['Đinh','Lý','Trần','Lê','Nguyễn','Triệu','Huỳnh','Võ','Châu','Dương']
lot=['Thị','Ngọc','Văn','Tuyết','Minh','Phước','Tấn','Thế','Tấn','Chí']
ten=['Khoa','Thành','Long','Lợi','Trí','Đạt','An','Ngân','Linh','Thảo']
khoa=['KH&KTTT','CNPM','KHMT','KTMT','MMT&TT','HTTT']
hocvi=['CN','KS','ThS','TS','PGS','GS']
hsl={'CN':2.34,'KS':2.34,'ThS':2.69,'TS':3.95,'PGS':5,'GS':9}
def Capnhathethong(list_gv,list_sv,list_mh,list_bd):
    for gv in list_gv:
        gv.hesoluong=hsl[gv.hocvi]
        gv.thunhap=gv.hesoluong*1350000+8000000
    for sv in list_sv:
        sum=0
        count=0
        sumtl=0
        counttl=0
        for bd in list_bd:
            if sv.mssv==bd.mssv:
                sum+=bd.diem
                count+=1
            for mh in list_mh:
                if mh.mamon==bd.mamon:
                    sumtl+=bd.diem*mh.sotinchi
                    counttl+=mh.sotinchi
        if count!=0: 
            sv.diemtrungbinh=sum/count
        if counttl!=0:
            sv.diemtichluy=sumtl/counttl

    print('Cập nhật thành công')

    
def Taosinhvien(list_sv):
    list_sv.append(SinhVien(input('Nhập mssv: '),input('Nhập họ tên:'),input('Nhập khoa:')))
    print('Tạo thành công')
def Xoasinhvien(list_sv):
    mssv=input('Nhập mssv cần xóa:')
    for sv in list_sv:
        if sv.mssv==mssv:
            list_sv.remove(sv)
    print('Xóa thành công')
def Taogiangvien(list_gv):
    id=input('Nhập mã giảng viên:')
    hoten=input('Nhập họ tên gv:')
    fac=input('Nhập khoa:')
    hv=input('Nhập học vị:')
    list_gv.append(GiangVien(id,hoten,fac,hv))
    print('Tạo thành công')
def Xoagiangvien(list_gv):
    mgv=input('Nhập mã gv cần xóa:')
    for gv in list_gv:
        if gv.mgv==mgv:
            list_gv.remove(gv)
    print('Xóa thành công')
def Taomonhoc(list_mh):
    mmh=input('Nhập mã môn học:')
    tmh=input('Nhập tên môn học:')
    stc=input('Nhập số tín chỉ:')
    list_mh.append(MonHoc(mmh,tmh,stc))
    print('Tạo thành công')
def Xoamonhoc(list_mh):
    mmh=input('Nhập mã môn học cần xóa: ')
    for mh in list_mh:
        if mh.mamon==mmh:
            list_mh.remove(mh)
    print('Xóa thành công')
def Capnhatbangdiem(list_bd):
    mssv=input('Nhập mssv:')
    ml=input('Nhập mã lớp:')
    mgv=input('Nhập mã giáo viên:')
    diem=input('Nhập số điểm:')
    for bd in list_bd:
        if bd.malop==ml and bd.magv==mgv and bd.mssv==mssv:
            bd.diem=diem
            print('Cập nhật thành công')
            return
    print('Thông tin cung cấp không chính xác')
        
def Locsinhvien(list_sv):
    x=float(input('Nhập x:'))
    for sv in list_sv:
        if sv.diemtichluy > x:
            print(sv.hoten)
def Xuatsinhvien(list_sv):
    mssv=input('Nhập mssv:')
    for sv in list_sv:
        if sv.mssv==mssv:
            print('Họ tên:',sv.hoten)
            print('Khoa:',sv.khoa)
            print('TBC:',sv.diemtrungbinh)
            print('TBTL:',sv.diemtichluy)
            return
    print('mssv không tồn tại')
def Callmenu():
    print("###################    MENU    ####################")
    print('1. Cập nhật toàn hệ thống')
    print('2. Tạo thêm 1 sinh viên')
    print('3. Xóa sinh viên')
    print('4. Tạo thêm 1 giảng viên')
    print('5. Xóa giảng viên')
    print('6. Tạo môn học mới')
    print('7. Xóa môn học')
    print('8. Cập nhật điểm')
    print('9. Lọc sinh viên có trung bình > x')
    print('10. Xuất thông tin sinh viên')
    #Xu li
    select=str(input('Mời chọn chức năng: '))
    if '1'==select:
        Capnhathethong(list_gv,list_sv,list_mh,list_bd)
        Callmenu()
    elif '2'==select:
        Taosinhvien(list_sv)
        Callmenu()
    elif '3'==select:
        Xoasinhvien(list_sv)
        Callmenu()
    elif '4'==select:
        Taogiangvien(list_gv)
        Callmenu()
    elif '5'==select:
        Xoagiangvien(list_gv)
        Callmenu()
    elif '6'==select:
        Taomonhoc(list_mh)
        Callmenu()
    elif '7'==select:
        Xoamonhoc(list_mh)
        Callmenu()
    elif '8'==select:
        Capnhatbangdiem(list_bd)
        Callmenu()
    elif '9'==select:
        Locsinhvien(list_sv)
        Callmenu()
    elif '10'==select:
        Xuatsinhvien(list_sv)
        Callmenu()
    else:
        print('Không tồn tại mục này')
        Callmenu()
########################################################
if __name__=='__main__':
    list_sv=[]
    list_gv=[]
    list_mh=[]
    list_bd=[]
    #Khoi tao 1500 sinh vien va 50 giang vien
    for i in range(1,1501,1):
        temp_id='2152'+str(i).zfill(4)
        temp_hoten=random.choice(ho)+' '+random.choice(lot)+' '+random.choice(ten)
        temp_fac=random.choice(khoa)
        list_sv.append(SinhVien(temp_id, temp_hoten, temp_fac))
    for i in range(1,51,1):
        temp_id='80'+str(i).zfill(4)
        temp_hoten=random.choice(ho)+' '+random.choice(lot)+' '+random.choice(ten)
        temp_fac=random.choice(khoa)
        temp_hocvi=random.choice(hocvi)
        list_gv.append(GiangVien(temp_id, temp_hoten, temp_fac, temp_hocvi)) 
    #Khoi tạo 10 môn học
    for i in range(1,11,1):
        list_mh.append(MonHoc('IT'+str(i).zfill(3),'Môn học số '+str(i),random.choice([2,3,4])))
    #Khoi tao 6000 bang diem
    mgvs=[gv.mgv for gv in list_gv]
    mssvs=[sv.mssv for sv in list_sv]
    idcourses=[course.mamon for course in list_mh]
    classes='C'+str(random.randrange(1,1000,1))
    for i in range(1,6001,1):
        list_bd.append(BangDiem('C'+str(random.randrange(1,1000,1)),random.choice(mgvs),random.choice(idcourses),random.choice(mssvs), random.randrange(0,10,1)))
    #Call menu
    Callmenu()
    ###########################################################
    #Xay dung menu


