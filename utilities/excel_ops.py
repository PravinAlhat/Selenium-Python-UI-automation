import xlrd
from utility.variables import Variables as V

def read_excel_data(file_path, sheet_name):
    wb = xlrd.open_workbook(filename=file_path)
    sheet = wb.sheet_by_name(sheet_name=sheet_name)
    for rx in range(1, sheet.nrows):
        for col in range(1, sheet.ncols):
            print(sheet.cell_value(rx, col))
    return  sheet, wb

def read_specific_cell_value(sheet_data):
    for rx in range(sheet_data.nrows):
        print(sheet_data.row(rx))

def close_excel_file(workbook):
    workbook.close()

def read_car():
    sheet, wb = read_excel_data(file_path=V.test_data_excel_path, sheet_name='Cars')
    # read_specific_cell_value(sheet)
    # close_excel_file(wb) 

def exl_to_dict():
    wb = xlrd.open_workbook(V.test_data_excel_path)
    sheet = wb.sheet_by_name('Cars')
    dict_lst = []
    keys = sheet.row_values(0)
    values = [sheet.row_values(i) for i in range(1, sheet.nrows)]
    for value in values:
        dict_lst.append(dict(zip(keys, value)))
    return dict_lst
