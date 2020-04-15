import PLPDegreePaths
from tkinter import *
from tkinter import filedialog
root = Tk()

root.title("Student Course Prediction Program")

'''
    e = Entry(root)
    e.pack()
    e.insert(0, "Enter Your Name: ")
'''
#Degree Path Screen.
def DegreePath():
    temp= open("temp.txt", "a")
    open("temp.txt", 'w').close()
    def cisDisplay():
        for x in PLPDegreePaths.computerScienceInnovation:
            #print (x)
            temp.writelines(x+'\n')
            for y in PLPDegreePaths.computerScienceInnovation[x]:
                #print (y, ':', PLPDegreePaths.computerScienceInnovation[x][y])
                temp2 = (y + ': '+ PLPDegreePaths.computerScienceInnovation[x][y]+'\n')
                temp.writelines(str(temp2))
        temp.close()
        def cisPrint():
            lines=open("temp.txt","r")
            data = lines.read()
            #print(data)
            cisCourses = Label(top, text = data)
            cisCourses.pack()
        cisPrint()
    def cloudServiceDisplay():
        for x in PLPDegreePaths.cloudServices:
            #print (x)
            temp.writelines(x+'\n')
            for y in PLPDegreePaths.cloudServices[x]:
                #print (y, ':', PLPDegreePaths.computerScienceInnovation[x][y])
                temp2 = (y + ': '+ PLPDegreePaths.cloudServices[x][y]+'\n')
                temp.writelines(str(temp2))
        temp.close()
        def clsPrint():
            lines=open("temp.txt","r")
            data = lines.read()
            #print(data)
            cisCourses = Label(top, text = data)
            cisCourses.pack()
        clsPrint()
    def cyberSecurityDisplay():
        for x in PLPDegreePaths.cyberSecurity:
            #print (x)
            temp.writelines(x+'\n')
            for y in PLPDegreePaths.cyberSecurity[x]:
                #print (y, ':', PLPDegreePaths.computerScienceInnovation[x][y])
                temp2 = (y + ': '+ PLPDegreePaths.cyberSecurity[x][y]+'\n')
                temp.writelines(str(temp2))
        temp.close()
        def cysPrint():
            lines=open("temp.txt","r")
            data = lines.read()
            #print(data)
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
        def dataPartone():
            tripWords = ['ENGL', 'INT','MATH','PHIL','PSYC','HIST','ESCI','A0']
            with open(studentEntry.get(), 'r') as oldfile, open('newfile.txt','w') as newfile:
                for line in oldfile:
                    if not any(tripWords in line for tripWords in tripWords):
                        newfile.write(line)
            temp = open('newfile.txt', 'r')
            studentData=temp.read()
            print(studentData)
        dataPartone()
        test2 =open(courseEntry.get(), 'r')
        courseData = test2.read()
        #print(courseData)
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
