import random
"""game_of_life.py 
Requires grid dict of board on init. 
MainApp calls next_state(grid, black_tiles)
"""


class GameOfLife:
    """Game Of Life
    Attributes:
        grid: passed from app, {(x, y): item_id, ...}

    Methods:
        init_board_state

    Note: grid[x,y] = id, black_tiles = ((ids),...)
        coords must be matched with grid[x,y] to return [ids,]
    """
    def __init__(self, grid, cells):
        self.grid = grid
        # Assuming grid == Square!
        self.y_height = len(cells) - 1
        self.x_width = len(cells[0]) - 1

        # self.start_width = max(max(grid.keys()))
        # self.start_height = max(max(grid.keys()))

        self.initial_coord_ids = self.return_ids(cells)

    def count_neighbors(self, x, y, grid, black_tiles):
        """Given board, and x,y coords - counts surrounding neighbors
        Returns: count of alive_neighbors
        """
        # Index values for grid
        x_bound = self.x_width
        y_bound = self.y_height
        alive_neighbors = 0

        # Set Horizontal, Vertical, RDIAG, LDIAG directions
        for delta_x, delta_y in [(1, 0), (0, 1), (1, 1), (-1, 1)]:
            # Set delta for +- directions
            for delta in (1, -1):
                delta_x *= delta  # (1*1); (1+-1); (0*1); (0*-1) ...
                delta_y *= delta  # (0*1); (0*-1); (1*1); (1*-1) ...
                next_x = x + delta_x  # = 1; -1; 0; 0; ...
                next_y = y + delta_y  # = 0, 0; 1; -1; ...

                # Only one step each delta_direction
                # y_bound is KeyError for AutomataBot
                if 0 <= next_y < y_bound and 0 <= next_x < x_bound:

                    # if (next_x, next_y) coords in black_tiles
                    if grid[next_y, next_x] in black_tiles:
                        alive_neighbors += 1

        return alive_neighbors

    def next_state(self, black_tiles):
        """Returns next state, given dict of grid {(x,y):id, ...}"""
        rtn_ids = []

        # If initial, use init_coords
        if self.initial_coord_ids:
            rtn_ids = self.initial_coord_ids.copy()
        if rtn_ids:
            self.initial_coord_ids.clear()
            return rtn_ids

        for i in range(self.x_width):
            for j in range(self.y_height):
                # count alive neighbors
                alive_nei = self.count_neighbors(x=i, y=j, grid=self.grid, black_tiles=black_tiles)

                if alive_nei < 2 and self.grid[j, i] in black_tiles:  # dies
                    rtn_ids.append(self.grid[j, i])
                elif alive_nei == 3 and self.grid[j, i] not in black_tiles:  # revives
                    rtn_ids.append(self.grid[j, i])
                elif alive_nei > 3 and self.grid[j, i] in black_tiles:  # starves
                    rtn_ids.append(self.grid[j, i])
                else:
                    pass  # no change

        return rtn_ids

    def return_ids(self, state):
        """Returns list of tuples of [(x,y),...]
        Only useful for randomisation of entire grid convert.
        """
        rtn_list = []
        # iterate over entire initial
        for i, row in enumerate(state):
            for j, col_el in enumerate(row):
                if col_el == 1:  # its a color tile
                    rtn_list.append(self.grid[i, j])  # get id

        return rtn_list

    def initialize_board_state(self):
        """Randomizes grid into list of lists.
        Returns: state=[[1,0,1],...]
        """
        n = self.x_width
        m = self.y_height
        # n, m = 30, 30

        total_length = n * m
        r = []
        for i in range(total_length):
            r.append(random.choice([0, 1]))
        state = [r[i:i + n] for i in range(0, len(r), n)]  # cool list slice comp
        return state

    # def build_dead_state(cols=6, rows=6):
    #     # board_state = [[None]*cols]* rows # creating linked lists!!!
    #     state = []
    #     for i in range(cols):
    #         state.append([])
    #         for j in range(rows):
    #             state[i].append(0)
    #     return state
