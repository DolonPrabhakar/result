from csv import *
from tabulate import *
def stud_write():
    with open(r"E:\Student results\demo.csv","a",newline="") as obj1:
        w_obj1=writer(obj1,delimiter=",")
        while True:
            try:
                rno=int(input("Enter roll no.:"))
                name=input("Enter name:")
                clas=int(input("Enter your class in numbers:"))
                sec=input("Enter your section <A/B/C/D/NM/M/Comm>:")
                state=input("Is the student from Andhra Pradesh or Punjab <A/P>?:")
                term=input("Marks of term I or II?<I/II>:")
                m1=float(input("Enter your marks in English:"))
                m2=float(input("Enter your marks in Maths:"))
                m3=float(input("Enter your marks in Chemistry:"))
                m4=float(input("Enter your marks in Physics:"))
                m5=float(input("Enter your marks in Computer Science:"))
                if state in "Aa":
                    m6=float(input("Enter your marks in Telegu:"))
                elif state in "Pp":
                    m6=float(input("Enter your marks in Punjabi:"))
                else:
                    print("Please choose from Punjab or Andhra Pradesh")
                tmarks=(m1+m2+m3+m4+m5+m6)
                avg= tmarks/600
                perc= avg*100
                w_obj1.writerow([name,rno,clas,sec,state,m1,m2,m3,m4,m5,m6,tmarks,avg,perc,term])
                ch=input("Type Y or y if you wish to continue entering data:")
                if ch in "nN":
                    break
            except Exception as e:
                print("Input error",e)
def stud_read():
    with open(r"E:\Student results\demo.csv","r",newline="")as obj1:
        try:
            b=reader(obj1)
            print(tabulate(b,headers='firstrow',tablefmt="fancy_grid"))
        except Exception as e:
                print("Display error",e)
def read_listofP():
    with open(r"E:\Student results\demo.csv","r",newline="")as obj1:
        try:
            r_obj1=reader(obj1)
            for i in r_obj1:
                if i[4] in "Pp":
                    print(i[0])
        except Exception as e:
                print("Display error",e)
def read_listofAP():
    with open(r"E:\Student results\demo.csv","r",newline="")as obj1:
        try:
            r_obj1=reader(obj1)
            for i in r_obj1:
                if i[4] in "Aa":
                    print(i[0])
        except Exception as e:
                print("Display error",e)
def read_c():
    with open(r"E:\Student results\demo.csv","r",newline="")as obj1:
        try:
            r_obj1=reader(obj1)
            t_name=input("Enter name you want:")
            for i in r_obj1:
                if i[0]==t_name:
                    print(i)
        except Exception as e:
                print("Display error",e)
def cls_result():
    cls=input("Enter the class you desire the result for:")
    sec=input("Enter the section:")
    with open(r"E:\Student results\demo.csv","r",newline="")as obj1:
        r_obj1=reader(obj1)
        for i in r_obj1:
            if i[2]==cls and i[3]==sec:
                print(i)
def positions():
    cls=input("Enter  the class for positions:")
    with open(r"E:\Student results\demo.csv","r",newline="")as obj1:
        try:
            r_obj1=reader(obj1)
            res=[]
            print("The postions of class",cls,"are as follows:")
            for j in r_obj1:
                if j[2]==cls:
                    res.append(j[12])
            pos = res
            a=max(pos)
            pos.remove(a)
            b=max(pos)
            pos.remove(b)
            c=max(pos)
            pos.remove(c)
            for i in r_obj1:
                print("First postion is bagged with",a,"%")
                print("Second postion is bagged with",b,"%")
                print("Third postion is bagged with",c,"%")
        except Exception as e:
                print("Display error",e)
def grades():
    cls=input("Enter the class you desire the result for:")
    sec=input("Enter the section:")
    with open(r"E:\Student results\demo.csv","r",newline="")as obj1:
        r_obj1=reader(obj1)
        for i in r_obj1:
            if i[2]==cls and i[3]==sec:
                print(i[0],"---",i[11],"%")
                if float(i[12])>90:
                    print("Congratulations!!! You got A grade!")
                elif float(i[12])>=80:
                    print("Well done!! You got B grade!")
                elif float(i[12])>=70:
                    print("Good work!! You got C grade!")
                elif float(i[12])>=60:
                    print("Keep practicing more! You got D grade!")
                elif float(i[12])>=50:
                    print("Need more efforts! You got E grade!")
                elif float(i[12])>=40:
                    print("Keep putting your efforts! You got F grade!")
                elif float(i[12])<30:
                    print("Reappear")
while True:
    print(".----------------------------.")
    print("|==========MENU==============|")
    print(".----------------------------.")
    print("1. WRITE MARKS AND OTHER DATA")
    print("2. DISPLAY RESULTS OF ALL STUDENTS")
    print("3. LIST OF STUDENTS FROM PUNJAB")
    print("4. LIST OF STUDENTS FROM ANDHRA PRADESH")
    print("5. SEARCH A STUDENT")
    print("6. RESULT OF DESIRED CLASS")
    print("7. CLASS-WISE POSITIONS")
    print("8. GRADES")
    ch=int(input("Enter your choice:"))
    if ch==1:
        stud_write()
    elif ch==2:
        stud_read()
    elif ch==3:
        read_listofP()
    elif ch==4:
        read_listofAP()
    elif ch==5:
        read_c()
    elif ch==6:
        cls_result()
    elif ch==7:
        positions()
    elif ch==8:
        grades()
    else:
        print("Wrong option selected!!!")
    opt=input("Do you wish to continue with the program? <y/n>:")
    if opt in "Nn":
        break
