from tkinter import Button
from game_pack.Functions import Function
from enum import Enum,auto

class Cell_state(Enum):
    blank=auto()
    suspect=auto()
    inactive=auto()

class Cell:

    __cell_list = []
    __bomb_symbol= "x"
    __suspect_sign='?'
    __info_label=None
    __counter_label = None
    __counter=0
    __bomb_amount=0
    __bomb_list=0


    def __init__(self,row,column,location):
        # state="blank" - uncovered cell -> click -> "suspect"
        # state="suspect" - suspect cell marked with suspect_sign -> click -> "inactive"
        # state="inactive" - exposed value and unresponsive cell
        self.state = Cell_state.blank
        self.row=row
        self.column=column
        self.button=self.create_button(location)
        self.value=Function.set_cell_value(self.row,self.column,Cell.__bomb_list,Cell.__bomb_symbol)

    def create_button(self,location):
        button=Button(location, text="",font=('consolas', 20), width=3, height=1,bg="#252525",fg="green",command=self.cell_action)
        return button

    def cell_action(self):
        if self.state == Cell_state.blank:

            self.action_for_blank()

        elif self.state==Cell_state.suspect:

            self.action_for_suspect()

    def action_for_blank(self):
        self.button.config(text=Cell.__suspect_sign)

        self.state = Cell_state.suspect

    def action_for_suspect(self):

        self.check_if_lose()
        if self.state != Cell_state.inactive:
            self.show_save_cell()

            self.check_if_win()

    def check_if_lose(self):
        if self.value==Cell.__bomb_symbol:
            self.button.config(text=self.value)
            Cell.end_reset('BUUUUUM! You lost!')

    def check_if_win(self):
        if Cell.__counter == 0:
            Cell.end_reset('You win!')

    def show_save_cell(self):
        if self.value == 0:

            self.recu_for_zero()

        else:
            self.button.config(text=self.value)
            self.deactivation()

        Cell.__counter_label.config(text=f"Remaining save cells: {Cell.__counter}")

    def recu_for_zero(self):
        if self.value == 0:
            self.button.config(text="",bg="black")
            self.check_neighbor()


    def check_neighbor(self):
        for row in range(-1,2):
            for col in range(-1,2):

                neighbor_row = self.row+ row
                neighbor_column = self.column+ col
                self.neighbor_action(neighbor_row,neighbor_column)

    def neighbor_action(self,row,column):
        for cell in Cell.__cell_list:
            if cell.check_cell_activity() and cell.row== row and cell.column== column:
                if cell.value != 0:
                    cell.button.config(text=cell.value)
                cell.deactivation()
                cell.recu_for_zero()

    def deactivation(self):
        self.state = Cell_state.inactive
        Cell.__counter -= 1


    def check_cell_activity(self):
        return bool(self.state == Cell_state.suspect or self.state == Cell_state.blank)


    @staticmethod
    def end_reset(text):
        Cell.__info_label.config(text=text)
        Cell.__counter_label.config(text=f"Remaining save cells: {Cell.__counter}")
        Cell.__counter = 0
        for cell in Cell.__cell_list: cell.state = Cell_state.inactive

    @staticmethod
    def set_cell_list_and_counter(list_cell):
        Cell.__cell_list = list_cell
        Cell.__counter=len(list_cell)-Cell.__bomb_amount
        Cell.__counter_label.config(text=f"Remaining save cells: {Cell.__counter}")

    @staticmethod
    def set_info_label(label):
        Cell.__info_label = label

    @staticmethod
    def set_counter_label(label):
        Cell.__counter_label = label

    @staticmethod
    def create_bomb_list(rows, columns,bomb_amount):
        Cell.__bomb_amount = bomb_amount
        Cell.__bomb_list=Function.make_bomb_list(rows,columns,bomb_amount)
