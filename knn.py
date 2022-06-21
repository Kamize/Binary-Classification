from openpyxl import Workbook, load_workbook
from pathlib import Path

# Paths for file processing
FOLDER_PATH = Path(__file__).parent
EXCEL_PATH = FOLDER_PATH/"traintest.xlsx"
OUTPUT_PATH = FOLDER_PATH/"kNN_result.xlsx"

K = 3

def main():
    # Loading bengkel.xlsx
    wb = load_workbook(EXCEL_PATH)
    train = wb["train"]
    test = wb["test"]

    # Getting data
    train_rows = train.rows
    test_rows = test.rows
    train_header = next(train_rows)
    test_header = next(test_rows)

    # Creating training data set from excel
    train_set = [Data(id = id.value, value = y.value, x1.value, x2.value, x3.value) for id, x1, x2, x3, y in train_rows]
    # test_set = [Data(id = id.value, value = y.value, x1.value, x2.value, x3.value) for id, x1, x2, x3, y in train_rows]
    test_set = []

    # kNN
    for test_data in test_set:
        test_data.value = kNN(test_data, train_set)

    # Closing excel file
    wb.close()



class Data():
    def __init__(self, id,  *args, value=None):
        self.id = id
        self.value = value
        self.coords = []
        for point in args:
            self.coords.append(point)

def euclidian_distance(data1, data2):
    sum = 0
    for point1, point2 in zip(data1.coords, data2.coords):
        sum += (point2-point1)**2
    return sum**(1/2)

def kNN(test_data, train_set):
    kNN_list = sorted(train_set, key=lambda train_data: euclidian_distance(train_data, test_data))
    value_counter = {0:0, 1:0}
    for data in kNN_list[:K]:
        value_counter[data.value]+=1
    return max(value_counter, key=value_counter.get)

def get_data(self):
    return self.id, *self.coords, self.value