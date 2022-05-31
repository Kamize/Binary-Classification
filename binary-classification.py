import pandas as pd
from pathlib import Path

#PATHS
FOLDER_PATH = Path(__file__).parent
EXCEL_PATH = FOLDER_PATH/"traintest.xlsx"   #TRAINING & TESTING FILES
OUTPUT_PATH = FOLDER_PATH/"hasil.xlsx"      #OUTPUT PROGRAM

def main():
    # Load Excel File
    xls = pd.ExcelFile(EXCEL_PATH)
    df1 = pd.read_excel(xls,'train')
    df2 = pd.read_excel(xls, 'test')

    #Creating data set instances
    training_list = [Train(id.value,x1.value,x2.value,x3.value,y.value) for row in df1]
    testing_list = [Train(id.value,x1.value,x2.value,x3.value,y.value) for row in df1]

    #Write an output file
    writer = pd.ExcelWriter(OUTPUT_PATH , engine='openpyxl')
    df1.to_excel(writer,sheet_name='trained')
    writer.save()
    writer.close()

class Train():
    '''Object representation of data set'''
    
    def __init__(self,id,x1,x2,x3,y):
        '''Initialize data set properties'''
        self.id = id
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.y = y
    
    '''pilih salah satu methods binary classification :
    1. Decision Tree (ID3)
    2. KNN
    3. Naive Bayes'''
    
    def get_data(self):
        '''Returns data for output file'''
        return self.id, self.x1, self.x2, self.x3, self.y
    



if __name__ == "__main__":
    main()