import sys
src = sys.argv[1]
# src = "/home/tommystarlit/Programowanie/GitRepo/clashTestBuilder/CNEB_cTests.xml"

import xml.etree.ElementTree as ET
root = ET.parse(src).getroot()

ssets = []
for sset in root.findall('selectionsets/selectionset'):
    value = sset.get('name')
    ssets.append(value)

print(ssets)
    # print(value)
# - provide search set file
# - copy ss file to as new_name
# - open ss file
# - scrap search set names
# - create test sets
# - create tests
# - append to file
# - save and close
