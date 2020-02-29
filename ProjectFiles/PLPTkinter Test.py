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
    top = Toplevel()
    top.title('Degree Path Viewer')
    titleText = Label(top, text="This is the screen where the three CS degree paths will be viewable.")
    returnbutton = Button(top, text="Return to start screen.", command=top.destroy)
    titleText.pack()
    returnbutton.pack()

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
    frame = LabelFrame(root, text="This is a test", padx=50,pady=50)
    frame.pack(padx=300,pady=200)
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
StartScreen()
root.mainloop()
