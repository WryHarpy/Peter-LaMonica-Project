#This code was written by John Hayes, Evan Roberts, and Nicholas Demanche.
#If your Python is marked as havving 100+ problems, it is because it considers many of the Tkinter parts as going unused.
import PLPDegreePaths
from tkinter import *
from tkinter import filedialog
#Calls The main screen
root = Tk()

root.title("Student Course Prediction Program")
#Degree Path Screen.
def DegreePath():
    temp= open("CoursePrint.txt", "a")
    open("CoursePrint.txt", 'w').close()
    #Displays the Computer Science Courses
    def cisDisplay():
        for x in PLPDegreePaths.computerScienceInnovation:
            temp.writelines(x+'\n')
            for y in PLPDegreePaths.computerScienceInnovation[x]:
                temp2 = (y + ': '+ PLPDegreePaths.computerScienceInnovation[x][y]+'\n')
                temp.writelines(str(temp2))
        temp.close()
        def cisPrint():
            lines=open("CoursePrint.txt","r")
            data = lines.read()
            cisCourses = Label(top, text = data)
            cisCourses.pack()
        cisPrint()
    #Displays the Cloud Services Courses
    def cloudServiceDisplay():
        for x in PLPDegreePaths.cloudServices:
            temp.writelines(x+'\n')
            for y in PLPDegreePaths.cloudServices[x]:
                temp2 = (y + ': '+ PLPDegreePaths.cloudServices[x][y]+'\n')
                temp.writelines(str(temp2))
        temp.close()
        def clsPrint():
            lines=open("CoursePrint.txt","r")
            data = lines.read()
            cisCourses = Label(top, text = data)
            cisCourses.pack()
        clsPrint()
    #Displays the Cyber Security courses
    def cyberSecurityDisplay():
        for x in PLPDegreePaths.cyberSecurity:
            temp.writelines(x+'\n')
            for y in PLPDegreePaths.cyberSecurity[x]:
                temp2 = (y + ': '+ PLPDegreePaths.cyberSecurity[x][y]+'\n')
                temp.writelines(str(temp2))
        temp.close()
        def cysPrint():
            lines=open("CoursePrint.txt","r")
            data = lines.read()
            cisCourses = Label(top, text = data)
            cisCourses.pack()
        cysPrint()
    #This is the Tkinter Code for the Course Display screen, it calls the buttons and details
    top = Toplevel()
    top.title('Degree Path Viewer')
    titleText = Label(top, font="Verdana 24",text="Please select a degree path to view.")
    subtitleText = Label(top, font="Verdana 16",text="Once you view a path, you must return or re-open the window to do another.")
    CSI = Button(top, font="Verdana 16",text = "Computer Science and Innovation", bg="Grey",command=cisDisplay)
    cloudService=Button(top, font="Verdana 16",text = "Cloud Services IT",bg="White" ,command=cloudServiceDisplay)
    cyberSecurity=Button(top, font="Verdana 16",text = "Cyber Security", bg="Grey",command=cyberSecurityDisplay)
    returnbutton = Button(top, font="Verdana 16",text="Return to start screen.", bg="White",command=top.destroy)
    titleText.pack()
    subtitleText.pack()
    CSI.pack()
    cloudService.pack()
    cyberSecurity.pack()
    returnbutton.pack()
    topframe = LabelFrame(top,padx=5,pady=5)
    topframe.pack(padx=10,pady=10)

#Course Prediction Screen.
def CoursePrediction():
    top = Toplevel()
    studentEntry=Entry(top, width=100)
    courseEntry=Entry(top, width=100)
    #This grabs the directory for the student CSV file.
    def studentFile():
        root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select Student List CSV File",filetypes = (("CSV files","*.csv"),("all files","*.*")))
        studentEntry.insert(0, root.filename)
    #This grabs the directory for the course CSV file.
    def courseFile():
        root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select Course List CSV File",filetypes = (("CSV files","*.csv"),("all files","*.*")))
        courseEntry.insert(0, root.filename)
    #This is the start of the student course number comparison.
    def dataComparison():
            #This part skims through the student data to grab only the tech courses.
            with open(studentEntry.get(), 'r') as oldfile, open('studentfile1.txt','w') as newfile:
                tripWords = ['ENGL','INT','MATH','PHIL','PSYC','HIST','ESCI']
                tripList = ['A0']
                for line in oldfile:
                    if any(tripList in line for tripList in tripList):
                        tripWords = ['ENGL','INT','MATH','PHIL','PSYC','HIST','ESCI']
                    if not any(tripWords in line for tripWords in tripWords):
                        newfile.write(line)
                        tripWords.append(line[23:31])
            #This part checks if the student is passing the courses left behind and removes the failed courses, it then converts the student ID lines into strings of asterisks.
            with open('studentfile1.txt', 'r') as oldfile, open('studentfile2.txt','w') as newfile:
                tripWords = ['CIS','CYBD','CSIT','CSCN']
                tripList = ['A0']
                failingGrade = [',D,',',F,']
                for line in oldfile:
                        if any(tripList in line for tripList in tripList):
                            newfile.write('\n'+'*'* 20)
                        if any(tripWords in line for tripWords in tripWords):
                            if not any(failingGrade in line for failingGrade in failingGrade):
                                newfile.write('\n'+ line[23:31])
            #This section cleans up the data and leaves behind only the bare essentials ex: CIS210 CYBD220 etc.
            with open('studentfile2.txt', 'r') as newerfile, open ('studentData.txt', 'w') as studentData:
                temp = newerfile.read()
                temp=temp.replace(",","")
                studentData.write(temp)
            #This part cleans up the course data csv file for later use.
            with open (courseEntry.get(), 'r') as courseTemp, open ('courseFixed.txt','w') as courseData:
                temp = courseTemp.read()
                temp=temp.replace("M","")
                temp=temp.replace("(","")
                temp=temp.replace(")","")
                temp=temp.replace(",","")
                courseData.write(temp)
            courseDataHolder = []
            tripListTwo=['********************']
            with open('courseFixed.txt', 'r') as dataTest:
                for line in dataTest:
                    courseDataHolder.append(line)
                    courseDataHolder=([s.strip('\n') for s in courseDataHolder])
            #This part converts the course list into a dictionary that allows the courses to have storable values.
            studentDict = {i : 0 for i in courseDataHolder}
            tempDict = studentDict.copy()
            #This is the data comparison part, it spits out a print of the dictionary with numbers relating to the number of students that need to take that course.
            with open('studentData.txt', 'r') as studentData:
                counter = 0
                for line in studentData:
                    if any(tripListTwo in line for tripListTwo in tripListTwo):
                        counter = counter + 1
                    else:
                        temp = (line.strip('\n'))
                        tempDict[temp] = tempDict.get(temp,0) + 1
            #This gives the final value of the students.
            for element in studentDict:
                studentDict[element] = counter - tempDict.get(element)
            finalOutcome = Label(top, font="Verdana 16",text = studentDict)
            finalOutcome.pack()
            #This part writes the dictionary to a txt file.
            with open('courseDataComparison.txt','w') as finalComparison:
                    finalComparison.write(str(studentDict))
    #Comparison screen window code.
    top.title('Course Prediction System')
    titleText = Label(top, font="Verdana 18",text="Select two files, one for student data, and one for courses, to make a comparison for numbers.")
    studentDatabutton = Button(top, font="Verdana 16",text="Select a CSV file of student data.", command=studentFile)
    courseListbutton = Button(top, font="Verdana 16",text="Select a CSV file of course lists.", command=courseFile)
    comparebutton= Button(top,font="Verdana 16",text="Compare the list of student data to the course list.", command=dataComparison)
    returnbutton = Button(top, font="Verdana 16",text="Close window and return to start screen.", command=top.destroy)
    titleText.pack()
    studentDatabutton.pack()
    studentEntry.pack()
    courseListbutton.pack()
    courseEntry.pack()
    comparebutton.pack()
    returnbutton.pack()
    topframe = LabelFrame(top,padx=5,pady=5)
    topframe.pack(padx=10,pady=10)

#Starting page Screen
def StartScreen():
    programTitle = Label(root, font="Verdana 24" ,text ="Student Course Prediction Program")
    creditSubtitle = Label(root, font="Verdana 16" ,text ="Created by John Hayes, Evan Roberts, and Nicholas Demanche.")
    bottomText = Label(root,font="Verdana 16 italic" ,text ="CIS 291 Spring Semester 2020")
    bottomText2 = Label(root,font="Verdana 16 italic" ,text ="Created for Peter LaMonica")
    degreePathButton = Button(root, height=5, width=35 ,font="Verdana 16",text= "Click to View Degree Paths" ,fg="Black", bg="White", command= DegreePath)
    studentCourseButton = Button(root, height=5, width=35,font="Verdana 16",text= "Click to Predict a Students's Next Semester", fg="Black", bg="Grey",command=CoursePrediction)
    exit_Button = Button(root, height=5, width=35, font="Verdana 16" ,text="Close Program", bg="White" ,command=root.quit)
    programTitle.pack()
    creditSubtitle.pack()
    degreePathButton.pack()
    studentCourseButton.pack()
    exit_Button.pack()
    bottomText.pack()
    bottomText2.pack()
StartScreen()
root.mainloop()
