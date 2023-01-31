import tkinter.messagebox
from tkinter import Label, Button, Tk
from game_pack.Dialog_Box import Dialog_Box

class Game:

    def __init__(self, window):

        self.window = window
        self.window.title('SAPER')
        self.window.config(background='black')
        self.parent_Dialog_window=None
        self.Dialog_Box_window=None
        self.main_label= Label(self.window, text=
        """
        ────────────────────────────────────────────────────────────────────────────────
        ─██████████████─██████████████─██████████████─██████████████─████████████████───
        ─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██───
        ─██░░██████████─██░░██████░░██─██░░██████░░██─██░░██████████─██░░████████░░██───
        ─██░░██─────────██░░██──██░░██─██░░██──██░░██─██░░██─────────██░░██────██░░██───
        ─██░░██████████─██░░██████░░██─██░░██████░░██─██░░██████████─██░░████████░░██───
        ─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██───
        ─██████████░░██─██░░██████░░██─██░░██████████─██░░██████████─██░░██████░░████───
        ─────────██░░██─██░░██──██░░██─██░░██─────────██░░██─────────██░░██──██░░██─────
        ─██████████░░██─██░░██──██░░██─██░░██─────────██░░██████████─██░░██──██░░██████─
        ─██░░░░░░░░░░██─██░░██──██░░██─██░░██─────────██░░░░░░░░░░██─██░░██──██░░░░░░██─
        ─██████████████─██████──██████─██████─────────██████████████─██████──██████████─
        ────────────────────────────────────────────────────────────────────────────────

        Instrukcja:

                Klikajac raz lewym na danym polu pojawia sie znak ? oznaczajacy podejrzane pole,
                klikajac drugi raz pole odkrywa się, pokazując ile min z danym polem sąsiaduje.
                Aby wygrać należy okryc wszytkie pola bez min.
        """,
                                justify="center",
                                font=('Arial', 10, 'bold'),
                                bg='black',
                                fg='green')
        self.start = Button(self.window,
                           text='podaj parametry gry',
                           bg='black', fg='green',
                           highlightbackground='black',
                        command=self.check_existing_windows)

        self.main_label.pack()
        self.start.pack()


    def check_existing_windows(self):
        if Dialog_Box.get_state_Core()==1:
            msg = tkinter.messagebox.showerror("Blokada", "Zamknij najpierw istaniejace okno gry")
        else:
            self.clear_state_Dialog_Box()
            self.create_Dialog_Box()

    def clear_state_Dialog_Box(self):
        if Dialog_Box.get_state_Dialog() == 1:
            Dialog_Box.set_state_zero_Dialog()
            self.parent_Dialog_window = None

    def create_Dialog_Box(self):
        if self.parent_Dialog_window is None:
            self.parent_Dialog_window = Tk()
            self.Dialog_Box_window = Dialog_Box(self.parent_Dialog_window)
            self.parent_Dialog_window.protocol('WM_DELETE_WINDOW', self.remove_parent_window)

    def remove_parent_window(self):
        self.parent_Dialog_window.destroy()
        self.parent_Dialog_window = None

if __name__ == "__main__":
    window = Tk()
    game = Game(window)
    window.mainloop()