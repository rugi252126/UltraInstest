# Code compatibility
from __future__ import absolute_import
from __future__ import print_function

# import the necessary packages
import openpyxl


class Excel:
    def __init__(self):
        self.__xls = None
        self.__active_sheet = None

    def load_file(self):
        self.__xls = openpyxl.load_workbook('../../Resources/Project_Information.xlsx', data_only=True)

    def read_sheet(self, sheet_name):
        # make sure file is already loaded
        if self.__xls is not None:
            # read specific sheet from excel file
            self.__active_sheet = self.__xls[sheet_name]

    def get_cell_value(self, col_name="A"):
        # make sure there is active sheet
        if self.__active_sheet is not None:
            # take individual value from cells
            a = []
            # excluding the first row(header)
            for row in range(2, self.__active_sheet.max_row + 1):
                # specify the column coverage
                for column in col_name:
                    cell_name = "{}{}".format(column, row)
                    if self.__active_sheet[cell_name].value is not None:
                        a.append(self.__active_sheet[cell_name].value)

            return a
