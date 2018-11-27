import xml.etree.ElementTree as ET
import ntpath
import glob


# Find TestSequence files in the specified directory:
list_of_found_sequences = []
for filename in glob.glob('F:\\9.36 Config Cleanup\\TestSequences\\*.xml', recursive=True):  # Set the root of the sequences directory here
    list_of_found_sequences.append(filename)


# Find TestCases files in the specified directory:
list_of_found_test_cases = []
for filename in glob.glob('F:\\9.36 Config Cleanup\\9.36.x\\**\\*TestCases*.xml', recursive=True):  # Set the root of the config file 'Working' directory here
    if "requiredFilesOnly" not in filename:
        list_of_found_test_cases.append(filename)


# Build list of required configs:
list_of_required_configs = []  # Empty to start with
for sequence in list_of_found_sequences:
    tree = ET.parse(sequence)
    root = tree.getroot()
    for config in root.iter('config'):
        if "EncoderConfigFiles" in config.get("path"):
            list_of_required_configs.append(ntpath.basename(config.get("path")))
    print("Found", len(list_of_required_configs), "required configs so far.")

# Create simplified TestCases files:
removed_counter = 0
average_config_filesize = 3
for test_cases in list_of_found_test_cases:
    tree = ET.parse(test_cases)  # TestCases file goes here
    root = tree.getroot()
    for test in root.findall('test'):
        testname = test.get("outputFileName")
        if testname in list_of_required_configs:
            print(testname, "kept")
        else:
            print(testname, "did not match anything: stripping it out...")
            root.remove(test)
            removed_counter += 1
    tree.write("%s_requiredFilesOnly.xml" % test_cases[:-4])

total_diskspace_saved = ((removed_counter * average_config_filesize)/1024)
print(removed_counter, "unneccessary TestCase mutation instructions were removed. That's potentially saved", total_diskspace_saved, "GB of wasted disk space")
