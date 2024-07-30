import datetime

import face_recognition
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from myapp.models import *


def login(request):
    return render(request,'loginindex.html')
def login_post(request):
    username=request.POST['textfield']
    password=request.POST['textfield2']
    login_data=Login.objects.filter(username=username,password=password)
    if login_data.exists():
        lg=Login.objects.get(username=username,password=password)
        request.session['lid']=lg.id
        if lg.type == 'admin':
            return HttpResponse('''<script>alert('welcome home');window.location='/myapp/adminhome/'</script>''')
        elif lg.type == 'student':
            return HttpResponse('''<script>alert('welcome home');window.location='/myapp/studenthome/'</script>''')
        else:
            return HttpResponse('''<script>alert('invalid username and password');window.location='/myapp/login/'</script>''')
    else:
        return HttpResponse('''<script>alert('invalid username and password');window.location='/myapp/login/'</script>''')


def changepassword(request):
    return render(request,'admin/changepassword.html')
def changepassword_post(request):
    curenntpassword=request.POST['textfield']
    changepassword=request.POST['textfield2']
    confirmpassword=request.POST['textfield3']
    chps=Login.objects.get(id=request.session['lid'],password=curenntpassword)
    if changepassword==confirmpassword:
        newps=Login.objects.filter(id=request.session['lid']).update(password=confirmpassword)
        return HttpResponse('''<script>alert('password succesfully changed');window.location='/myapp/login/'</script>''')
    else:
        return HttpResponse('''<script>alert('password missmatched');window.location='/myapp/changepassword/'</script>''')



def adddepartment(request):
    return render(request,'admin/adddepartment.html')



def adddepartment_post(request):
    departmentname=request.POST['textfield']
    dp=Department()
    dp.DepartmentName=departmentname
    dp.save()
    return  HttpResponse('''<script>alert('dep added');window.location='/myapp/adminhome/'</script>''')


def viewdepartment(request):
    vd=Department.objects.all()
    return render(request,'admin/viewdepartment.html',{'data':vd})

def viewdepartment_post(request):
    search=request.POST['textfield']
    vd=Department.objects.filter(DepartmentName__icontains=search)
    return render(request,'admin/viewdepartment.html',{'data':vd})


def editdepartment(request,id):
    dobj=Department.objects.get(id=id)
    return render(request,'admin/editdepartment.html',{'data':dobj})

def editdepartment_post(request):
    id=request.POST['id']
    editdepartmentname=request.POST['textfield']
    dp = Department.objects.get(id=id)
    dp.DepartmentName = editdepartmentname
    dp.save()
    return  HttpResponse('''<script>alert(' added');window.location='/myapp/viewdepartment/'</script>''')

def addcourse(request):
    dp=Department.objects.all()
    return render(request,'admin/addcourse.html',{'data':dp})
def addcourse_post(request):
    department=request.POST['select']
    coursename=request.POST['textfield']
    totalsemester=request.POST['textfield2']
    ac=Course()
    ac.DEPARTMENT_id=department
    ac.CourseName=coursename
    ac.TotalSem=totalsemester
    ac.save()
    return  HttpResponse('''<script>alert('course added');window.location='/myapp/adminhome/'</script>''')


def viewcourse(request):
    vc=Course.objects.all()
    return render(request,'admin/viewcourse.html',{'data':vc})

def viewcourse_post(request):
    search = request.POST['textfield']
    vc=Course.objects.filter(CourseName__icontains=search)

    return render(request,'admin/viewcourse.html',{'data':vc})


def editcourse(request,id):
    dobj =Course.objects.get(id=id)
    dp=Department.objects.all()
    return render(request,'admin/editcourse.html',{'data': dobj,'data1':dp})

def editcourse_post(request):
    id=request.POST['id']
    dpt=request.POST['dpt']
    coursename=request.POST['textfield']
    totalsemester=request.POST['textfield2']
    cs=Course.objects.get(id=id)
    cs.TotalSem=totalsemester
    cs.DEPARTMENT=Department.objects.get(id=dpt)
    cs.CourseName=coursename
    cs.save()
    return  HttpResponse('''<script>alert(' added');window.location='/myapp/viewcourse/'</script>''')

def addsubject(request):
    cu=Course.objects.all()
    return render(request,'admin/addsubject.html',{'data':cu})
def addsubject_post(request):
    course=request.POST['select']
    subject=request.POST['textfield']
    semester=request.POST['textfield2']

    asb=Subject()
    asb.COURSE_id=course
    asb.SubjectName=subject
    asb.Semester=semester
    asb.save()


    return  HttpResponse('''<script>alert('subject added');window.location='/myapp/adminhome/'</script>''')

def viewsubject(request):
    cu=Subject.objects.all()
    c = Course.objects.all()
    return render(request,'admin/viewsubject.html',{'data':cu,'c':c})

def viewsubject_post(request):
    search = request.POST['textfield']
    semester= request.POST["semester"]
    course= request.POST["course"]

    if request.POST["button"] =="Search":

        cu=Subject.objects.filter(SubjectName__icontains=search)
        c=Course.objects.all()
        return render(request,'admin/viewsubject.html',{'data':cu,'c':c})
    else:
        cu=Subject.objects.filter(COURSE_id=course,Semester=semester)
        c=Course.objects.all()
        return render(request,'admin/viewsubject.html',{'data':cu,'c':c})


def editsubject(request,id):
    es=Subject.objects.get(id=id)
    sc=Course.objects.all()

    return render (request,'admin/editsubject.html',{'data':sc,'data1':es})


def editsubject_post(request):
    id=request.POST['id']
    course=request.POST['select']
    subject = request.POST['textfield']
    semester = request.POST['textfield2']
    esb=Subject.objects.get(id=id)

    esb.COURSE_id=course
    esb.SubjectName=subject
    esb.Semester=semester
    esb.save()

    return  HttpResponse('''<script>alert(' added');window.location='/myapp/viewsubject/'</script>''')

def addstudent(request):
    res=Course.objects.all()
    return render(request,'admin/addstudent.html',{"data":res})
def addstudent_post(request):

    name=request.POST['textfield']
    pin=request.POST['textfield2']
    post=request.POST['textfield3']
    email=request.POST['textfield9']
    phone=request.POST['textfield4']
    gender=request.POST['radio']
    housename=request.POST['textfield5']
    place=request.POST['textfield6']
    parentname=request.POST['textfield7']
    parentphone=request.POST['textfield8']
    dob=request.POST['textfield1']
    sem=request.POST['radio1']
    image=request.FILES['filefield']
    course=request.POST['select']

    lobj=Login()
    lobj.username=email
    lobj.password=phone
    lobj.type='student'
    lobj.save()
    sobj=Student()
    sobj.Name=name
    sobj.Gender=gender
    sobj.Sem=sem
    sobj.Pin=pin
    sobj.Post=post
    sobj.Phone=phone
    sobj.HouseName=housename
    sobj.Place=place
    sobj.ParentName=parentname
    sobj.ParentPhone=parentphone
    sobj.DOB=dob
    sobj.Email=email
    sobj.COURSE_id=course
    import datetime
    fs=FileSystemStorage()
    date=datetime.datetime.now().strftime("%Y%m%d-%H%M%S")+".jpg"
    fs.save(date,image)
    path=fs.url(date)
    sobj.Image=path
    sobj.LOGIN=lobj
    sobj.save()

    return HttpResponse('''<script>alert(' added');window.location='/myapp/viewstudent/'</script>''')

def viewstudent(request):
    res=Student.objects.all()

    c=Course.objects.all()


    return render(request,'admin/viewstudent.html',{"data":res,'c':c})

def viewstudent_post(request):
    search = request.POST['textfield']
    semester = request.POST['semester']
    course = request.POST['course']
    search = request.POST['textfield']

    c = Course.objects.all()
    if request.POST["s"]=="Search":

        res=Student.objects.filter(Name__icontains=search)
        return render(request,'admin/viewstudent.html',{"data":res,'c':c})
    else:
        res=Student.objects.filter(COURSE_id=course,Sem=semester)
        return render(request,'admin/viewstudent.html',{"data":res,'c':c})


def editstudent(request,id):
    es=Course.objects.all()
    ot=Student.objects.get(id=id)
    return render(request,'admin/editstudent.html',{"data":es ,"data1":ot})


def editstudent_post(request):
    id = request.POST['id']
    name = request.POST['textfield']
    pin = request.POST['textfield2']
    post = request.POST['textfield3']
    email = request.POST['textfield9']
    phone = request.POST['textfield4']
    gender = request.POST['radio']
    sem = request.POST['radio1']
    housename = request.POST['textfield5']
    place = request.POST['textfield6']
    parentname = request.POST['textfield7']
    parentphone = request.POST['textfield8']
    dob = request.POST['textfield1']

    course = request.POST['select']
    sobj = Student.objects.get(id=id)




    if 'filefield' in request.FILES:
        image = request.FILES['filefield']

        import datetime
        fs = FileSystemStorage()
        date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
        fs.save(date, image)
        path = fs.url(date)
        sobj.Image = path
        sobj.save()

    sobj.Name = name
    sobj.Gender = gender
    sobj.Pin = pin
    sobj.Sem=sem
    sobj.Post = post
    sobj.Phone = phone
    sobj.HouseName = housename
    sobj.Place = place
    sobj.Email=email
    sobj.ParentName = parentname
    sobj.ParentPhone = parentphone
    sobj.DOB = dob
    sobj.COURSE_id = course

    sobj.save()

    return HttpResponse('''<script>alert(' added');window.location='/myapp/viewstudent/'</script>''')

def addtimetable(request):
    rec=Subject.objects.all()
    return render(request,'admin/addtimetable.html',{"data":rec})
def addtimetable_post(request):
    hour = request.POST['textfield2']
    day = request.POST['textfield']
    sub=request.POST['select']
    tobj=Timetable()
    tobj.SUBJECT_id=sub
    tobj.Day=day
    tobj.Hour=hour
    tobj.save()

    return HttpResponse('''<script>alert(' added');window.location='/myapp/viewtimetable/'</script>''')

def viewtimetable(request):
    res=Timetable.objects.all()
    rsr=Subject.objects.all()

    return render(request,'admin/viewtimetable.html',{"data":res,'data1':rsr})

def viewtimetable_post(request):
    search = request.POST['select']
    rsr=Subject.objects.all()
    res=Timetable.objects.filter(SUBJECT_id=search)
    return render(request,'admin/viewtimetable.html',{"data":res,'data1':rsr})


def edittimetable(request,id):
    rec=Subject.objects.all()
    res=Timetable.objects.get(id=id)
    return render(request,'admin/edittimetable.html',{"data":rec,"data1":res})


def edittimetable_post(request):
    hour = request.POST['textfield2']
    day = request.POST['textfield']
    sub = request.POST['select']
    id=request.POST['id']
    tobj = Timetable.objects.get(id=id)
    tobj.SUBJECT_id = sub
    tobj.Day = day
    tobj.Hour = hour
    tobj.save()

    return HttpResponse('''<script>alert(' added');window.location='/myapp/viewtimetable/'</script>''')

def attendancereport(request):
    res = Attendance.objects.all()
    return render(request,'admin/attendancereport.html',{'data':res})

def adminhome(request):
    return render(request,'admin/adminindex.html')

def searchbyphoto(request):
    spt = request.FILES['searchbyphoto']

    foundid=""


    fs = FileSystemStorage()
    import datetime
    date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
    fs.save(date, spt)
    path = fs.url(date)

    knownimage = []
    knownids = []
    knownpersonlandmark = []

    l = Student.objects.all()
    for i in l:
        s = "C:\\Users\\Administrator\\PycharmProjects\\facerecognition"
        m = s + i.Image
        print(m)

        picture_of_me = face_recognition.load_image_file(m)
        my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

        print(my_face_encoding)
        knownimage.append(my_face_encoding)
        knownids.append(i.id)

    picture_of_post = face_recognition.load_image_file(
        "C:\\Users\\Administrator\\PycharmProjects\\facerecognition\\media\\" + date)

    others_face_encoding = face_recognition.face_encodings(picture_of_post)

    totface = len(others_face_encoding)
    print(totface)
    for i in range(0, totface):
        res = face_recognition.compare_faces(knownimage, others_face_encoding[i], tolerance=0.5)
        print(res)


        for i in range(0,len(res)):
            if res[i]== True:
                foundid=knownids[i]
                break


    # knownids.append(i['id'])

        # sid = 13
    if foundid=="":
        return HttpResponse('''<script>alert(' no data');window.location='/myapp/adminhome/'</script>''')



    sid=foundid
    res=Student.objects.get(id=sid)
    res2=Attendance.objects.filter(STUDENT_id=sid)
    ttlabsent=0
    ttlpresent=0
    for i in res2:
        if i.Attendance=='Absent':
            ttlabsent=ttlabsent+1
        else :
            ttlpresent=ttlpresent+1

    return render(request,'admin/SearchByPhoto.html',{'data':res,'data2':res2,'ttlabsent':str(ttlabsent),'ttlpresent':str(ttlpresent),'sid':sid})

def searchbyphoto_post_month(request):
    sid = request.POST['sid']
    month = request.POST['month']
    # sid = 13
    res = Student.objects.get(id=sid)
    res2 = Attendance.objects.filter(STUDENT_id=sid, Date__month=month)
    ttlabsent = 0
    ttlpresent = 0
    for i in res2:
        if i.Attendance == 'Absent':
            ttlabsent = ttlabsent + 1
        else:
            ttlpresent = ttlpresent + 1

    return render(request, 'admin/SearchByPhoto.html',
                  {'data': res, 'data2': res2, 'ttlabsent': str(ttlabsent), 'ttlpresent': str(ttlpresent), 'sid': sid})

def searchbyphoto_post_date(request):
    sid = request.POST['sid']
    fdate = request.POST['fdate']
    tdate = request.POST['tdate']
    # sid = 13
    res = Student.objects.get(id=sid)
    res2 = Attendance.objects.filter(STUDENT_id=sid, Date__range=[fdate, tdate])
    ttlabsent = 0
    ttlpresent = 0
    for i in res2:
        if i.Attendance == 'Absent':
            ttlabsent = ttlabsent + 1
        else:
            ttlpresent = ttlpresent + 1

    return render(request, 'admin/SearchByPhoto.html',
                  {'data': res, 'data2': res2, 'ttlabsent': str(ttlabsent), 'ttlpresent': str(ttlpresent), 'sid': sid})


def deletedepartment(request,id):
    Department.objects.get(id=id).delete()
    return HttpResponse('''<script>alert(' deleted');window.location='/myapp/viewdepartment/'</script>''')

def deletecourse(request,id):
    Course.objects.get(id=id).delete()
    return HttpResponse('''<script>alert(' deleted');window.location='/myapp/viewcourse/'</script>''')

def deletesubject(request,id):
    Subject.objects.get(id=id).delete()
    return HttpResponse('''<script>alert(' deleted');window.location='/myapp/viewsubject/'</script>''')

def deletestudent(request,id):
    Student.objects.get(id=id).delete()
    return HttpResponse('''<script>alert(' deleted');window.location='/myapp/viewstudent/'</script>''')

def deletetimetable(request,id):
    Timetable.objects.get(id=id).delete()
    return HttpResponse('''<script>alert(' deleted');window.location='/myapp/viewtimetable/'</script>''')


################TUDENT

def studenthome(request):
    return render(request,'student/studentindex.html')

def stdchangepassword(request):
    return render(request,'student/stdchangepassword.html')
def stdchangepassword_post(request):
    curenntpassword=request.POST['textfield']
    changepassword=request.POST['textfield2']
    confirmpassword=request.POST['textfield3']
    chps=Login.objects.get(id=request.session['lid'],password=curenntpassword)
    if changepassword==confirmpassword:
        newps=Login.objects.filter(id=request.session['lid']).update(password=confirmpassword)
        return HttpResponse('''<script>alert('password succesfully changed');window.location='/myapp/login/'</script>''')
    else:
        return HttpResponse('''<script>alert('password missmatched');window.location='/myapp/stdchangepassword/'</script>''')

def viewprofile(request):
    res=Student.objects.get(LOGIN_id=request.session['lid'])
    return render(request,'student/viewprfile.html',{'data':res})

def stdattendancereport(request):
    stda=Attendance.objects.filter(STUDENT__LOGIN_id=request.session['lid'])
    ttlabsent = 0
    ttlpresent = 0
    for i in stda:
        if i.Attendance == 'Absent':
            ttlabsent = ttlabsent + 1
        else:
            ttlpresent = ttlpresent + 1
    return render(request,'student/stdattendancereport.html',{'data':stda,'ttlpresent':str(ttlpresent),'ttlabsent':str(ttlabsent)})

# def searchbyphoto(request):
#     spt=request.FILES['searchbyphoto']
#     fs = FileSystemStorage()
#     date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
#     fs.save(date, spt)
#     path = fs.url(date)
#     sbp=Student.objects.filter(Image=path)
#
#     return render(request,"admin/SearchByPhoto.html",{'data':sbp})







def sadm_view_timetable(request):
    res=Course.objects.all()
    return render(request, 'admin/view timetable 1.html',{'data':res})

def sadm_view_timetable_post(request):
    res=Course.objects.all()
    cls = request.POST['Course']
    sem = request.POST['dropdown2']
    Days=['Monday','Tuesday','Wednesday','Thursday','Friday']
    Day=[{0:['Monday','Tuesday','Wednesday','Thursday','Friday']}]
    tt = []
    # timet=timetable.objects.filter(DIVISION_id=div,CLASS_id=cls)
    for i in Days:
        Hour = [1, 2, 3, 4, 5]
        ss=[]
        for j in Hour:
            # if i.hour==1:
            if Timetable.objects.filter(SUBJECT__Semester=sem,Hour=j, Day=i).exists():
                timet= Timetable.objects.get(SUBJECT__Semester=sem,Hour=j, Day=i)
                ss.append(timet.SUBJECT.SubjectName)

                # m={'sub':timet.SUBJECT.subject_name}
            else:
                ss.append("free")
        ss.insert(0,i)
        tt.append(ss)

    print(tt,"full")

    return render(request, 'admin/view timetable @.html',{'data':res,'data2':tt,'i':1,'day':Days,'m':tt,'hr':Hour})
    # return render(request, 'subadmin/view timetable 1.html',{'data':res,'data2':tt,'i':1,'day':Days,'m':m,'hr':Hour})

def sadm_view_timetable_post1(request):
    res=Course.objects.all()
    cls = request.POST['Course']
    sem = request.POST['dropdown2']
    Days=['Monday','Tuesday','Wednesday','Thursday','Friday']
    Day=[{0:['Monday','Tuesday','Wednesday','Thursday','Friday']}]
    tt = []
    # timet=timetable.objects.filter(DIVISION_id=div,CLASS_id=cls)
    for i in Days:
        Hour = [1, 2, 3, 4, 5, 6, 7]
        ss=[]
        for j in Hour:
            # if i.hour==1:
            if Timetable.objects.filter(SUBJECT__Semester=sem,Hour=j, Day=i).exists():
                timet= Timetable.objects.get(SUBJECT__Semester=sem,Hour=j, Day=i)
                ss.append(timet.SUBJECT.SubjectName)

                # m={'sub':timet.SUBJECT.subject_name}
            else:
                ss.append("free")
        ss.insert(0,i)
        tt.append(ss)

    print(tt,"full")

    return render(request, 'admin/view timetable @.html',{'data':res,'data2':tt,'i':1,'day':Days,'m':tt,'hr':Hour})
    # return render(request, 'subadmin/view timetable 1.html',{'data':res,'data2':tt,'i':1,'day':Days,'m':m,'hr':Hour})

#
# def load_div_on_class_1(request):
#     cid=request.POST["cid"]
#     print(cid)
#     dd=division.objects.filter(CLASS_id=cid)
#     l=[]
#     for i in dd:
#         l.append({"id":i.id,"div":i.class_division})
#     print(l)
#     return JsonResponse({"data":l})




def view_attendence(request):
    if request.session['lid']=='':
        return redirect('/collegeapp/add_login/')

    course = Course.objects.all()
    yr = datetime.datetime.now().year


    return render(request,'admin/view_attendence_temp.html',{"d":course,'yr':yr})

def view_attendence_post(request):
    if request.session['lid']=='':
        return redirect('/collegeapp/add_login/')
    course = request.POST['select3']
    sem = request.POST['select']
    year = request.POST['year']
    month = request.POST['month']

    alldates= Attendance.objects.filter(STUDENT__Sem=sem,STUDENT__COURSE_id=course,Date__month=month,Date__year=year).order_by('Date')

    dates=[]
    q=[]
    for i in alldates:
        if i.Date not in dates:
            dates.append(i.Date)
            q.append(str(i.Date.day))


    allstudents=Student.objects.filter(COURSE_id=course,Sem=sem)

    ds=[]
    hours=[1,2,3,4,5]
    for i in allstudents:

        s=[]

        for j in dates:

            aft=0
            bfr=0


            for h in hours:

                rd= Attendance.objects.filter(STUDENT=i,Date=j,Hour=str(h),Attendance="Present")
                print(rd)
                if rd.exists():
                    if h<4:
                        bfr=bfr+1
                    else:
                        aft=aft+1


            s.append({'MRNG':bfr,'NOON':aft})

        ds.append({'student':i.Name, 'attendance': s })


    course = Course.objects.all()







    return render(request, 'admin/view_attendence_temp.html', {'data':ds,'d':course,'dates':q})


def gettotalsembycourseid(request,courseid):


    c=Course.objects.get(id=courseid).TotalSem

    print(c)

    return JsonResponse({'sem':c})
