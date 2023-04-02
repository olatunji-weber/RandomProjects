import openpyxl

workbook = openpyxl.load_workbook("ApocolypseFoodPrep.xlsx")
worksheet = workbook['Sheet1']

productPerStore = {}
columnLetter = 'A'

for row in worksheet.iter_rows(min_row=2, max_row=worksheet.max_row):
    if row[0].value in productPerStore:
        productPerStore[row[0].value] += 1
    else:
        productPerStore[row[0].value] = 1
print(productPerStore)
    # for cell in row:
    #     print(cell.value)

# for row in range(2, storesInfo.max_row + 1):
#     #Get the name of the Stores
#     # print(storesInfo[row])
#     for elem in storesInfo[row]:
#         print(elem.value)

# print(productPerStore.values())




