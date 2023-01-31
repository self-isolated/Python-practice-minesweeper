import tkinter.messagebox
from tkinter import Label, Entry, Button,  Tk
from game_pack.Core import Core

class Dialog_Box:
    # state==0 - non-existence of window
    # state==1 - existance of window
    __Dialog_Box_state=0
    __Core_state=0
    def __init__(self,window):
        self.window=window
        self.window.config(bg="black")
        self.rows=0
        self.columns=0
        self.bomb_amount=0
        self.core_window=None
        self.window_elements()

    def window_elements(self):
        self.row_label=Label(self.window,
                          text='podaj ilosc wierszy:',
                          font=('Arial',10,'bold'),
                          bg="black",
                          fg='green')

        self.row_entry=Entry(self.window,
                             bg="black",
                             fg='green')


        self.column_label=Label(self.window,
                          text='podaj ilosc kolumn:',
                          font=('Arial',10,'bold'),
                          bg="black",
                          fg='green')

        self.column_entry=Entry(self.window, bg="black", fg='green')

        self.bomb_label = Label(self.window, text='podaj ilosc bomb:',
                            font=('Arial', 10, 'bold'),
                            bg="black",
                            fg='green')

        self.bomb_entry = Entry(self.window, bg="black", fg='green')

        self.game_button=Button(self.window,text="zatwierdz parametry",command=self.function,bg="black", fg='green')


        self.row_label.pack()
        self.row_entry.pack()

        self.column_label.pack()
        self.column_entry.pack()

        self.bomb_label.pack()
        self.bomb_entry.pack()

        self.game_button.pack()

    def function(self):
        try:
            self.columns= int(self.column_entry.get())
            self.rows= int(self.row_entry.get())
            self.bomb_amount= int(self.bomb_entry.get())


        except:
            msg = tkinter.messagebox.showerror("Zla wartosc", "wprowadziles wartosc niebedaca liczba")
        else:
            self.check_input_params_span()

            Dialog_Box.__Dialog_Box_state = 1
    def check_input_params_span(self):

        if Dialog_Box.check_safety_gameboard_size(self.rows,self.columns) and Dialog_Box.check_safety_bomb_amount(self.bomb_amount,self.rows,self.columns):

            self.create_core_and_close()

        else:
            msg = tkinter.messagebox.showerror("Zla wartosc",
                                               "wprowadziles wartosc poza zakresem- od 1 do 20 lub za duzo bomb")

    def create_core_and_close(self):
        self.core_window = Tk()
        self.core = Core(self.core_window, self.rows, self.columns, self.bomb_amount)
        self.core_window.protocol('WM_DELETE_WINDOW', self.remove_core_window)
        Dialog_Box.__Core_state = 1
        self.window.destroy()

    def remove_core_window(self):
        self.core_window.destroy()
        self.core_window = None
        Dialog_Box.__Core_state=0

    @staticmethod
    def check_safety_gameboard_size(rows,columns):
        return bool(columns < 13 and columns > 0 and rows < 13 and rows > 0)

    @staticmethod
    def check_safety_bomb_amount(bomb_amount,rows,columns):
        return bool(bomb_amount > 0 and bomb_amount < (columns * rows))

    @staticmethod
    def get_state_Dialog():
        return Dialog_Box.__Dialog_Box_state

    @staticmethod
    def set_state_zero_Dialog():
        Dialog_Box.__Dialog_Box_state=0

    @staticmethod
    def get_state_Core():
        return Dialog_Box.__Core_state

    @staticmethod
    def set_state_zero_Core():
        Dialog_Box.__Core_state = 0