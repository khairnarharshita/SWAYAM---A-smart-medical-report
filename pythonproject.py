from tkinter import *
import pandas as pd

root = Tk()  # Create an instance of Tkinter frame/window
root.title("SWAYAM")  # Title of window
root.geometry('800x800')  # Dimension of window
root.state('zoomed')  # Maximize window to full size


def prediction(inp, inp1, inp2, inp3):  # inp-observed, inp1-low, inp2-high, inp3-parameter
    df = pd.read_csv('ideal.csv')

    low_rem = df['Low remedies'].tolist()
    High_rem = df['High remedies'].tolist()
    low_dis = df['Low Disorder'].tolist()
    High_dis = df['High Disorder'].tolist()

    # for printing statement one by one
    a = 4
    b = 4

    root1 = Tk()
    root1.geometry('800x800')
    root1.title("SMART REPORT")
    root1.state('zoomed')

    r3 = Frame(root1, bg='#F2E7D5', width=3000, height=1000, relief=SUNKEN)
    r3.pack(fill=X)

    # Shown on second frame
    p1 = Label(r3, text=f"\tSMART  REPORT", fg='green',
               bg='#F2E7D5',
               padx=5, pady=20,
               font="Cambria 36 bold", justify=CENTER)
    p1.grid(row=0, column=1)

    # To display Entry taken from user(using Entry Widget) on screen with help of Label
    p1 = Label(r3, text=f"NAME : {uservalue.get()}", fg='#453C67',
               bg='#F2E7D5',
               padx=5, pady=30,
               font="comfortaa 20 bold", justify=LEFT)
    p1.grid(row=1, column=0)

    p1 = Label(r3, text=f"AGE : {passage.get()}", fg='#453C67',
               bg='#F2E7D5',
               padx=5, pady=30,
               font="comfortaa 20 bold", justify=LEFT)
    p1.grid(row=2, column=0)

    p1 = Label(r3, text=f"GENDER  : {passgender.get()}", fg='#453C67',
               bg='#F2E7D5',
               padx=5, pady=30,
               font="comfortaa 20 bold", justify=LEFT)
    p1.grid(row=2, column=2)

    bmi = (passweight.get() / (passheight.get() * passheight.get()))

    p1 = Label(r3, text=f"BMI : {float(round(bmi, 2))}", fg='#453C67',
               bg='#F2E7D5',
               padx=5, pady=30,
               font="comfortaa 20 bold", justify=LEFT)
    p1.grid(row=1, column=2)

    flag = 0
    flag1 = 0
    l1 = []
    l2 = []

    for i in range(len(inp)):
        if inp[i] < inp1[i]:  # Observed value < Low value of parameter
            l1.append(i)
            flag = 1
        if inp[i] > inp2[i]:  # Observed value > Highe value of parameter
            l2.append(i)
            flag1 = 1

    if flag1 == 0 and flag == 0:  # Observed value is in range of given values of parameter
        p1 = Label(r3, text=f"YOU ARE COMPLETELY FIT", fg='Green',
                   bg='#F2E7D5',
                   padx=30, pady=30,
                   font="comfortaa 18 bold")
        p1.grid(row=3, column=0)

    else:
        # Display Label of parameter, result, disorder predicted and remedies
        p3 = Label(r3, text="PARAMETER",
                   fg='Green',
                   bg='#F2E7D5',
                   pady=20,
                   font="comfortaa 18 bold", justify=LEFT)
        p3.grid(row=4, column=0)

        p3 = Label(r3, text="RESULT",
                   fg='Green',
                   bg='#F2E7D5',
                   padx=5, pady=20,
                   font="comfortaa 18 bold", justify=LEFT)
        p3.grid(row=4, column=1)

        p3 = Label(r3, text=" DISORDER PREDICTED",
                   fg='Green',
                   bg='#F2E7D5',
                   padx=5, pady=20,
                   font="comfortaa 18 bold", justify=LEFT)
        p3.grid(row=4, column=2)

        p3 = Label(r3, text="REMEDIES",
                   fg='Green',
                   bg='#F2E7D5',
                   padx=5, pady=20,
                   font="comfortaa 18 bold", justify=LEFT)
        p3.grid(row=4, column=3)

        for i in l1:
            if len(l1) != 0:
                a = a + 1
                b = b + 1
                p3 = Label(r3,
                           text=f"{inp3[i]}",  # Parameter
                           fg='purple',
                           bg='#F2E7D5',
                           pady=20,
                           font="comfortaa 18", justify=LEFT)
                p3.grid(row=a, column=0)

                p3 = Label(r3, text=" LOW ",
                           fg='purple',
                           bg='#F2E7D5',
                           padx=2, pady=20,
                           font="comfortaa 18", justify=LEFT)
                p3.grid(row=a, column=1)

                p3 = Label(r3, text=f"{low_dis[i]}",  # Low Disorder
                           fg='purple',
                           bg='#F2E7D5',
                           padx=2, pady=20,
                           font="comfortaa 18", justify=LEFT)
                p3.grid(row=a, column=2)

                p3 = Label(r3, text=f"{low_rem[i]}",  # Remedies for Low Disorder
                           fg='purple',
                           bg='#F2E7D5',
                           padx=2, pady=20,
                           font="comfortaa 18", justify=LEFT)
                p3.grid(row=a, column=3)

        for i in l2:
            if len(l2) != 0:
                a = a + 1
                b = b + 1
                p3 = Label(r3,
                           text=f"{inp3[i]}",  # Parameter
                           fg='purple',
                           bg='#F2E7D5',
                           padx=20, pady=20,
                           font="comfortaa 18", justify=LEFT)
                p3.grid(row=a, column=0)

                p3 = Label(r3, text=" HIGH ",
                           fg='purple',
                           bg='#F2E7D5',
                           padx=2, pady=20,
                           font="comfortaa 18", justify=LEFT)
                p3.grid(row=a, column=1)

                p3 = Label(r3, text=f"{High_dis[i]}",  # High Disorder
                           fg='purple',
                           bg='#F2E7D5',
                           padx=20, pady=20,
                           font="comfortaa 18", justify=LEFT)
                p3.grid(row=a, column=2)

                p3 = Label(r3, text=f"{High_rem[i]}",  # Remedies for High Disorder
                           fg='purple',
                           bg='#F2E7D5',
                           padx=20, pady=20,
                           font="comfortaa 18", justify=LEFT)
                p3.grid(row=a, column=3)

    # button 2 -BMI suggestion
    def BMI():
        root2 = Tk()
        root2.title("BMI ")
        root2.geometry('800x800')
        root2.state('zoomed')  # maximize window to full screen

        fr1 = Frame(root2, bg='#F2E7D5', width=3000, height=1000, relief=SUNKEN)
        fr1.pack(fill=X)
        fr2 = Frame(root2, bg='#F2E7D5', width=3000, height=1000, relief=SUNKEN)
        fr2.pack(fill=X)

        if passage.get() > 18:  # if age is greater than 18
            if bmi < 18.5:
                bm1 = Label(fr1, text="YOUR BMI IS LOW !",
                            fg='red',
                            bg='#F2E7D5',
                            padx=20, pady=20,
                            font="comfortaa 30 bold", justify=LEFT)
                bm1.grid(row=0, column=0)
                bm1 = Label(fr1, text="Here are some remedies :",
                            fg='green',
                            bg='#F2E7D5',
                            padx=20, pady=20,
                            font="comfortaa 25 bold", justify=LEFT)
                bm1.grid(row=1, column=0)
                bm1 = Label(fr1,
                            text="1. Eat more frequently. When you're underweight, you may feel full faster\n2. "
                                 "Choose nutrient-rich "
                                 "foods\n3. Try smoothies and shakes\n4. Watch when you drink\n5. Exercise",
                            fg='green',
                            bg='#F2E7D5',
                            padx=20, pady=20,
                            font="comfortaa 23 bold", justify=LEFT)
                bm1.grid(row=1, column=0)

            elif 18.5 < bmi < 24.9:
                bm1 = Label(fr1, text="YOUR BMI IS NORMAL !",
                            fg='green',
                            bg='#F2E7D5',
                            padx=20, pady=20,
                            font="comfortaa 28 bold", justify=LEFT)
                bm1.grid(row=0, column=0)

            elif 25 < bmi:
                bm1 = Label(fr1, text="YOUR BMI IS HIGH !",
                            fg='red',
                            bg='#F2E7D5',
                            padx=20, pady=20,
                            font="comfortaa 28 bold", justify=LEFT)
                bm1.grid(row=0, column=0)
                bm1 = Label(fr1, text="Here are some remedies :",
                            fg='green',
                            bg='#F2E7D5',
                            padx=20, pady=20,
                            font="comfortaa 25 bold", justify=LEFT)
                bm1.grid(row=1, column=0)
                bm1 = Label(fr1,
                            text="1. Drinking lemon water with honey\n2. Powder of fenugreek seeds, carom seeds and "
                                 "black cumin "
                                 "seeds:\n3. Stop consuming artificial sugars:\n4. Eat in a small plate",
                            fg='green',
                            bg='#F2E7D5',
                            padx=20, pady=20,
                            font="comfortaa 23 bold", justify=LEFT)

                bm1.grid(row=3, column=0)

        if 18 >= passage.get():  # if age is less than equals to 18
            if bmi < 18.5:
                bm1 = Label(fr1, text="YOUR BMI IS LOW !",
                            fg='red',
                            bg='#F2E7D5',
                            padx=20, pady=20,
                            font="comfortaa 28 bold", justify=LEFT)
                bm1.grid(row=0, column=0)
                bm1 = Label(fr1, text="Here are some remedies :",
                            fg='green',
                            bg='#F2E7D5',
                            padx=20, pady=20,
                            font="comfortaa 25 bold", justify=LEFT)
                bm1.grid(row=1, column=0)
                bm1 = Label(fr1, text="1. Add leafy vegetables to diet\n2. Eat more fruits\n3. Have more play "
                                      "session\n4. Add more milk products",
                            fg='green',
                            bg='#F2E7D5',
                            padx=20, pady=20,
                            font="comfortaa 23 bold", justify=LEFT)
                bm1.grid(row=1, column=0)

            elif 18.5 < bmi < 24.9:
                bm1 = Label(fr1, text="YOUR BMI IS NORMAL !",
                            fg='green',
                            bg='#F2E7D5',
                            padx=20, pady=20,
                            font="comfortaa 28 bold", justify=LEFT)
                bm1.grid(row=0, column=0)

            elif 25 < bmi:
                bm1 = Label(fr1, text="YOUR BMI IS HIGH !",
                            fg='red',
                            bg='#F2E7D5',
                            padx=20, pady=20,
                            font="comfortaa 28 bold", justify=LEFT)
                bm1.grid(row=0, column=0)
                bm1 = Label(fr1, text="Here are some remedies :",
                            fg='green',
                            bg='#F2E7D5',
                            padx=20, pady=20,
                            font="comfortaa 25 bold", justify=LEFT)
                bm1.grid(row=1, column=0)
                bm1 = Label(fr1,
                            text="1. Indulge an exercises \n2. Avoid fried & fast food\n3. Increase fiber in your diet "
                                 "\n4. Replace packed snacks with homely snacks ",
                            fg='green',
                            bg='#F2E7D5',
                            padx=20, pady=20,
                            font="comfortaa 23 bold", justify=LEFT)

                bm1.grid(row=3, column=0)

    # BMI suggestion button
    b2 = Button(r3, fg="white", bg="green", text="BMI suggestion", command=BMI, font="comfortaa 22 bold")
    b2.grid(row=a + 1, column=0, pady=50, padx=60)
    r4 = Frame(root1, bg='#F2E7D5', width=3000, height=1000, relief=SUNKEN)
    r4.pack(fill=X)


def registration():
    if passvalue.get() == 101:  # Registration Id = 101
        df = pd.read_csv('HIGH- Sheet1.csv')

        inp = df['Observed'].tolist()  # patient's values
        inp1 = df['Low'].tolist()
        inp2 = df['High'].tolist()  # list of high range
        inp3 = df['Parameter'].tolist()  # list of high range
        prediction(inp, inp1, inp2, inp3)

    elif passvalue.get() == 102:  # Registration Id = 102
        df = pd.read_csv('LOW-Sheet1.csv')

        inp = df['Observed'].tolist()
        inp1 = df['Low'].tolist()
        inp2 = df['High'].tolist()  # list of high range
        inp3 = df['Parameter'].tolist()  # list of high range
        prediction(inp, inp1, inp2, inp3)

    elif passvalue.get() == 103:  # Registration Id = 103
        df = pd.read_csv('HIGH_LOW_NORMAL - Sheet1.csv')

        inp = df['Observed'].tolist()
        inp1 = df['Low'].tolist()
        inp2 = df['High'].tolist()  # list of high range
        inp3 = df['Parameter'].tolist()  # list of high range
        prediction(inp, inp1, inp2, inp3)

    elif passvalue.get() == 104:  # Registration Id = 104
        df = pd.read_csv('LOW_HIGH_NORMAL - Sheet1.csv')

        inp = df['Observed'].tolist()
        inp1 = df['Low'].tolist()
        inp2 = df['High'].tolist()  # list of high range
        inp3 = df['Parameter'].tolist()  # list of high range
        prediction(inp, inp1, inp2, inp3)

    elif passvalue.get() == 105:  # Registration Id = 105
        df = pd.read_csv('NORMAL - Sheet1.csv')

        inp = df['Observed'].tolist()
        inp1 = df['Low'].tolist()
        inp2 = df['High'].tolist()  # list of high range
        inp3 = df['Parameter'].tolist()  # list of high range
        prediction(inp, inp1, inp2, inp3)
    else:
        print()
        # If user puts any value of registeration id other than 101-105
        p1 = Label(f3, text=f"SORRY {uservalue.get()}   IS NOT THERE", fg='purple',
                   bg='#F2E7D5',
                   padx=30, pady=20,
                   font="comfortaa 15 ")
        p1.grid(row=0, column=0)


# FRAME - 1 start swayam
f1 = Frame(root, bg='#F2E7D5', width=3000, height=1000, relief=SUNKEN)
f1.pack(fill=X)

l = Label(f1, text="SWAYAM\nBe your own Doctor", fg='#453C67', bg='#F2E7D5', padx=13, pady=1,
          font="Cambria 40 bold")
l.pack(pady=30)

# Importing image
photo = PhotoImage(file="image.png")
label = Label(image=photo)
label.pack()

# FRAME - 2 User input
f2 = Frame(root, borderwidth=2, bg="#F2E7D5", relief=SUNKEN, width=100, height=100)
f2.pack(side=TOP, fill="x")

# Labels for name, registeration id, age, gender, height, weight
l1 = Label(f2, text="Enter Name :", fg='#453C67', bg='#F2E7D5', padx=13, pady=13, font="comfortaa 22 bold",
           borderwidth=1,
           )
l2 = Label(f2, text="Registration Id :", fg='#453C67', bg='#F2E7D5', padx=13, pady=13, font="comfortaa 22 bold",
           borderwidth=1,
           )
l3 = Label(f2, text="Age :", fg='#453C67', bg='#F2E7D5', padx=13, pady=13, font="comfortaa 22 bold", borderwidth=1,
           )
l4 = Label(f2, text="Gender :", fg='#453C67', bg='#F2E7D5', padx=13, pady=13, font="comfortaa 22 bold", borderwidth=1,
           )
l5 = Label(f2, text="Height (m) :", fg='#453C67', bg='#F2E7D5', padx=13, pady=13, font="comfortaa 22 bold",
           borderwidth=1,
           )
l6 = Label(f2, text="Weight (kg) :", fg='#453C67', bg='#F2E7D5', padx=13, pady=13, font="comfortaa 22 bold",
           borderwidth=1,
           )

l1.grid(row=0, column=0)
l2.grid(row=0, column=6)
l3.grid(row=2, column=0)
l4.grid(row=1, column=0)
l5.grid(row=1, column=6)
l6.grid(row=2, column=6)

# User input
# Entry widget for NAME of patient
uservalue = StringVar()
userentry = Entry(f2, textvariable=uservalue, font=('Arial 20'))
userentry.grid(row=0, column=1, padx=20, pady=35)

# Entry widget for registration ID
passvalue = IntVar()
passvalue.set("")
regtry = Entry(f2, textvariable=passvalue, font=('Arial 20'))
regtry.grid(row=0, column=7, padx=20, pady=35)

# Entry widget for age
passage = IntVar()
agetry = Entry(f2, textvariable=passage, font=('Arial 20'))
agetry.grid(row=2, column=1, padx=20, pady=35)
passage.set("")

# Entry widget for gender
passgender = StringVar()
gendertry = Entry(f2, textvariable=passgender, font=('Arial 20'))
gendertry.grid(row=1, column=1, padx=20, pady=35)
passgender.set("")

# Entry widget for height
passheight = DoubleVar()
heighttry = Entry(f2, textvariable=passheight, font=('Arial 20'))
heighttry.grid(row=1, column=7, padx=20, pady=35)
passheight.set("")

# Entry widget for weight
passweight = IntVar()
weighttry = Entry(f2, textvariable=passweight, font=('Arial 20'))
weighttry.grid(row=2, column=7, padx=20, pady=20)
passweight.set("")

# search button
b1 = Button(f2, fg="yellow", bg="red", text="SUBMIT", command=registration, font="comfortaa 22 bold")
b1.grid(row=7, column=4, pady=100, padx=20)
f3 = Frame(root, bg='#F2E7D5', borderwidth=2, width=1000, height=1000, relief=SUNKEN)
f3.pack(side=TOP, fill=X)
root.mainloop()
