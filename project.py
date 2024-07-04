"""Final Project for Harvard's CS50 Python
Once you have solved each of the course’s problem sets, it’s time to implement your final project, a Python program of your very own! The design and implementation of your project is entirely up to you, albeit subject to these requirements:

Your project must be implemented in Python.
Your project must have a main function and three or more additional functions. At least three of those additional functions must be accompanied by tests that can be executed with pytest.
Your main function must be in a file called project.py, which should be in the “root” (i.e., top-level folder) of your project.
Your 3 required custom functions other than main must also be in project.py and defined at the same indentation level as main (i.e., not nested under any classes or functions).
Your test functions must be in a file called test_project.py, which should also be in the “root” of your project. Be sure they have the same name as your custom functions, prepended with test_ (test_custom_function, for example, where custom_function is a function you’ve implemented in project.py).
You are welcome to implement additional classes and functions as you see fit beyond the minimum requirement.
Implementing your project should entail more time and effort than is required by each of the course’s problem sets.
Any pip-installable libraries that your project requires must be listed, one per line, in a file called requirements.txt in the px_UI of your project.
"""
    
    
import tkinter as ui


def main():
    input_patient_info()
    display_columnar()
    wait_for_event()
    save_columnar_as_PDF()
    

def input_patient_info():
    px_UI = ui.Tk()
    px_UI.geometry("400x400")
    px_UI.title("Patient's Information Index")
    
    # constants for entry widgets
    PADX = 20
    IPADX = 3
    PADY = 10
    IPADY = 1
    ui.Entry.config

    # patient's info --------------------------
    
    # constants for each patient's entry info
    WIDGET = 0
    VALUE = 1
    PLACEHOLDER_VALUE = 2
    # name[0, 1] or name[WIDGET, VALUE]
    name = [None, "", "First and Last names"]
    name[WIDGET] = ui.Entry(master=px_UI)
    name[WIDGET].insert(0, name[PLACEHOLDER_VALUE])
    name[WIDGET].grid(padx=PADX, pady=PADY, ipadx=IPADX, ipady=IPADY)
    
    def placeholder_text(event):
        print(event, type(event))
        name[VALUE] = name[WIDGET].get()
        print(name[VALUE])
        if "FocusIn" in str(event) and name[VALUE] == name[PLACEHOLDER_VALUE]:
            name[WIDGET].delete(0, "end")
        elif "FocusOut" in str(event) and name[WIDGET].get() == "":
            name[WIDGET].insert(0, name[PLACEHOLDER_VALUE])
        
        
    name[WIDGET].bind("<FocusIn>", placeholder_text)
    name[WIDGET].bind("<FocusOut>", placeholder_text)
    
    # age
    age = [None, "Age"]
    age[WIDGET] = ui.Entry(master=px_UI)
    age[WIDGET].insert(0, age[VALUE])
    age[WIDGET].grid(padx=PADX, pady=PADY, ipadx=IPADX, ipady=IPADY)
    # address = input("Contact No: ")
    # contact_no = input("Occupation: ")
    # occupation = input("Occupation: ")
    # date = input("Date: ")

    # frames = input("Frames: ")
    # lens = input("Lens: ")
    # total_amount = input("Total Amount: ")
    # deposit = input("Deposit Amount: ")
    # balance = total_amount - deposit

    # rx_od = oculus_dexter_righteye
    # rx _os = oculus_sinister_lefteye
    # rx_add = reading, for 40+ px

    # sales_staff = input("Sales Staff: ")
    # doctor = input("Doctor: ")
                  
    ui.Button(px_UI, text="Exit", command=px_UI.destroy).grid()

    px_UI.mainloop()
    
    print("name:", name)
    
    
def display_columnar():
    # # sheet/page ---------for columnar

    # # header
    # clinic_logo_path = ""
    # date = ""
    # doctor_in_charge = ""
    # sales_personnel = []

    # # table, row per patient (px)
    # job_order = 0
    # name[WIDGET] = ""
    # amount = 0
    # deposit = 0
    # balance = amount - deposit
    # frame = ""
    # lens = ""
    # staff = ""

    # # footer
    # stocks = 0
    # sold_items = 0
    # added_items = 0
    # checked_by = ""
    # date_checked = ""
    ...


def wait_for_event():
    ...
    
    
def save_columnar_as_PDF():
    ...


if __name__ == "__main__":
    main()