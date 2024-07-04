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
from tkinter import ttk
from tkinter import filedialog
import csv

FONT = ("Liberation Sans", 10, "bold")
FONTBIG = ("Liberation Sans", 11, "bold")


def main():
    px_infos = input_patient_info()
    display_columnar(px_infos)
    wait_for_event()
    save_columnar_as_PDF()
    

def input_patient_info():
    px_UI = ui.Tk()
    px_UI.geometry("650x750+20+20") # Size 400x400, Start position at x:20 and y:20
    px_UI.title("Patient's Information Index")
    
    clinic_logo_frame = ui.Frame(master=px_UI)
    clinic_logo_frame.grid(row=0, column=0, columnspan=2)
    px_info_frame = ui.Frame(master=px_UI)
    px_info_frame.grid(row=1, column=0, columnspan=2)
    px_info_frameA = ui.Frame(master=px_info_frame)
    px_info_frameA.grid(row=0, column=0)
    px_info_frameB = ui.Frame(master=px_info_frame)
    px_info_frameB.grid(row=0, column=1)
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
    INPUT_COLOR = "#000000"
    PLACEHOLDER_COLOR = "#5d5d5d"

    # tk Entry for each patient's entry info; txtEntry is a list for [0] widget [1] text value and [2] placeholder label
    def ui_entry(txtEntry):
        print(txtEntry, type(txtEntry))
        txtEntry[WIDGET] = ui.Entry(master=px_info_frameA, fg=PLACEHOLDER_COLOR, font=FONT, width=40)
        txtEntry[WIDGET].insert(0, txtEntry[PLACEHOLDER_VALUE])
        txtEntry[WIDGET].grid(column=0, padx=PADX, pady=PADY, ipadx=IPADX, ipady=IPADY)
        
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
    
    def ui_entry2(txtEntry):
        print(txtEntry, type(txtEntry))
        txtEntry[WIDGET] = ui.Entry(
            master=px_info_frameB, fg=PLACEHOLDER_COLOR, font=FONT, width=40)
        txtEntry[WIDGET].insert(0, txtEntry[PLACEHOLDER_VALUE])
        txtEntry[WIDGET].pack(padx=PADX, pady=PADY, ipadx=IPADX, 
                              ipady=IPADY+20 if "Rx" in txtEntry[PLACEHOLDER_VALUE] else IPADY)

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
    clinic_label.grid(row=0, column=0, columnspan=1, sticky="w")
    
    # patient's info --------------------------

    name = ui_entry([None, "", "Patient's Fullname"])

    age = ui_entry([None, "", "Age"])
    address = ui_entry([None, "", "Address"])
    contact_no = ui_entry([None, "", "Contact Number"])
    occupation = ui_entry([None, "", "Occupation"])
    date = ui_entry([None, "", "Date"])

    frames = ui_entry([None, "", "Frames"])
    lens = ui_entry([None, "", "Lens"])
    total_amount = ui_entry([None, "", "Total Amount"])
    deposit = ui_entry([None, "", "Deposit Amount"])
    # balance = total_amount - deposit


    # rx_od = oculus_dexter_righteye
    rx_od = ui_entry2([None, "", "Rx OD"])
    # rx _os = oculus_sinister_lefteye
    rx_os = ui_entry2([None, "", "Rx OS"])
    # rx_add = reading, for 40+ px
    rx_add = ui_entry2([None, "", "Rx ADD"])

    sales_staff = ui_entry2([None, "", "Sales Staff"])
    doctor = ui_entry2([None, "", "Doctor"])

    ui.Button(master=proceed_frame, text="PROCEED", font=FONTBIG, command=px_UI.destroy).grid(row=0, column=0, columnspan=2)

    px_UI.mainloop()
    
    px_info = (name[VALUE], age[VALUE], address[VALUE], contact_no[VALUE], occupation[VALUE], date[VALUE])
    
    print("px_info:", px_info)
    
    return px_info
    
    
def display_columnar(*columns):
    print("display_colmnar args:", columns)
    all_columns = str(columns)

    columnarUI = ui.Tk()
    columnarUI.geometry("1200x800+20+20")
    columnarUI.title("Columnar of Clinic Transactions")
    
    # create a notebook to held frames
    notebook = ttk.Notebook(columnarUI, width=1200, height=700)

    # create frames
    ed_frame1 = ttk.Frame(notebook, width=1100, height=800)
    pe_frame2 = ttk.Frame(notebook, width=1100, height=800)
    
    
    def open_csv_file():
        file_path = filedialog.askopenfilename(
            title="Open CSV File", filetypes=[("CSV files", "*.csv")])
        if file_path:
            display_csv_data(file_path)


    def display_csv_data(file_path):
        
        try:
            with open(file_path, 'r', newline='') as csvfile:
                csv_reader = csv.reader(csvfile)
                
                # Read the header row
                header = next(csv_reader)
                
                # Clear the current data
                tree.delete(*tree.get_children())  

                tree["columns"] = header
                for column in header:
                    tree.heading(column, text=column)
                    tree.column(column, width=20 if column in ("age", "lens") else 100 if column!="address" else 200)

                for row in csv_reader:
                    tree.insert("", "end", values=row)

                status_label.config(text=f"CSV file loaded: {file_path}")

        except Exception as error:
            status_label.config(text=f"Error: {str(error)}")


    def open_csv_file2():
        file_path = filedialog.askopenfilename(
            title="Open CSV File", filetypes=[("CSV files", "*.csv")])
        if file_path:
            display_csv_data2(file_path)


    def display_csv_data2(file_path):

        try:
            with open(file_path, 'r', newline='') as csvfile:
                csv_reader = csv.reader(csvfile)

                # Read the header row
                header = next(csv_reader)

                # Clear the current data
                tree2.delete(*tree2.get_children())

                tree2["columns"] = header
                for column in header:
                    tree2.heading(column, text=column)
                    tree2.column(column, width=20 if column in (
                        "age", "lens") else 100 if column != "address" else 200)

                for row in csv_reader:
                    tree2.insert("", "end", values=row)

                status_label2.config(text=f"CSV file loaded: {file_path}")

        except Exception as error:
            status_label2.config(text=f"Error: {str(error)}")



    notebook.pack(pady=10, expand=True, side="top", fill="both")
    ed_frame1.pack(fill='both', expand=True)
    pe_frame2.pack(fill='both', expand=True)

    # add frames to notebook
    # add first frame
    notebook.add(ed_frame1, text='Eye Clinic 1')

    open_CSV_button = ui.Button(ed_frame1, text="Open CSV File", command=open_csv_file)
    open_CSV_button.pack(padx=20, pady=10)

    tree = ttk.Treeview(ed_frame1, show="headings")
    tree.pack(padx=20, pady=20, fill="both", expand=True)
    
    status_label = ui.Label(ed_frame1, text="", padx=20, pady=10)
    status_label.pack()

    file_path = "eyedl_px.csv"
    display_csv_data(file_path)

    # add second frame to notebook
    notebook.add(pe_frame2, text='Personal Clinic 2')

    open_CSV_button2 = ui.Button(pe_frame2, text="Open CSV File", command=open_csv_file2)
    open_CSV_button2.pack(padx=20, pady=10)

    tree2 = ttk.Treeview(pe_frame2, show="headings")
    tree2.pack(padx=20, pady=20, fill="both", expand=True)
    
    status_label2 = ui.Label(pe_frame2, text="", padx=20, pady=10)
    status_label2.pack()
    
    file_path2 = "personal_px.csv"
    display_csv_data2(file_path2)
    
    ui.Button(master=columnarUI, text="EXIT COLUMNAR", font=FONTBIG, command=columnarUI.destroy).pack(pady=5)
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