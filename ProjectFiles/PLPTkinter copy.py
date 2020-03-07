import PLPDegreePaths
from tkinter import *
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
    top.title('Course Prediction System')
    titleText = Label(top, text="This is the screen where the three Course Prediction System will be viewable.")
    returnbutton = Button(top, text="Return to start screen.", command=top.destroy)
    titleText.pack()
    returnbutton.pack()

#Starting page Screen
def StartScreen():
    programTitle = Label(root, text ="Student Course Prediction Program")
    programSubtitle = Label(root, text ="Placeholder GUI created by John Hayes")
    degreePathButton = Button(root, text= "Click to View Degree Paths", fg="Black", bg="Pink", command= DegreePath)
    studentCourseButton = Button(root, text= "Click to Predict a Students's Next Semester", fg="Black", bg="Cyan",command=CoursePrediction and Toplevel.quit)
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