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
FONT = ("Liberation Sans", 11, "bold")


def main():
    px_infos = input_patient_info()
    display_columnar(px_infos)
    wait_for_event()
    save_columnar_as_PDF()
    

def input_patient_info():
    px_UI = ui.Tk()
    px_UI.geometry("400x400+20+20") # Size 400x400, Start position at x:20 and y:20
    px_UI.title("Patient's Information Index")
    
    clinic_logo_frame = ui.Frame(master=px_UI)
    clinic_logo_frame.grid(row=0, column=0)
    px_info_frame = ui.Frame(master=px_UI)
    px_info_frame.grid(row=1, column=0)
    proceed_frame = ui.Frame(master=px_UI)
    proceed_frame.grid(row=2, column=0)

    # constants for entry widgets
    PADX = 20
    IPADX = 2
    PADY = 10
    IPADY = 2

    
    # constants for each patient's entry info, sample: name_entry[0, 1, 2] or name_entry[WIDGET, VALUE, PLACEHOLDER_VALUE]
    WIDGET = 0
    VALUE = 1
    PLACEHOLDER_VALUE = 2

    # tk Entry for each patient's entry info; txtEntry is a list for [0] widget [1] text value and [2] placeholder label
    def ui_entry(txtEntry):
        print(txtEntry, type(txtEntry))
        INPUT_COLOR = "#000000"
        PLACEHOLDER_COLOR = "#828282"
        txtEntry[WIDGET] = ui.Entry(master=px_info_frame, fg=PLACEHOLDER_COLOR, font=FONT, width=50)
        txtEntry[WIDGET].insert(0, txtEntry[PLACEHOLDER_VALUE])
        txtEntry[WIDGET].pack(padx=PADX, pady=PADY, ipadx=IPADX, ipady=IPADY)
        
        def placeholder_label(event):
            event_str = str(event)
            print(event_str)
            if "FocusIn" in event_str and txtEntry[WIDGET].get() == txtEntry[PLACEHOLDER_VALUE]:
                txtEntry[WIDGET].delete(0, "end")
            elif "FocusOut" in event_str and txtEntry[WIDGET].get() == "":
                txtEntry[WIDGET].insert(0, txtEntry[PLACEHOLDER_VALUE])
                txtEntry[WIDGET].config(fg=PLACEHOLDER_COLOR)
            elif "Key" in event_str or ("Motion" in event_str and not txtEntry[WIDGET].get() in ("", txtEntry[PLACEHOLDER_VALUE])):
                txtEntry[WIDGET].config(fg=INPUT_COLOR)
                txtEntry[VALUE] = txtEntry[WIDGET].get()
                    
                    
        txtEntry[WIDGET].bind("<FocusIn>", placeholder_label)
        txtEntry[WIDGET].bind("<FocusOut>", placeholder_label)
        txtEntry[WIDGET].bind("<Key>", placeholder_label)
        txtEntry[WIDGET].bind("<Motion>", placeholder_label)
        
        return txtEntry
    

    logo = ui.PhotoImage(file="clinic_logo.png")
    clinic_label = ui.Label(master=clinic_logo_frame, image=logo)
    clinic_label.grid(row=0, column=0)
    
    # patient's info --------------------------

    name = ui_entry([None, "", "Patient's Fullname"])

    age = ui_entry([None, "", "Age"])
    address = ui_entry([None, "", "Address"])
    contact_no = ui_entry([None, "", "Contact Number"])
    occupation = ui_entry([None, "", "Occupation"])
    date = ui_entry([None, "", "Date"])

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

    ui.Button(master=proceed_frame, text="Proceed", font=FONT, command=px_UI.destroy).grid(row=0, column=0)

    px_UI.mainloop()
    
    px_info = (name[VALUE], age[VALUE], address[VALUE], contact_no[VALUE], occupation[VALUE], date[VALUE])
    
    print("px_info:", px_info)
    
    return px_info
    
    
def display_columnar(*columns):
    print("display_colmnar args:", columns)
    all_columns = str(columns)

    columnarUI = ui.Tk()
    columnarUI.geometry("700x500+20+20")
    columnarUI.title("Columnar of Clinic Transactions")
    
    ui.Label(master=columnarUI, text=all_columns, font=FONT).grid(pady=10)
    ui.Button(master=columnarUI, text="Okay", font=FONT, command=columnarUI.destroy).grid(pady=5)
    columnarUI.mainloop()
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