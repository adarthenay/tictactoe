class Board(object):
    def __init__(self, init_value="000 000 000"):
        self.grid = self._parse_init_value(init_value)
        
    def is_empty(self):
        for line in self.grid:
            for item in line:
                if item != 0:
                    return False
        return True
        
    def _parse_init_value(self, init_value):
        grid = []
        for str_line in init_value.strip().split(' '):
            line = []
            if len(str_line.strip()) > 0:
                for char in str_line.strip():
                    line.append(int(char))
                grid.append(line)
        return grid
        
    def winner(self):
        lines = self._winner_lines()
        if lines != 0:
            return lines
        columns = self._winner_columns()
        if columns != 0:
            return columns
        diagonal = self._winner_diagonal()
        if diagonal != 0:
            return diagonal
        adiagonal = self._winner_adiagonal()
        return self._winner_adiagonal()
        
    def _winner_lines(self):
        for line in self.grid:
            if line in [ [1]*len(line), [2]*len(line)]:
                return line[0]
        return 0
        
    def _winner_columns(self):
        for index, item in enumerate(self.grid[0]):
            line = [ self.grid[i][index] for i in range(len(self.grid)) ]
            if line in [ [1]*len(line), [2]*len(line)]:
                return line[0]
        return 0
        
    def _winner_diagonal(self):
        for index, item in enumerate(self.grid[0]):
            line = [ self.grid[i][i] for i in range(len(self.grid)) ]
            if line in [ [1]*len(line), [2]*len(line)]:
                return line[0]
        return 0
        
    def _winner_adiagonal(self):
        for index, item in enumerate(self.grid[0]):
            line = [ self.grid[i][len(self.grid)-i-1] for i in range(len(self.grid)) ]
            if line in [ [1]*len(line), [2]*len(line)]:
                return line[0]
        return 0
        
            