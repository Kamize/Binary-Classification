from itertools import chain

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from openpyxl import load_workbook

from knn import FOLDER_PATH, EXCEL_PATH, TRAINING_WS, TESTING_WS

FIG_FOLDER = FOLDER_PATH/'images'

def main():

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    # Loading excel file
    wb = load_workbook(EXCEL_PATH)
    train = wb[TRAINING_WS]
    test = wb[TESTING_WS]

    # Getting data
    train_rows = train.rows
    test_rows = test.rows
    next(train_rows)
    next(test_rows)

    # Initializing color table
    color_table = {0:'red', 1:'blue', '?':'yellow'}

    # Creating training data set from excel
    for id, x1, x2, x3, y in chain(train_rows, test_rows):
        ax.scatter(x1.value, x2.value, x3.value, c=color_table[y.value])

    # Closing excel file
    wb.close()

    # Setting label
    ax.set_xlabel('x1')
    ax.set_ylabel('x2')
    ax.set_zlabel('x3')
    ax.legend(handles=[mpatches.Patch( label=label, color=color) for label, color in color_table.items()])

    # Initializing viewpoints in azimuth and elevation
    viewpoints = {
        'default':(-60, 30),
        'x2x3':(0,0),
        'x1x3':(90,0),
        'x1x2':(90,90)
    }
    # Creates image folder if doesn't exist
    FIG_FOLDER.mkdir(exist_ok=True)

    # Saving image
    for fig_name, (azim, elev) in viewpoints.items():
        ax.view_init(azim=azim, elev=elev)
        plt.savefig(FIG_FOLDER/f"{fig_name}.png")

    # plt.show()

if __name__ == '__main__':
    main()