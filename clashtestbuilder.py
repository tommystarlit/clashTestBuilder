import sys
src = sys.argv[1]
# src = "/home/tommystarlit/Programowanie/GitRepo/clashTestBuilder/CNEB_cTests.xml"
dst = sys.argv[2]
dst = "/home/tommystarlit/Programowanie/GitRepo/clashTestBuilder/template.xml"

import xml.etree.ElementTree as ET
import copy

sroot = ET.parse(src).getroot()

ssets = []
for sset in sroot.findall('selectionsets/selectionset'):
    value = sset.get('name')
    ssets.append(value)

# print(ssets)

ctests = []
for sset in ssets:
    for cnt in range(ssets.index(sset),len(ssets)):
        ctest = [sset,ssets[cnt]]
        # print(ctest)
        # print(ctest[0], " vs ", ctest[1])
        ctests.append(ctest)

# print(ctests)
droot = ET.parse(dst).getroot()
# print((droot.findall('batchtest/clashtests/clashtest')[2].get('name')))
dlen = len(droot.findall('batchtest/clashtests/clashtest'))

while dlen < len(ctests):
    droot[0][0].append(copy.deepcopy(droot[0][0][0]))
#     file = ET.fromstring(s)
# b = file.find("b")
# for c in file.findall(".//c"):
#     dupe = copy.deepcopy(c) #copy <c> node
#     b.append(dupe) #insert the new node


# - scrap search set names
# - file name from parameter
# - create test sets
# - create tests
# - append to file
# - save and close
