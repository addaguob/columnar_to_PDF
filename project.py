"""
Columnar to PDF Application

by Alexander D. Daguob
Manila, Philippines
alexanderdaguob@gmail.com

Guidelines for Final Project for Harvard's CS50 Python
Once you have solved each of the course’s problem sets, it’s time to
implement your final project, a Python program of your very own!
The design and implementation of your project is entirely up to
you, albeit subject to these requirements:

➡ Your project must be implemented in Python.

➡ Your project must have a main function and three or more additional
functions.

➡ At least three of those additional functions must be accompanied by
tests that can be executed with pytest.

➡ Your main function must be in a file called project.py, which should be
in the “root” (i.e., top-level folder) of your project.

➡ Your 3 required custom functions other than main must also be in

project.py and defined at the same indentation level as main (i.e., not
nested under any classes or functions).

➡ Your test functions must be in a file called test_project.py, which
should also be in the “root” of your project.

➡ Be sure they have the same name as your custom functions, prepended

with test_ (test_custom_function, for example, where custom_function is
a function you’ve implemented in project.py).

➡ You are welcome to implement additional classes and functions as you
see fit beyond the minimum requirement.

➡ Implementing your project should entail more time and effort than is
required by each of the course’s problem sets.

➡ Any pip-installable libraries that your project requires must be
listed, one per line, in a file called requirements.txt in the root of your project.
""" 
# tkinter will do to keep everything in a single file module
import tkinter as ui
from tkinter import ttk
from tkinter import filedialog
import csv

# UI constants
FONT = ("Liberation Sans", 10, "bold")
FONTBIG = ("Liberation Sans", 11, "bold")
# constants for entry widgets
PADX = 20
PADY = 10
IPADX = 2
IPADY = 2
# text_entry[WIDGET, VALUE, PLACEHOLDER_VALUE]
WIDGET = 0
VALUE = 1
PLACEHOLDER_VALUE = 2
INPUT_COLOR = "#000000"
PLACEHOLDER_COLOR = "#5d5d5d"

def main():
    """Main overview of the program"""
    display_patients(
        input_patient_info())
    display_columnar()
    wait_for_event()
    save_columnar_as_PDF()
    

def input_patient_info():
    """Create a form for patient's information"""
    px_UI = ui.Tk()
    # Size 650x750, Start position at x:20 and y:20
    px_UI.geometry("650x750+20+20")
    px_UI.title("Patient's Information Index")
    # For naming consistency:
    # <widget type>_<widget name>_<widget attribute>
    frame_clinic_logo = ui.Frame(master=px_UI)
    frame_clinic_logo.grid(row=0, column=0, columnspan=2)
    frame_px_info = ui.Frame(master=px_UI)
    frame_px_info.grid(row=1, column=0, columnspan=2)
    frame_px_info_left = ui.Frame(master=frame_px_info)
    frame_px_info_left.grid(row=0, column=0)
    frame_px_info_right = ui.Frame(master=frame_px_info)
    frame_px_info_right.grid(row=0, column=1)
    frame_proceed = ui.Frame(master=px_UI)
    frame_proceed.grid(row=2, column=0)

    def ui_entry(master, txt_entry):
        """Draw the entry widget and return it along with
        its value and placeholder.
        """
        print(txt_entry, type(txt_entry))
        txt_entry[WIDGET] = ui.Entry(master=master, fg=PLACEHOLDER_COLOR, font=FONT, width=40)
        txt_entry[WIDGET].insert(0, txt_entry[PLACEHOLDER_VALUE])
        txt_entry[WIDGET].pack(
            padx=PADX,
            pady=PADY,
            ipadx=IPADX,
            ipady=IPADY+20 if "Rx" in txt_entry[PLACEHOLDER_VALUE] \
                else IPADY)
        
        def placeholder_label(event):
            """Hint text for the entry widget"""
            event_str = str(event)
            # print(event_str)
            if "FocusIn" in event_str \
            and txt_entry[WIDGET].get() == txt_entry[PLACEHOLDER_VALUE]:
                txt_entry[WIDGET].delete(0, "end")
            elif "FocusOut" in event_str \
            and txt_entry[WIDGET].get() == "":
                txt_entry[WIDGET].insert(0, txt_entry[PLACEHOLDER_VALUE])
                txt_entry[WIDGET].config(fg=PLACEHOLDER_COLOR)
            elif "Key" in event_str or (
                    "Motion" in event_str \
                    and not txt_entry[WIDGET].get() \
                    in ("", txt_entry[PLACEHOLDER_VALUE])
                ):
                txt_entry[WIDGET].config(fg=INPUT_COLOR)
                txt_entry[VALUE] = txt_entry[WIDGET].get()
                
        txt_entry[WIDGET].bind("<FocusIn>", placeholder_label)
        txt_entry[WIDGET].bind("<FocusOut>", placeholder_label)
        txt_entry[WIDGET].bind("<Key>", placeholder_label)
        txt_entry[WIDGET].bind("<Motion>", placeholder_label)
        
        return txt_entry

    logo = ui.PhotoImage(file="clinic_logo.png")
    clinic_label = ui.Label(master=frame_clinic_logo, image=logo)
    clinic_label.grid(row=0, column=0, columnspan=1, sticky="w")
    
    # patient's info (left)------------------------------------------
    name = ui_entry(frame_px_info_left, [None, "", "Patient's Fullname"])
    age = ui_entry(frame_px_info_left, [None, "", "Age"])
    address = ui_entry(frame_px_info_left, [None, "", "Address"])
    contact_no = ui_entry(
        frame_px_info_left, [None, "", "Contact Number"])
    occupation = ui_entry(frame_px_info_left, [None, "", "Occupation"])
    date = ui_entry(frame_px_info_left, [None, "", "Date"])
    # frames = ui_entry(frame_px_info_left, [None, "", "Frames"])
    ui.Label(frame_px_info_right, text="Frames").pack()
    current_var = ui.StringVar()
    keepvar = current_var.get
    frames = ttk.Combobox(frame_px_info_right, textvariable=keepvar, values=[
        "Contact Lens",
        "Own F.",
        "9100",
        "ED955",
        "ED990",
        "ED9150",
        "ED9150",
        "ED9500",
        "PE990",
        "PE9150",
    ])
    frames.pack()
    lens = ui_entry(frame_px_info_left, [None, "", "Lens"])
    total_amount = ui_entry(
        frame_px_info_left, [None, "", "Total Amount"])
    deposit = ui_entry(frame_px_info_left, [None, "", "Deposit Amount"])
    # balance = total_amount - deposit
    
    # patient's info (right)------------------------------------------
    # rx_od = oculus_dexter_righteye
    rx_od = ui_entry(frame_px_info_right, [None, "", "Rx OD"])
    # rx _os = oculus_sinister_lefteye
    rx_os = ui_entry(frame_px_info_right, [None, "", "Rx OS"])
    # rx_add = reading, for 40+ px
    rx_add = ui_entry(frame_px_info_right, [None, "", "Rx ADD"])

    sales_staff = ui_entry(frame_px_info_right, [None, "", "Sales Staff"])
    doctor = ui_entry(frame_px_info_right, [None, "", "Doctor"])

    ui.Button(master=frame_proceed, text="PROCEED", font=FONTBIG, command=px_UI.destroy).grid(row=0, column=0, columnspan=2)
    px_UI.mainloop()
    
    px_info = (
        name[VALUE], age[VALUE],
        address[VALUE], contact_no[VALUE],
        occupation[VALUE], date[VALUE])
    print("px_info:", px_info)
    return px_info
    

def display_patients(*columns):
    print("display_colmnar args:", columns)
    all_columns = str(columns)
    px_columnarUI = ui.Tk()
    px_columnarUI.geometry("1450x800+20+20")
    px_columnarUI.title("Columnar of Clinic Transactions")
    # create a notebook to held frames
    notebook = ttk.Notebook(px_columnarUI, width=1200, height=500)
    # create frames
    ed_frame1 = ttk.Frame(notebook, width=1100, height=500)
    pe_frame2 = ttk.Frame(notebook, width=1100, height=500)
    
    def open_csv_file(file_path, tree, label_status):
        file_path = filedialog.askopenfilename(
            title="Open CSV File", filetypes=[("CSV Databases", "*.csv")], initialdir="./")
        if file_path:
            display_csv_data(file_path, tree, label_status)

    def display_csv_data(file_path, tree, label_status):
        """Display data from a CSV file in a Treeview widget."""
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
                    tree.column(
                        column,
                        width=20 if column in ("age", "lens") \
                            else 100 if column \
                            not in ("address", "occupation") else 200)
                for row in csv_reader:
                    tree.insert("", "end", values=row)
                label_status.config(
                    text=f"Patients CSV File loaded: {file_path}")
        except Exception as error:
            label_status.config(text=f"Error: {str(error)}")

    notebook.pack(pady=10, expand=True, side="top", fill="both")
    ed_frame1.pack(fill='both', expand=True)
    pe_frame2.pack(fill='both', expand=True)

    # add frames to notebook
    # add first frame
    notebook.add(ed_frame1, text='Eye Clinic Patients')

    button_open_CSV = ui.Button(
        ed_frame1, text="Open Patients CSV File",
        command=lambda: open_csv_file(file_path, tree, label_status))
    tree = ttk.Treeview(ed_frame1, show="headings")
    label_status = ui.Label(ed_frame1, text="", padx=20, pady=10)
    
    button_open_CSV.pack(padx=20, pady=10)
    tree.pack(padx=20, pady=20, fill="both", expand=True)
    label_status.pack()

    file_path = "eyedl_px.csv"
    display_csv_data(file_path, tree, label_status)

    # add second frame to notebook
    notebook.add(pe_frame2, text='Another Clinic Patients')

    button_open_CSV2 = ui.Button(
        pe_frame2, text="Open Patients CSV File",
        command=lambda: open_csv_file(file_path2, tree2, label_status2))
    tree2 = ttk.Treeview(pe_frame2, show="headings")
    label_status2 = ui.Label(pe_frame2, text="", padx=20, pady=10)
    
    button_open_CSV2.pack(padx=20, pady=10)
    tree2.pack(padx=20, pady=20, fill="both", expand=True)
    label_status2.pack()
    
    file_path2 = "personal_px.csv"
    display_csv_data(file_path2, tree2, label_status2)
    
    ui.Button(master=px_columnarUI, text="EXIT COLUMNAR", font=FONTBIG, command=px_columnarUI.destroy).pack(pady=5)
    px_columnarUI.mainloop()

def display_columnar():
    columnarUI = ui.Tk()
    columnarUI.geometry("1200x700+20+20")
    columnarUI.title("Columnar of Clinic Transactions")
    # create a notebook to held frames
    notebook = ttk.Notebook(columnarUI, width=1200, height=500)
    # create frames
    ed_frame1 = ttk.Frame(notebook, width=1200, height=500)
    pe_frame2 = ttk.Frame(notebook, width=1200, height=500)

    def open_csv_file(file_path, tree, label_status):
        """Invoked from display_csv_data to open a CSV file."""
        file_path = filedialog.askopenfilename(
            title="Open CSV File", filetypes=[("CSV Databases", "*.csv")], initialdir="./")
        if file_path:
            display_csv_data(file_path, tree, label_status)

    def display_csv_data(file_path, tree, label_status):
        """Display data from a CSV file in a Treeview widget
        and update the status label.
        """
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
                    tree.column(column, width=20 if column in ("age", "lens")
                                else 40 if column not in ("address", "occupation") else 200)

                for row in csv_reader:
                    tree.insert("", "end", values=row)

                label_status.config(text=f"CSV File loaded: {file_path}")

        except Exception as error:
            label_status.config(text=f"Error: {str(error)}")

    notebook.pack(pady=10, expand=True, side="top", fill="both")
    ed_frame1.pack(fill='both', expand=True)
    pe_frame2.pack(fill='both', expand=True)

    # add frames to notebook
    # add first frame
    notebook.add(ed_frame1, text='Eye Clinic Transactions')

    button_open_CSV = ui.Button(
        ed_frame1, text="Open CSV File",
        command=lambda: open_csv_file(file_path, tree, label_status))
    button_open_CSV.pack(padx=20, pady=10)

    tree = ttk.Treeview(ed_frame1, show="headings")
    tree.pack(padx=20, pady=20, fill="both", expand=True)

    label_status = ui.Label(ed_frame1, text="", padx=20, pady=10)
    label_status.pack()

    file_path = "eyedl_columnar.csv"
    display_csv_data(file_path, tree, label_status)
    # Observe if objects of tree and label_status are changed too
    # without returning values

    # add second frame to notebook
    notebook.add(pe_frame2, text='Another Clinic Transactions')
    button_open_CSV2 = ui.Button(
        pe_frame2,
        text="Open CSV File",
        command=lambda: open_csv_file(file_path2, tree2, label_status2))
    tree2 = ttk.Treeview(pe_frame2, show="headings")
    label_status2 = ui.Label(pe_frame2, text="", padx=20, pady=10)

    button_open_CSV2.pack(padx=20, pady=10)
    tree2.pack(padx=20, pady=20, fill="both", expand=True)
    label_status2.pack()

    file_path2 = "personal_columnar.csv"
    display_csv_data(file_path2, tree2, label_status2)

    ui.Button(master=columnarUI, text="EXIT COLUMNAR",
              font=FONTBIG, command=columnarUI.destroy).pack(pady=5)
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


def wait_for_event():
    pass
    
    
def save_columnar_as_PDF():
    pass


if __name__ == "__main__":
    main()
