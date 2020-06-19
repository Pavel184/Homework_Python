# Pavel Krupenya
# Matrix
class Matrix:
    def __init__(self, *args):
        self.my_list = []
        for el in args:
            self.my_list.extend(el)

    def __add__(self, other):
        my_matr = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
        for i in range(len(self.my_list)):

            for j in range(len(other.my_list[i])):
                my_matr[i][j] = self.my_list[i][j] + other.my_list[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in my_matr]))


    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.my_list]))


m_obj_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m_obj_2 = Matrix([[10, 11, 12], [13, 14, 15], [16, 17, 18]])
print(m_obj_1, "\n")
print(m_obj_2, "\n")
print(m_obj_2 + m_obj_1, "\n")
input("\nPress Enter for exit")