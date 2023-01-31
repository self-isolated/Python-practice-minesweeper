from tkinter import Button, Label, Frame
from game_pack.Cell import Cell

class Core:

    def __init__(self, window, rows, columns, bomb_amount):
        self.window = window
        self.rows=rows
        self.columns=columns
        self.bomb_amount=bomb_amount
        self.window.config(bg='black')
        self.window.resizable(False, False)
        self.window.title('Game-Saper')

        self.board_elements()
        self.new_game()

    def board_elements(self):
        self.reset = Button(self.window, text='reset', command=self.new_game,bg="black",fg='green')
        self.reset.pack(side='bottom')

        self.label = Label(self.window, font=('consolas', 15), bg="black", fg='green')
        self.label.pack(side='top')

        self.label_counter=Label(self.window, font=('consolas', 15), bg="black", fg='green')
        self.label_counter.pack(side='top')

        self.frame = Frame(self.window, bg='grey')
        self.frame.pack()



    def new_game(self):
        self.label.config(text='Choose cell:')
        Cell.set_info_label(self.label)
        Cell.set_counter_label(self.label_counter)
        Cell.create_bomb_list(self.rows,self.columns,self.bomb_amount)
        self.cell_list= []
        self.setup_board_of_cells()

    def setup_board_of_cells(self):

        for row in range(self.rows):
            for column in range(self.columns):

                cell = Cell(row,column,self.frame)

                cell.button.grid(row=row, column=column)

                self.cell_list.append(cell)

                Cell.set_cell_list_and_counter(self.cell_list)
