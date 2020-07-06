from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from ttkthemes import themed_tk as tk
from backend_penn import Database

class Frontend:
    """
    Class that draws frontend of planner using Tkinter
    """

    ## constructor
    def __init__(self):
        self.selected_tuple = ()
        self.planned_tuple = ()

        # self.ttk.Style.configure(font = ("Gobold Lowplus", 10)s)
        self.my_big_font = ("Gobold", 12)
        self.my_small_font = ("Gobold Lowplus", 10)
        # self.customFont = tkFont.Font(family="Helvetica", size=12)
        self.window = tk.ThemedTk() ## create main frame
        self.window.get_themes()
        self.window.configure(bg="#CCE6FF")
        self.window.set_theme("plastik")
        self.window.title("Penn Planner") ## set fram title

        self.course_list = []

        ## Labels
        title_label = Label(self.window, text="Penn Course Organizer", fg="white", bg="#003CB2", borderwidth=2, relief="ridge", font=self.my_big_font)
        title_label.grid(row=0, column=0, columnspan=2)
        code_label = Label(self.window, text="Code", font=self.my_small_font, fg="white", bg="#7CB9E8", borderwidth=2, relief="ridge")
        code_label.grid(row=1, column=0)
        course_label = Label(self.window, text="Course Name", font=self.my_small_font, fg="white", bg="#7CB9E8", borderwidth=2, relief="ridge")
        course_label.grid(row=2, column=0)
        credit_label = Label(self.window, text="CUs", font=self.my_small_font, fg="white", bg="#7CB9E8", borderwidth=2, relief="ridge")
        credit_label.grid(row=3, column=0)

        ## Entry Boxes
        self.code_text = StringVar()
        self.code_entry = ttk.Entry(self.window, textvariable = self.code_text, font=self.my_small_font)
        self.code_entry.grid(row = 1, column=1)
        self.course_text = StringVar()
        self.course_entry = ttk.Entry(self.window, textvariable = self.course_text, font=self.my_small_font)
        self.course_entry.grid(row = 2, column=1)
        self.credit_text = StringVar()
        self.credit_entry = ttk.Entry(self.window, textvariable=self.credit_text, font=self.my_small_font)
        self.credit_entry.grid(row=3, column=1)

        ## Lists
        all_label = Label(self.window, text="Course Cart", font=self.my_big_font, fg="black", bg="#7CB9E8", borderwidth=2, relief="ridge")
        all_label.grid(row=7, column=0)
        self.list_all = Listbox(self.window, height=15, width = 35, font=self.my_small_font)
        self.list_all.grid(row=8, column=0, columnspan=2, rowspan=15)
        self.list_all.bind('<<ListboxSelect>>', self.get_selected_row)

        ## Semesters list
        self.ff_list = []
        self.fs_list = []
        self.sf_list = []
        self.ss_list = []
        self.jf_list = []
        self.js_list = []
        self.sef_list = []
        self.ses_list = []

        ff_label = Label(self.window, text="Freshman Fall", font=self.my_big_font, fg="black", bg="#7CB9E8", borderwidth=2, relief="ridge")
        ff_label.grid(row=0, column=4)
        self.ff_cu = StringVar()
        self.ff_cu.set("0 CU")
        self.ff_cu_label = Label(self.window, textvariable=self.ff_cu, font=self.my_small_font, fg="black", bg="#80FFD4", relief="sunken")
        self.ff_cu_label.grid(row=0, column = 5)
        self.list_freshman_fall = Listbox(self.window, height=6, width = 40, font=self.my_small_font)
        self.list_freshman_fall.grid(row=1, column=3, rowspan = 6, columnspan=3)
        self.list_freshman_fall.bind('<<ListboxSelect>>', self.get_selected_ff)

        fs_label = Label(self.window, text="Freshman Spring", font=self.my_big_font, fg="black", bg="#7CB9E8", borderwidth=2, relief="ridge")
        fs_label.grid(row=0, column=10)
        self.fs_cu = StringVar()
        self.fs_cu.set("0 CU")
        self.fs_cu_label = Label(self.window, textvariable=self.fs_cu, font=self.my_small_font, fg="black", bg="#80FFD4", relief="sunken")
        self.fs_cu_label.grid(row=0, column = 11)
        self.list_freshman_spring = Listbox(self.window, height=6, width = 40, font=self.my_small_font)
        self.list_freshman_spring.grid(row=1, column=9, rowspan = 6, columnspan=3)
        self.list_freshman_spring.bind('<<ListboxSelect>>', self.get_selected_fs)

        sf_label = Label(self.window, text="Sophomore Fall", font=self.my_big_font, fg="black", bg="#7CB9E8", borderwidth=2, relief="ridge")
        sf_label.grid(row=7, column=4)
        self.sf_cu = StringVar()
        self.sf_cu.set("0 CU")
        self.sf_cu_label = Label(self.window, textvariable=self.sf_cu, font=self.my_small_font, fg="black", bg="#80FFD4", relief="sunken")
        self.sf_cu_label.grid(row=7, column = 5)
        self.list_sophomore_fall = Listbox(self.window, height=6, width = 40, font=self.my_small_font)
        self.list_sophomore_fall.grid(row=8, column=3, rowspan = 6, columnspan=3)
        self.list_sophomore_fall.bind('<<ListboxSelect>>', self.get_selected_sf)

        ss_label = Label(self.window, text="Sophomore Spring", font=self.my_big_font, fg="black", bg="#7CB9E8", borderwidth=2, relief="ridge")
        ss_label.grid(row=7, column=10)
        self.ss_cu = StringVar()
        self.ss_cu.set("0 CU")
        self.ss_cu_label = Label(self.window, textvariable=self.ss_cu, font=self.my_small_font, fg="black", bg="#80FFD4", relief="sunken")
        self.ss_cu_label.grid(row=7, column = 11)
        self.list_sophomore_spring = Listbox(self.window, height=6, width = 40, font=self.my_small_font)
        self.list_sophomore_spring.grid(row=8, column=9, rowspan = 6, columnspan=3)
        self.list_sophomore_spring.bind('<<ListboxSelect>>', self.get_selected_ss) 

        jf_label = Label(self.window, text="Junior Fall", font=self.my_big_font, fg="black", bg="#7CB9E8", borderwidth=2, relief="ridge")
        jf_label.grid(row=14, column=4)
        self.jf_cu = StringVar()
        self.jf_cu.set("0 CU")
        self.jf_cu_label = Label(self.window, textvariable=self.jf_cu, font=self.my_small_font, fg="black", bg="#80FFD4", relief="sunken")
        self.jf_cu_label.grid(row=14, column = 5)
        self.list_junior_fall = Listbox(self.window, height=6, width = 40, font=self.my_small_font)
        self.list_junior_fall.grid(row=15, column=3, rowspan = 6, columnspan=3)
        self.list_junior_fall.bind('<<ListboxSelect>>', self.get_selected_jf)

        js_label = Label(self.window, text="Junior Spring", font=self.my_big_font, fg="black", bg="#7CB9E8", borderwidth=2, relief="ridge")
        js_label.grid(row=14, column=10)
        self.js_cu = StringVar()
        self.js_cu.set("0 CU")
        self.js_cu_label = Label(self.window, textvariable=self.js_cu, font=self.my_small_font, fg="black", bg="#80FFD4", relief="sunken")
        self.js_cu_label.grid(row=14, column = 11)
        self.list_junior_spring = Listbox(self.window, height=6, width = 40, font=self.my_small_font)
        self.list_junior_spring.grid(row=15, column=9, rowspan = 6, columnspan=3)
        self.list_junior_spring.bind('<<ListboxSelect>>', self.get_selected_js)

        sef_label = Label(self.window, text="Senior Fall", font=self.my_big_font, fg="black", bg="#7CB9E8", borderwidth=2, relief="ridge")
        sef_label.grid(row=21, column=4)
        self.sef_cu = StringVar()
        self.sef_cu.set("0 CU")
        self.sef_cu_label = Label(self.window, textvariable=self.sef_cu, font=self.my_small_font, fg="black", bg="#80FFD4", relief="sunken")
        self.sef_cu_label.grid(row=21, column = 5)
        self.list_senior_fall = Listbox(self.window, height=6, width = 40, font=self.my_small_font)
        self.list_senior_fall.grid(row=22, column=3, rowspan = 6, columnspan=3)
        self.list_senior_fall.bind('<<ListboxSelect>>', self.get_selected_sef)

        ses_label = Label(self.window, text="Senior Spring", font=self.my_big_font, fg="black", bg="#7CB9E8", borderwidth=2, relief="ridge")
        ses_label.grid(row=21, column=10)
        self.ses_cu = StringVar()
        self.ses_cu.set("0 CU")
        self.ses_cu_label = Label(self.window, textvariable=self.ses_cu, font=self.my_small_font, fg="black", bg="#80FFD4", relief="sunken")
        self.ses_cu_label.grid(row=21, column = 11)
        self.list_senior_spring = Listbox(self.window, height=6, width = 40, font=self.my_small_font)
        self.list_senior_spring.grid(row=22, column=9, rowspan = 6, columnspan=3)
        self.list_senior_spring.bind('<<ListboxSelect>>', self.get_selected_ses)

        ## creates scrollbar
        self.sb1=Scrollbar(self.window)
        self.sb1.grid(row=8, column=2, rowspan=6)

        self.list_all.configure(yscrollcommand=self.sb1.set)
        self.sb1.configure(command=self.list_all.yview)

        ## buttons
        self.add_button = ttk.Button(self.window, text="Add Course", width = 16, command=self.add_command)
        self.add_button.grid(row=5, column=0)
        self.remove_button = ttk.Button(self.window, text="Remove Course", width = 16, command=self.del_command)
        self.remove_button.grid(row=5, column=1)

        self.push_button = ttk.Button(self.window, text="Push to Plan", width = 16, command = self.push_command)
        self.push_button.grid(row=24, column=0)
        self.pull_button = ttk.Button(self.window, text="Pull to Cart", width = 16, command = self.pull_command)
        self.pull_button.grid(row=25, column=0)


        self.load_button = ttk.Button(self.window, text="Load", width = 16, command = self.load_command)
        self.load_button.grid(row = 26, column=0, columnspan=1)
        self.save_button = ttk.Button(self.window, text="Save", width = 16, command = self.save_command)
        self.save_button.grid(row = 27, column=0, columnspan=1)
        self.close_button = ttk.Button(self.window, text="Close", width = 16, command = self.close_command)
        self.close_button.grid(row = 26, column=1, rowspan=2)

        # semester toggle
        self.semester_var = StringVar()
        # self.semester_var.set("Freshman Fall")
        semester_choice = OptionMenu(self.window, self.semester_var, "Freshman Fall", "Freshman Spring",
                    "Sophomore Fall", "Sophomore Spring",
                    "Junior Fall", "Junior Spring",
                    "Senior Fall", "Senior Spring")
        semester_choice.config(width=13)
        semester_choice.grid(row = 25, column = 1, columnspan = 1)
        Label(self.window, text="Choose Semester", font=("Gobold", 9), width = 17, fg="black", bg="#7CB9E8", borderwidth=2, relief="ridge").grid(row=24, column =1)
        self.window.mainloop()

    ## Selection

    def get_selected_row(self, event): 
        try:
            # global selected_tuple
            self.index = self.list_all.curselection()[0]
            self.selected_tuple = self.list_all.get(self.index)
            ## puts name of selected course in entries
            self.code_entry.delete(0, END)
            self.code_entry.insert(END, self.selected_tuple[0])
            self.course_entry.delete(0, END)
            self.course_entry.insert(END, self.selected_tuple[1])
            self.credit_entry.delete(0, END)
            self.credit_entry.insert(END, self.selected_tuple[2])
        except IndexError:
            pass

    def get_selected_ff(self, event):
        try:
            self.planned_index = self.list_freshman_fall.curselection()[0]
            self.planned_tuple = self.list_freshman_fall.get(self.planned_index)
            # TODO
        except IndexError:
            pass

    def get_selected_fs(self, event):
        try:
            self.planned_index = self.list_freshman_spring.curselection()[0]
            self.planned_tuple = self.list_freshman_spring.get(self.planned_index)
            # TODO
        except IndexError:
            pass
    
    def get_selected_sf(self, event):
        try:
            self.planned_index = self.list_sophomore_fall.curselection()[0]
            self.planned_tuple = self.list_sophomore_fall.get(self.planned_index)
            # TODO
        except IndexError:
            pass

    def get_selected_ss(self, event):
        try:
            self.planned_index = self.list_sophomore_spring.curselection()[0]
            self.planned_tuple = self.list_sophomore_spring.get(self.planned_index)
            # TODO
        except IndexError:
            pass

    def get_selected_jf(self, event):
        try:
            self.planned_index = self.list_junior_fall.curselection()[0]
            self.planned_tuple = self.list_junior_fall.get(self.planned_index)
            # TODO
        except IndexError:
            pass
    
    def get_selected_js(self, event):
        try:
            self.planned_index = self.list_junior_spring.curselection()[0]
            self.planned_tuple = self.list_junior_spring.get(self.planned_index)
            # TODO
        except IndexError:
            pass

    def get_selected_sef(self, event):
        try:
            self.planned_index = self.list_senior_fall.curselection()[0]
            self.planned_tuple = self.list_senior_fall.get(self.planned_index)
            # TODO
        except IndexError:
            pass

    def get_selected_ses(self, event):
        try:
            self.planned_index = self.list_senior_spring.curselection()[0]
            self.planned_tuple = self.list_senior_spring.get(self.planned_index)
            # TODO
        except IndexError:
            pass

    ## Helpers

    def list_reset(self):
        self.ff_list = []
        self.fs_list = []
        self.sf_list = []
        self.ss_list = []
        self.jf_list = []
        self.js_list = []
        self.sef_list = []
        self.ses_list = []

    def list_sort(self, l):
        codes = []
        copy = l
        for item in l:
            codes.append(item[0])
        codes.sort()
        li=[]
        for item in codes:
            for c in copy:
                if c[0]==item:
                    li.append(c)
        return li
        
    def update_CU(self):
        ff_count = float(0.0)
        for c in self.ff_list:
            ff_count += c[2]
        self.ff_cu.set(str(ff_count) + " CU")

        fs_count = float(0.0)
        for c in self.fs_list:
            fs_count += c[2]
        self.fs_cu.set(str(fs_count) + " CU")

        sf_count = float(0.0)
        for c in self.sf_list:
            sf_count += c[2]
        self.sf_cu.set(str(sf_count) + " CU")

        ss_count = float(0.0)
        for c in self.ss_list:
            ss_count += c[2]
        self.ss_cu.set(str(ss_count) + " CU")

        jf_count = float(0.0)
        for c in self.jf_list:
            jf_count += c[2]
        self.jf_cu.set(str(jf_count) + " CU")

        js_count = float(0.0)
        for c in self.js_list:
            js_count += c[2]
        self.js_cu.set(str(js_count) + " CU")

        sef_count = float(0.0)
        for c in self.sef_list:
            sef_count += c[2]
        self.sef_cu.set(str(sef_count) + " CU")

        ses_count = float(0.0)
        for c in self.ses_list:
            ses_count += c[2]
        self.ses_cu.set(str(ses_count) + " CU")

    ## Commands

    def view_command(self):
        self.list_all.delete(0, END)
        for c in self.course_list:
            self.list_all.insert(END, c)

        self.list_freshman_fall.delete(0, END)
        for c in self.ff_list:
            self.list_freshman_fall.insert(END, c)

        self.list_freshman_spring.delete(0, END)
        for c in self.fs_list:
            self.list_freshman_spring.insert(END, c)

        self.list_sophomore_fall.delete(0, END)
        for c in self.sf_list:
            self.list_sophomore_fall.insert(END, c)

        self.list_sophomore_spring.delete(0, END)
        for c in self.ss_list:
            self.list_sophomore_spring.insert(END, c)

        self.list_junior_fall.delete(0, END)
        for c in self.jf_list:
            self.list_junior_fall.insert(END, c)

        self.list_junior_spring.delete(0, END)
        for c in self.js_list:
            self.list_junior_spring.insert(END, c)

        self.list_senior_fall.delete(0, END)
        for c in self.sef_list:
            self.list_senior_fall.insert(END, c)

        self.list_senior_spring.delete(0, END)
        for c in self.ses_list:
            self.list_senior_spring.insert(END, c)

        self.update_CU()
       
    def add_command(self):
        self.list_all.delete(0, END)
        if self.course_text.get() == "" or self.code_text.get() == ""  or self.credit_text.get() == "":
            messagebox.showinfo("Error", "Make sure you include all fields")
        else:
            try:
                exists = False
                if (not len(self.course_list) == 0 and len(self.ff_list) == 0 and len(self.fs_list)) == 0:
                    for c in self.course_list:
                        if self.code_text.get().upper() == c[0] or self.course_text.get().upper() == c[1]:
                            exists = True
                            break
                    for c in self.ff_list:
                        if exists:
                            break
                        if self.code_text.get().upper() == c[0] or self.course_text.get().upper() == c[1]:
                            exists = True
                    for c in self.fs_list:
                        if exists:
                            break
                        if self.code_text.get().upper() == c[0] or self.course_text.get().upper() == c[1]:
                            exists = True
                    for c in self.sf_list:
                        if exists:
                            break
                        if self.code_text.get().upper() == c[0] or self.course_text.get().upper() == c[1]:
                            exists = True
                    for c in self.ss_list:
                        if exists:
                            break
                        if self.code_text.get().upper() == c[0] or self.course_text.get().upper() == c[1]:
                            exists = True
                    for c in self.jf_list:
                        if exists:
                            break
                        if self.code_text.get().upper() == c[0] or self.course_text.get().upper() == c[1]:
                            exists = True
                    for c in self.sef_list:
                        if exists:
                            break
                        if self.code_text.get().upper() == c[0] or self.course_text.get().upper() == c[1]:
                            exists = True
                    for c in self.ses_list:
                        if exists:
                            break
                        if self.code_text.get().upper() == c[0] or self.course_text.get().upper() == c[1]:
                            exists = True
                if (not exists):
                    self.course_list.append([self.code_text.get().upper(), self.course_text.get().upper(), round(float(self.credit_text.get()),1)])
                else:
                    messagebox.showinfo("Error", "This course has already been added...")
                # self.list_all.insert(END, (self.code_text.get(), self.course_text.get(), self.credit_text.get()))
            except:
                 messagebox.showinfo("Error", "There is something wrong with your entries")
            self.course_list = self.list_sort(self.course_list)
            self.view_command()
    
    def del_command(self):
        print(self.code_text.get(), self.course_text.get(), self.credit_text.get())
        for c in self.course_list:
            if c[0] == self.selected_tuple[0] and c[1] == self.selected_tuple[1] and c[2] == self.selected_tuple[2]:
                self.course_list.remove(c)
        self.selected_tuple = ()
        self.view_command()
  
    def push_command(self):
        try:
            course = [self.selected_tuple[0], self.selected_tuple[1], self.selected_tuple[2]]
            for c in self.course_list:
                if c == course:
                    if self.semester_var.get() == "Freshman Fall":
                        self.ff_list.append(course)
                        self.ff_list = self.list_sort(self.ff_list)
                    elif self.semester_var.get() == "Freshman Spring":
                        self.fs_list.append(course)
                        self.fs_list = self.list_sort(self.fs_list)
                    elif self.semester_var.get() == "Sophomore Fall":
                        self.sf_list.append(course)
                        self.sf_list = self.list_sort(self.sf_list)
                    elif self.semester_var.get() == "Sophomore Spring":
                        self.ss_list.append(course)
                        self.ss_list = self.list_sort(self.ss_list)
                    elif self.semester_var.get() == "Junior Fall":
                        self.jf_list.append(course)
                        self.jf_list = self.list_sort(self.jf_list)
                    elif self.semester_var.get() == "Junior Spring":
                        self.js_list.append(course)
                        self.js_list = self.list_sort(self.js_list)
                    elif self.semester_var.get() == "Senior Fall":
                        self.sef_list.append(course)
                        self.sef_list = self.list_sort(self.sef_list)
                    elif self.semester_var.get() == "Senior Spring":
                        self.ses_list.append(course)
                        self.ses_list = self.list_sort(self.ses_list)
                    self.course_list.remove(course)
                self.selected_tuple = ()
            self.view_command()          
        except IndexError:
            messagebox.showinfo("Error", "Something went wrong...")

    def pull_command(self):
        try:
            course = [self.planned_tuple[0], self.planned_tuple[1], self.planned_tuple[2]]
            if course in self.ff_list:
                self.ff_list.remove(course)
            elif course in self.fs_list:
                self.fs_list.remove(course)
            elif course in self.sf_list:
                self.sf_list.remove(course)
            elif course in self.ss_list:
                self.ss_list.remove(course)
            elif course in self.jf_list:
                self.jf_list.remove(course)
            elif course in self.js_list:
                self.js_list.remove(course)
            elif course in self.sef_list:
                self.sef_list.remove(course)
            elif course in self.ses_list:
                self.ses_list.remove(course)

            self.course_list.append(course)
            self.view_command()

        except IndexError:
            pass
    
    def save_command(self):
        all_list = ["cart"]
        for c in self.course_list:
            all_list.append(c[0] + "," + c[1] + "," + str(c[2]))
        all_list.append("ff")
        for c in self.ff_list:
            all_list.append(c[0] + "," + c[1] + "," + str(c[2]))
        all_list.append("fs")
        for c in self.fs_list:
            all_list.append(c[0] + "," + c[1] + "," + str(c[2]))
        all_list.append("sf")
        for c in self.sf_list:
            all_list.append(c[0] + "," + c[1] + "," + str(c[2]))
        all_list.append("ss")
        for c in self.ss_list:
            all_list.append(c[0] + "," + c[1] + "," + str(c[2]))
        all_list.append("jf")
        for c in self.jf_list:
            all_list.append(c[0] + "," + c[1] + "," + str(c[2]))
        all_list.append("js")
        for c in self.js_list:
            all_list.append(c[0] + "," + c[1] + "," + str(c[2]))
        all_list.append("sef")
        for c in self.sef_list:
            all_list.append(c[0] + "," + c[1] + "," + str(c[2]))
        all_list.append("ses")
        for c in self.ses_list:
            all_list.append(c[0] + "," + c[1] + "," + str(c[2]))
        with open("plan_save.txt", "w") as file:
            file.truncate(0)
            for x in all_list:
                file.write(x + "\n")
            file.close()
        print("Saved")
        
    def close_command(self):
        self.save()
        self.window.destroy()

    def load_command(self):
        with open("plan_save.txt", "r") as file:

            status = ""
            curr = file.readline()
            self.course_list = []
            self.list_reset()
            while curr:
                if curr=="cart\n" or curr=="ff\n" or curr=="fs\n" or curr=="sf\n" or curr=="ss\n" or curr=="jf\n" or curr=="js\n" or curr=="sef\n" or curr=="ses\n":
                    status = curr[:-1]
                else:
                    course = []
                    line = curr.split(",")
                    course.append(line[0])
                    course.append(line[1])
                    course.append(round(float(line[2][:-1]), 2))
                    if status=="cart":
                        self.course_list.append(course)
                    if status=="ff":
                        self.ff_list.append(course)
                    elif status=="fs":
                        self.fs_list.append(course)
                    elif status=="sf":
                        self.sf_list.append(course)
                    if status=="ss":
                        self.ss_list.append(course)
                    if status=="jf":
                        self.jf_list.append(course)
                    if status=="js":
                        self.js_list.append(course)
                    if status=="sef":
                        self.sef_list.append(course)
                    if status=="ses":
                        self.ses_list.append(course)
                curr = file.readline()
            file.close()
            self.view_command()

planner = Frontend()

