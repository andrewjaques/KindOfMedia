import xml.etree.ElementTree as ET
tree = ET.parse('simpletestcases.xml') # TestCases file goes here
root = tree.getroot()

tests_to_keep = ("Test5", "Test1")

for test in root.findall('test'):
    testname = test.get("outputFileName")
    if testname in tests_to_keep:
        print(testname, "kept")
    else:
        print(testname, "did not match: stripping it out...")
        root.remove(test)

tree.write('output.xml')