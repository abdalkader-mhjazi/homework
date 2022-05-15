#تعريف القائمة
graduated_students = ['Salam','mohammed','zena','sahar','ali']
#إدخال اسم الطالب
name = input("Enter  name: ")
#اختبار إذا كان الطالب متخرج
if name in graduated_students:
    print(name,"is graduated")
else:
    print(name,"isn't graduated")
    
    
    