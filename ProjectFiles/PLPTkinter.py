import PLPDegreePaths
from tkinter import *
from tkinter import filedialog
root = Tk()

root.title("Student Course Prediction Program")
#Degree Path Screen.
def DegreePath():
    temp= open("temp.txt", "a")
    open("temp.txt", 'w').close()
    def cisDisplay():
        for x in PLPDegreePaths.computerScienceInnovation:
            temp.writelines(x+'\n')
            for y in PLPDegreePaths.computerScienceInnovation[x]:
                temp2 = (y + ': '+ PLPDegreePaths.computerScienceInnovation[x][y]+'\n')
                temp.writelines(str(temp2))
        temp.close()
        def cisPrint():
            lines=open("temp.txt","r")
            data = lines.read()
            cisCourses = Label(top, text = data)
            cisCourses.pack()
        cisPrint()
    def cloudServiceDisplay():
        for x in PLPDegreePaths.cloudServices:
            temp.writelines(x+'\n')
            for y in PLPDegreePaths.cloudServices[x]:
                temp2 = (y + ': '+ PLPDegreePaths.cloudServices[x][y]+'\n')
                temp.writelines(str(temp2))
        temp.close()
        def clsPrint():
            lines=open("temp.txt","r")
            data = lines.read()
            cisCourses = Label(top, text = data)
            cisCourses.pack()
        clsPrint()
    def cyberSecurityDisplay():
        for x in PLPDegreePaths.cyberSecurity:
            temp.writelines(x+'\n')
            for y in PLPDegreePaths.cyberSecurity[x]:
                temp2 = (y + ': '+ PLPDegreePaths.cyberSecurity[x][y]+'\n')
                temp.writelines(str(temp2))
        temp.close()
        def cysPrint():
            lines=open("temp.txt","r")
            data = lines.read()
            cisCourses = Label(top, text = data)
            cisCourses.pack()
        cysPrint()
    top = Toplevel()
    top.title('Degree Path Viewer')
    titleText = Label(top, text="Please select a degree path to view.")
    subtitleText = Label(top, text="Once you view a path, you must return or re-open the window to do another.")
    CSI = Button(top, text = "Computer Science and Innovation", command=cisDisplay)
    cloudService=Button(top, text = "Cloud Services IT", command=cloudServiceDisplay)
    cyberSecurity=Button(top, text = "Cyber Security", command=cyberSecurityDisplay)
    returnbutton = Button(top, text="Return to start screen.", command=top.destroy)
    titleText.pack()
    subtitleText.pack()
    CSI.pack()
    cloudService.pack()
    cyberSecurity.pack()
    returnbutton.pack()
    topframe = LabelFrame(top, text="This is a test", padx=5,pady=5)
    topframe.pack(padx=10,pady=10)

#Course Prediction Screen.
def CoursePrediction():
    top = Toplevel()
    studentEntry=Entry(top, width=28)
    courseEntry=Entry(top, width=28)
    def studentFile():
        root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select Student List CSV File",filetypes = (("CSV files","*.csv"),("all files","*.*")))
        studentEntry.insert(0, root.filename)
    def courseFile():
        root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select Course List CSV File",filetypes = (("CSV files","*.csv"),("all files","*.*")))
        courseEntry.insert(0, root.filename)
    def dataComparison():
            with open(studentEntry.get(), 'r') as oldfile, open('newfile.txt','w') as newfile:
                tripWords = ['ENGL','INT','MATH','PHIL','PSYC','HIST','ESCI']
                tripList = ['A0']
                for line in oldfile:
                    if any(tripList in line for tripList in tripList):
                        tripWords = ['ENGL','INT','MATH','PHIL','PSYC','HIST','ESCI']
                    if not any(tripWords in line for tripWords in tripWords):
                        newfile.write(line)
                        tripWords.append(line[23:31])
            with open('newfile.txt', 'r') as oldfile, open('newerfile.txt','w') as newfile:
                tripWords = ['CIS','CYBD','CSIT','CSCN']
                tripList = ['A0']
                failingGrade = [',D,',',F,']
                for line in oldfile:
                        if any(tripList in line for tripList in tripList):
                            newfile.write('\n'+'*'* 20)
                        if any(tripWords in line for tripWords in tripWords):
                            if not any(failingGrade in line for failingGrade in failingGrade):
                                newfile.write('\n'+ line[23:31])
            with open('newerfile.txt', 'r') as newerfile, open ('studentData.txt', 'w') as studentData:
                temp = newerfile.read()
                temp=temp.replace(",","")
                studentData.write(temp)            
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
            #We need to convert the course list into a dictionary that allows the courses to have storable values.
            studentDict = {i : 0 for i in courseDataHolder}
            #print(studentDict)
            #The Final Stretch
            with open('studentData.txt', 'r') as studentData:
                courseDataHolder = []
                counter = 0
                for line in studentData:
                    if any(tripListTwo in line for tripListTwo in tripListTwo):
                        if courseDataHolder == []:
                            with open('courseFixed.txt', 'r') as dataTest:
                                for line in dataTest:
                                    courseDataHolder.append(line)
                                    courseDataHolder=([s.strip('\n') for s in courseDataHolder])
                                    counter = 0
                        else:
                            print(courseDataHolder)
                            for element in courseDataHolder:
                                studentDict[element] += 1
                            courseDataHolder = []
                        with open('courseFixed.txt', 'r') as dataTest:
                            for line in dataTest:
                                courseDataHolder.append(line)
                                courseDataHolder=([s.strip('\n') for s in courseDataHolder])
                                counter = 0
                    if any(courseDataHolder in line for courseDataHolder in courseDataHolder):
                        courseDataHolder.remove(courseDataHolder[counter])
                        counter = counter + 1     
            finalOutcome = Label(top, text = studentDict)
            finalOutcome.pack()
            #print(courseDataHolder)
            #print(dataTest)
    top.title('Course Prediction System')
    titleText = Label(top, text="Select two files, one for student data, and one for courses, to make a comparison for numbers.")
    studentDatabutton = Button(top, text="Select a CSV file of student data.", command=studentFile)
    courseListbutton = Button(top, text="Select a CSV file of course lists.", command=courseFile)
    comparebutton= Button(top,text="Compare the list of student data to the course list.", command=dataComparison)
    returnbutton = Button(top, text="Close window and return to start screen.", command=top.destroy)
    titleText.pack()
    studentDatabutton.pack()
    studentEntry.pack()
    courseListbutton.pack()
    courseEntry.pack()
    comparebutton.pack()
    returnbutton.pack()

#Starting page Screen
def StartScreen():
    programTitle = Label(root, text ="Student Course Prediction Program")
    programSubtitle = Label(root, text ="Placeholder GUI")
    degreePathButton = Button(root, text= "Click to View Degree Paths", fg="Black", bg="Pink", command= DegreePath)
    studentCourseButton = Button(root, text= "Click to Predict a Students's Next Semester", fg="Black", bg="Cyan",command=CoursePrediction)
    exit_Button = Button(root, text="Close Program", command=root.quit)
    programTitle.pack()
    programSubtitle.pack()
    degreePathButton.pack()
    studentCourseButton.pack()
    exit_Button.pack()
    frame = LabelFrame(root, text="This is a test", padx=50,pady=50)
    frame.pack(padx=150,pady=100)
StartScreen()
root.mainloop()
