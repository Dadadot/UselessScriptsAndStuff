import tkinter as tk

class Omnicalc(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Omnicalc")
        
        self.widget_dict = {"Navigation":(Navigation, "300x100"), "CalcRemainder":(CalcRemainder, "300x600" ), "NumbersystemConversion":(NumbersystemConversion, "300x300")}
        self.open_widget = False
        self.create_widget("Navigation")

    def create_widget(self, widget_name_in):
        widget_name = self.widget_dict[widget_name_in][0]
        if self.open_widget is not False:
            self.open_widget.destroy()
        self.geometry(self.widget_dict[widget_name_in][1])
        self.open_widget = widget_name(self)
        self.open_widget.pack(expand=True)
        self.title(widget_name_in + " - Omnicalc")


class Navigation(tk.Frame):
    
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.nav_choice = tk.StringVar()
        
        nav_choice1 = tk.Radiobutton(self, text="CalcRemainder", variable=self.nav_choice, value="CalcRemainder", height=1, width=25).grid(row=1, column=0, stick=tk.E)
        nav_choice1 = tk.Radiobutton(self, text="NumbersystemConversion", variable=self.nav_choice, value="NumbersystemConversion", height=1, width=25).grid(row=2, column=0, stick=tk.E)
    
        open_button = tk.Button(self, text="Open", command=self.open_choice)
        open_button.grid(row=10, column=0)
        quit_button = tk.Button(self, text="Quit", command=parent.destroy)
        quit_button.grid(row=10, column=1)

    def open_choice(self):
        choice = self.nav_choice.get()
        self.parent.create_widget(choice)

class CalcRemainder(tk.Frame):
        
        # self.container.pack(side="top", fill="both", expand=True)
        # self.container.grid_rowconfigure(0, weight=1)
        # self.container.grid_columnconfigure(0, weight=1)

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        
        #Vars
        self.number_sys = tk.IntVar()
        self.entry_number = tk.IntVar()
        #Number System Chooser
        numbersys_frame = tk.Frame(self)
        numbersys_label = tk.Label(numbersys_frame, text="Chose numbersystem to convert to:").grid(row=0, column=0, columnspan=4)
        c_button1 = tk.Radiobutton(numbersys_frame, text="Bin", variable=self.number_sys, value="2", height=1, width=3).grid(row=1, column=0)
        c_button2 = tk.Radiobutton(numbersys_frame, text="Oct", variable=self.number_sys, value="8", height=1, width=3).grid(row=1, column=1)
        c_button3 = tk.Radiobutton(numbersys_frame, text="Hex", variable=self.number_sys, value="16", height=1, width=3).grid(row=1, column=2)
        numbersys_frame.pack()
        #Number Entry + Calc Button
        number_entry_frame = tk.Frame(self)
        number_entry_label = tk.Label(number_entry_frame, text="Enter Number:")
        number_entry_label.grid(row=2, column=0)
        number_entry = tk.Entry(number_entry_frame, textvariable=self.entry_number, width=10)
        number_entry.grid(row=2, column=1)
        number_entry.delete(0, "end") #clear out number entry, starts with 0 for whatever reason
        calculate_button = tk.Button(number_entry_frame, text="Calucate", command=self.print_textbox)
        calculate_button.grid(row=3, column=0, columnspan=4)
        number_entry_frame.pack()
        #Calculate Textbox
        calc_text_frame = tk.Frame(self)
        self.calc_text = tk.Text(calc_text_frame, height=20, width=30, state="disabled")
        self.calc_text.pack()
        calc_text_frame.pack()
        #Quit Button
        nav_frame = tk.Frame(self)
        back_button = tk.Button(nav_frame, text="Back", command=lambda: parent.create_widget("Navigation"))
        back_button.grid(row=0, column=0)
        quit_button = tk.Button(nav_frame, text="Quit", command=parent.destroy)
        quit_button.grid(row=0, column=1)
        nav_frame.pack()

    @staticmethod
    def calc_remainder(num_in, number_sys_in):
        if number_sys_in == 0:
            return
        rest_out = num_in % number_sys_in
        num_in = (num_in - rest_out) / number_sys_in
        return rest_out, num_in

    def create_calc(self, num_in, number_sys_in):
        print_remainders = []
        print_numbers = []
        number_orig = num_in
        while True:
            rest_tmp, num_in = self.calc_remainder(num_in, number_sys_in)
            print_remainders.append(int(rest_tmp))
            print_numbers.append(int(num_in))
            if num_in == 0:
                break
        return number_orig, print_numbers, print_remainders

    def clear_textbox(self):
        self.calc_text.configure(state="normal")
        self.calc_text.delete(1.0, tk.END)
        self.calc_text.configure(state="disabled")

    def insert_textbox(self, text_in):
        self.calc_text.configure(state="normal")
        self.calc_text.insert(tk.INSERT, str(text_in) + "\n")
        self.calc_text.configure(state="disabled")

    def print_textbox(self):
        self.clear_textbox()
        number_orig, numbers, remainders = self.create_calc(self.entry_number.get(), self.number_sys.get())
        self.insert_textbox(number_orig)
        for i in range(0, len(numbers)):
            self.insert_textbox(str(numbers[i]) + "\t\t" + str(hex(remainders[i])).upper().replace("0X",""))

class NumbersystemConversion(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        #Var
        self.number_sys_in = tk.IntVar()
        self.number_sys_out = tk.IntVar()
        self.entry_number = tk.StringVar()
        label = tk.Label(self, text="!!! Not type checking whatsoever !!!").pack()

        #Number System In Chooser
        numbersys_in_frame = tk.Frame(self)
        numbersys_label = tk.Label(numbersys_in_frame, text="Chose input numbersystem:").grid(row=0, column=0, columnspan=4)
        c_button1 = tk.Radiobutton(numbersys_in_frame, text="Bin", variable=self.number_sys_in, value="2", height=1, width=3).grid(row=1, column=0)
        c_button2 = tk.Radiobutton(numbersys_in_frame, text="Oct", variable=self.number_sys_in, value="8", height=1, width=3).grid(row=1, column=1)
        c_button2 = tk.Radiobutton(numbersys_in_frame, text="Dec", variable=self.number_sys_in, value="10", height=1, width=3).grid(row=1, column=2)
        c_button3 = tk.Radiobutton(numbersys_in_frame, text="Hex", variable=self.number_sys_in, value="16", height=1, width=3).grid(row=1, column=3)
        numbersys_in_frame.pack()

        #Number System Out Chooser
        numbersys_out_frame = tk.Frame(self)
        numbersys_label = tk.Label(numbersys_out_frame, text="Chose output numbersystem:").grid(row=0, column=0, columnspan=4)
        c_button1 = tk.Radiobutton(numbersys_out_frame, text="Bin", variable=self.number_sys_out, value="2", height=1, width=3).grid(row=1, column=0)
        c_button2 = tk.Radiobutton(numbersys_out_frame, text="Oct", variable=self.number_sys_out, value="8", height=1, width=3).grid(row=1, column=1)
        c_button2 = tk.Radiobutton(numbersys_out_frame, text="Dec", variable=self.number_sys_out, value="10", height=1, width=3).grid(row=1, column=2)
        c_button3 = tk.Radiobutton(numbersys_out_frame, text="Hex", variable=self.number_sys_out, value="16", height=1, width=3).grid(row=1, column=3)
        numbersys_out_frame.pack()

        #Numberentry + Calucate Button
        numbers_frame = tk.Frame(self)
        number_entry = tk.Entry(numbers_frame, textvariable=self.entry_number, width=30)
        number_entry.pack()
        number_entry.delete(0, "end")
        calc_button = tk.Button(numbers_frame, text="Calucate", command=self.print_number).pack()
        numbers_frame.pack()

        self.calc_text = tk.Text(self, height=1, width=30, state="disabled")
        self.calc_text.pack()

        #Quit Button
        nav_frame = tk.Frame(self)
        back_button = tk.Button(nav_frame, text="Back", command=lambda: parent.create_widget("Navigation"))
        back_button.grid(row=0, column=0)
        quit_button = tk.Button(nav_frame, text="Quit", command=parent.destroy)
        quit_button.grid(row=0, column=1)
        nav_frame.pack()

    def clear_textbox(self):
        self.calc_text.configure(state="normal")
        self.calc_text.delete(1.0, tk.END)
        self.calc_text.configure(state="disabled")

    def insert_textbox(self, text_in):
        self.calc_text.configure(state="normal")
        self.calc_text.insert(tk.INSERT, str(text_in) + "\n")
        self.calc_text.configure(state="disabled")

    #There are builtin ways in python to do this, all of this, but this is my function. There are many like it, but this one is mine.
    #My function is my best friend. It is my life. I must master it as I must master my life.
    #Without me, my function is useless. Without my function, I am useless.
    @staticmethod
    def to_dec(num_in, numsys_in):
        hex_conv = {"a":10, "b":11, "c":12, "d":13, "e":14, "f":15}
        num_in = num_in[::-1].lower()
        num_out = 0
        for index, number in enumerate(num_in):
            try: number = int(number)
            except ValueError:
                number = hex_conv[number]
            number = number * (numsys_in ** index)
            num_out += number
        return num_out

    @staticmethod
    def to_output_numsys(number_in, numsys_in):
        num_sys_dict = {2:bin, 8:oct, 10:int, 16:hex}
        return num_sys_dict[numsys_in](number_in)

    def print_number(self):
        tmp_num = self.entry_number.get()
        nsi = self.number_sys_in.get()
        nso = self.number_sys_out.get()
        tmp_num = self.to_dec(tmp_num, nsi)
        tmp_num = self.to_output_numsys(tmp_num, nso)
        self.clear_textbox()
        self.insert_textbox(tmp_num)
