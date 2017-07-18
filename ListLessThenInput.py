# Cho mot list, in ra danh sach cac phan tu cua list nho hon 1 so (ng.dung nhap)
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
print "This is list: a = ", a
num = int(raw_input("Enter number: "))
for i in a:
	if i < num:
		b.append(i)
print "They are numbers less than %d, b = " %num, b