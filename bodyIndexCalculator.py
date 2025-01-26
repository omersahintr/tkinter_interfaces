from tkinter import *

def bmi_calculator():
    if txt_weight.get() != "0" and txt_size.get() !="0":
        label_comments.config(text="")
        label_results.config(text="")
        try: #Error trapping to prevent an incorrect value from being returned.

            bmi_weight = float(txt_weight.get()) #body weight by kg
            bmi_size = float(txt_size.get()) / 100  # cm to meter converted
            bmiCalculate = bmi_weight / (pow(bmi_size, 2))  # bmi calculate function
            label_results.config(text=("BMI: " + str(round(bmiCalculate, 2))),bg="light blue")  # float number is round 2-digits and convert to string

            #Comment according to bmi values
            if bmiCalculate < 16.0:
                label_comments.config(text="Severe Thinness",bg="light green")
            elif bmiCalculate >= 16.0 and bmiCalculate < 17.0:
                label_comments.config(text="Moderate Thinness",bg="green")
            elif bmiCalculate >= 17.0 and bmiCalculate < 18.5:
                label_comments.config(text="Mild Thinness",bg="yellow")
            elif bmiCalculate >= 18.5 and bmiCalculate < 25.0:
                label_comments.config(text="Normal",bg="white")
            elif bmiCalculate >= 25.0 and bmiCalculate < 30.0:
                label_comments.config(text="Overweight",bg="orange")
            elif bmiCalculate >= 30.0 and bmiCalculate < 35.0:
                label_comments.config(text="Obese Class I",bg="red")
            elif bmiCalculate >= 35.0 and bmiCalculate < 40.0:
                label_comments.config(text="Obese Class II",bg="red")
            elif bmiCalculate >= 40.0:
                label_comments.config(text="Obese Class III",bg="red")
            else:
                label_comments.config(text="No Comment!",bg="red")

        except ValueError:
            label_comments.config(text="Just Numbers")
            return
        except ZeroDivisionError:
            label_comments.config(text="Do not type zero!")
            return
    else:
        label_comments.config(text="Do not type zero")
#Tkinter object:
tkScreen = Tk()
tkScreen.minsize(width=400,height=300)
tkScreen.title("Body Index Calculator - BMI")

#Labels:
label_weight = Label(text="Your Weight(kg):",fg="blue",font=("Verdana",12,"bold"))
label_size = Label(text="Your Body Size(cm):",fg="blue",font=("Verdana",12,"bold"))
label_results = Label(text="",font=("Verdana",12,"bold"))
label_comments = Label(text="",font=("Verdana",12,"bold"))

#Entries:
txt_weight = Entry(width=10)
txt_size = Entry(width=10)

btn_calc = Button(text="CALCULATE",font=("Verdana",14,"bold"),command=bmi_calculator)

###Locator###
label_weight.grid(row=0,column=0)
txt_weight.grid(row=0,column=1)
label_size.grid(row=1,column=0)
txt_size.grid(row=1,column=1)
label_results.grid(row=3,column=1)
label_comments.grid(row=4,column=1)
btn_calc.grid(row=2,column=0)

tkScreen.mainloop()