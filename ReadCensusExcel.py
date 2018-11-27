#! python3
# ReadCensusExcel.py - Tabulates population and number of census tracks for each county.

import openpyxl
import pprint

# open the workbook and extract the desired sheet

wb = openpyxl.load_workbook(r'C:\Users\zackb_000\Documents\Programming Projects\PythonExercises\censuspopdata.xlsx')
sheet = wb[wb.sheetnames[0]]

# load a dictionary called countyData with the data
countyData = {}

for row in range(2, len(list(sheet.rows)) + 1):
    # Each row has data for once census tract.
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value
    # Make sure the state is in countyData
    countyData.setdefault(state, {})
    # Make sure the county is a key in the state dict
    countyData[state].setdefault(county, {})
    # Update the county population and tract count
    countyData[state][county].setdefault('pop', 0)
    countyData[state][county]['pop'] += pop
    countyData[state][county].setdefault('tracts', 0)
    countyData[state][county]['tracts'] += 1

# open a new text file and write the contents of countyData to it
#  -- use pprint.pformat() to produce a string that is formatted as valid Python code
resultFile = open(r'C:\Users\zackb_000\Documents\Programming Projects\PythonExercises\census2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
