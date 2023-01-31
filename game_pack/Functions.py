import random

class Function:
    @staticmethod
    def set_cell_value(cell_row, cell_column,bomb_list,bomb_symbol):
        if [cell_row, cell_column] in bomb_list:
            cell_value = bomb_symbol

        else:
            cell_value=Function.count_neighbor_bombs(cell_row,cell_column,bomb_list)

        return cell_value
    @staticmethod
    def count_neighbor_bombs(cell_row,cell_column,bomb_list):
        cell_value=0
        for row in range(-1, 2):
            for col in range(-1, 2):
                neighbor_row = cell_row + row
                neighbor_column = cell_column + col
                if [neighbor_row, neighbor_column] in bomb_list:
                    cell_value += 1
        return cell_value

    @staticmethod
    def make_bomb_list(rows,columns,ile_bomb):
        bomb_list=[]
        while len(bomb_list) < ile_bomb:
            row = random.choice([p for p in range(rows)])
            column = random.choice([p for p in range(columns)])
            if [row, column] not in bomb_list:
                bomb_list.append([row, column])
        bomb_list.sort()
        return bomb_list

