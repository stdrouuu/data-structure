#Array 2 dimensi implementasi OOP

class Array(object):
    def __init__(self, size, fillValue=None):
        self.data = [fillValue] * size

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

    def __len__(self):
        return len(self.data)

    def __str__(self):
        return str(self.data)


class Grid(object):
    def __init__(self, rows, columns, fillValue=None):
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(columns, fillValue)

    def getHeight(self):
        return len(self.data)

    def getWidth(self):
        return len(self.data[0]) 

    def __getitem__(self, index):
        return self.data[index]

    def __str__(self):
        result = ""
        for row in range(self.getHeight()):
            for col in range(self.getWidth()):
                result += str(self.data[row][col]) + " "
            result += "\n"
        return result


# Example usage
arr_two = Grid(4, 5, 0)
print(arr_two)