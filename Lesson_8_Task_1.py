# Pavel Krupenya
# Date
class Date:
    def __init__(self, dd_mm_yy):
        self.dd_mm_yy = str(dd_mm_yy)

    @classmethod
    def convert(cls, dd_nn_yy):
        date = []
        for i in dd_nn_yy.split():
            if i != "-":
                date.append(i)
        return date

    @staticmethod
    def validation(day, month, year):
        if 1 <= day <= 31 and 1 <= month <= 12 and 0 <= year <= 2050:
            print(f"Date is valid")
        else:
            print("Date is incorrect")



    def __str__(self):
        return f"Date is {Date.convert(self.dd_mm_yy)}"

date = Date('05 - 02 - 2002')
print(date)
Date.validation(10, 9, 2000)
date.validation(10, 10, 20111)
print(Date.convert('11 - 11 - 11'))
print(date.convert('11 - 11 - 2020'))
Date.validation(1, 11, 2000)