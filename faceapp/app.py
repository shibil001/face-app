import cv2
import face_recognition

from DBConnection import Db


db=Db()
# Create your views here.

qry="SELECT * FROM `myapp_student` "
res= db.select(qry)


# print(res)



knownimage=[]
knownids=[]
knownsems=[]


for i in res:
    s=i["Image"]
    s=s.replace("/media/","")
    pth="C:\\Users\\Administrator\\PycharmProjects\\facerecognition\\media\\"+ s
    picture_of_me = face_recognition.load_image_file(pth)
    # print(pth)
    my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]
    # print(my_face_encoding)
    knownimage.append(my_face_encoding)
    knownids.append(i['id'])








# define a video capture object
vid = cv2.VideoCapture(0)



firsthour= (9,10)
second= (10,11)
third= (11,12)
forth= (13,14)
fifth= (14,15)
sixth= (15,20)





while(True):

    ret, frame = vid.read()

    cv2.imwrite("a.jpg",frame)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    picture_of_others = face_recognition.load_image_file("a.jpg")
    # print(pth)
    others_face_encoding = face_recognition.face_encodings(picture_of_others)

    totface=len(others_face_encoding)


    # print("aaaaa", totface)

    from datetime import datetime

    curh = float(str(datetime.now().time().hour) + "." + str(datetime.now().time().minute))

    # print(curh, "hgfhhgfgfghfghfgh")
    period=0
    if firsthour[0]<=  curh < firsthour[1]:
        period=1
    elif second[0]<= curh < second[1]:
        period=2
    elif third[0]<= curh < third[1]:
        period=3
    elif forth[0]<= curh < forth[1]:
        period=4
    elif fifth[0]<= curh < fifth[1]:
        period=5
    elif sixth[0]<= curh < sixth[1]:
        period=6

    # print(period)

    for i in range(0,totface):

        """
    
"""
        # print("inside check")
        res=face_recognition.compare_faces(knownimage,others_face_encoding[i],tolerance=0.45)
        # print(res,"helllo")
        l=0
        for j in res:
            if j==True:

                qry="SELECT * FROM `myapp_attendance` WHERE `date`=CURDATE() AND `STUDENT_id`='"+str(knownids[i])+"' AND `hour`='"+str(period)+"'"

                data= db.selectOne(qry)

                if data is None:

                    qry="INSERT INTO `myapp_attendance` (`date`,`hour`,`STUDENT_id`,Attendance,time) " \
                        "VALUES (CURDATE(),'"+str(period)+"','"+str(knownids[i])+"', 'Present',CURTIME())"
                    db.insert(qry)

            # else:
            #     if period>1 and period<7:
            #         qry1 = "SELECT * FROM `myapp_attendance` WHERE `date`=CURDATE() AND `STUDENT_id`='" + str(
            #             knownids[i]) + "' AND `hour`='" + str(period-1) + "'"
            #
            #         data1 = db.selectOne(qry1)
            #         if data1 is None:
            #             qry2 = "INSERT INTO `myapp_attendance` (`date`,`hour`,`STUDENT_id`, attendance) VALUES (CURDATE(),'" + str(
            #                 period-1) + "','" + str(knownids[i]) + "', 'Absent')"
            #             db.insert(qry2)

            l=l+1
        else:
            if period >1 and period<7:

                qry = "SELECT * FROM `myapp_student` WHERE id not in (SELECT STUDENT_id FROM myapp_attendance " \
                      "WHERE `date`=CURDATE() AND (HOUR=0 AND HOUR=1 AND HOUR=2 AND HOUR=3 AND HOUR=4 AND HOUR=5 ))"
                ret = db.select(qry)
                # print(ret)
                for j in ret:
                    if period==2:
                        qry1 = "SELECT * FROM `myapp_attendance` WHERE `date`=CURDATE() AND `STUDENT_id`='" + str(
                            j['id']) + "' AND `hour`='" + str(1) + "'"
                        res1 = db.selectOne(qry1)
                        if res1 is None:
                            qry2 = "INSERT INTO `myapp_attendance` (`date`,`hour`,`STUDENT_id`, attendance,time) VALUES (CURDATE(),'" + str(
                                1) + "','" + str(j['id']) + "', 'Absent')"
                            db.insert(qry2)

                    if period==3:

                        qry3 = "SELECT * FROM `myapp_attendance` WHERE `date`=CURDATE() AND `STUDENT_id`='" + str(
                            j['id']) + "' AND `hour`='" + str(2) + "'"
                        res3 = db.selectOne(qry3)
                        if res3 is None:
                            qry4 = "INSERT INTO `myapp_attendance` (`date`,`hour`,`STUDENT_id`, attendance,time) VALUES (CURDATE(),'" + str(
                                2) + "','" + str(j['id']) + "', 'Absent')"
                            db.insert(qry4)


                    if period==4:

                        qry5 = "SELECT * FROM `myapp_attendance` WHERE `date`=CURDATE() AND `STUDENT_id`='" + str(
                            j['id']) + "' AND `hour`='" + str(3) + "'"
                        res5 = db.selectOne(qry5)
                        if res5 is None:
                            qry6 = "INSERT INTO `myapp_attendance` (`date`,`hour`,`STUDENT_id`, attendance,time) VALUES (CURDATE(),'" + str(
                                3) + "','" + str(j['id']) + "', 'Absent')"
                            db.insert(qry6)



                    if period==5:
                        qry7 = "SELECT * FROM `myapp_attendance` WHERE `date`=CURDATE() AND `STUDENT_id`='" + str(
                            j['id']) + "' AND `hour`='" + str(4) + "'"
                        res7 = db.selectOne(qry7)
                        if res7 is None:
                            qry8 = "INSERT INTO `myapp_attendance` (`date`,`hour`,`STUDENT_id`, attendance,time) VALUES (CURDATE(),'" + str(
                               4) + "','" + str(j['id']) + "', 'Absent')"
                            db.insert(qry8)




                    if period==6:
                        qry9 = "SELECT * FROM `myapp_attendance` WHERE `date`=CURDATE() AND `STUDENT_id`='" + str(
                            j['id']) + "' AND `hour`='" + str(5) + "'"
                        res9 = db.selectOne(qry9)
                        if res9 is None:
                            qry10 = "INSERT INTO `myapp_attendance` (`date`,`hour`,`STUDENT_id`, attendance,time) VALUES (CURDATE(),'" + str(
                                5) + "','" + str(j['id']) + "', 'Absent',curtime())"
                            db.insert(qry10)









                            #
        #         data1 = db.selectOne(qry1)
        #         if data1 is None:
        #             qry2 = "INSERT INTO `myapp_attendance` (`date`,`hour`,`STUDENT_id`, attendance) VALUES (CURDATE(),'" + str(
        #                 period-1) + "','" + str(knownids[i]) + "', 'Absent')"
        #             db.insert(qry2)


vid.release()
# Destroy all the windows
cv2.destroyAllWindows()