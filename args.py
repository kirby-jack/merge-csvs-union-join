###################################################
# THIS HANDLES ALL THE ARGS THE USER MUST PASS IN # 
###################################################
import argparse
import os

# list allowed separators (note, if user types in '\t' this will come through as '\\t' )
availableSeparators = ["comma", "semicolon", "space", "tab", ",", ";", " ", "\t"]
separatorDict = {
    "comma": ',',
    ",": ",",
    "semicolon": ";",
    ";": ";",
    "space": " ",
    " ": " ",
    "tab": "\t",
    "\\t": "\t"
}


###################################################
#          DEFINE DYNAMIC HELP MESSAGES           # 
###################################################
def get_separator_help_message():
    helpMessage = "Specify your separator. Available separators include " + str(availableSeparators)[1:-1]
    return helpMessage


###################################################
#               CREATE ARGUMENTS                  # 
###################################################
# create arg instance
parser = argparse.ArgumentParser(
    description="This script merges csv files in your specified directory"
)

# add arguments to the instance
parser.add_argument('-d', '--directory', required=True, type=str, help="Enter the full directory path containing the csvs")
parser.add_argument('-o', '--output', required=True, type=str, help="Name your output file")
parser.add_argument('-s', '--separator', required=True, type=str, help=get_separator_help_message())

#  runs the parser and places the extracted data in a argparse.Namespace object:
args =   parser.parse_args()
directory=args.directory
output=args.output
separator=args.separator


###################################################
#           HANDLE -s SEPARATOR ARGUMENT          # 
###################################################
# exception for invalid -s input
if ((separator not in availableSeparators) and (separator != '\\t')):
    raise Exception("Please select from " + str(availableSeparators)[1:-1] + "\nIf you are using escaped or special characters, please enclose in quotation, e.g. '\\t', ';'")
    exit()

# convert -s argument to delimiter
separator = separatorDict[separator]


###################################################
#          HANDLE -d DIRECTORY ARGUMENT           # 
###################################################
# add "/" to end of directory
if (directory[-1:] != "/"):
    directory = directory + "/"

# check if path exists
if not (os.path.exists(directory)):
    raise Exception("Path does not exist, please ensure you specify full path")
    exit()


###################################################
#           HANDLE -o OUTPUT ARGUMENT             # 
###################################################
# ensure user entered no periods in the output argument
if("." in output):
    raise Exception("Please do not use a period '.' in your output name")
    exit()

# add .csv file type
output = output + ".csv"

# check file does not exist
if (os.path.exists(directory + output)):
    while True: 
        i = input("\nOutput file already exists, do you want to overwrite? Y or N: ")
        print("i is: " + i)
        if (i not in ["Y", "y", "N", "n", "Yes", "No"]):
            print("\nInvalid answer, please respond with Y or N")
        elif (i in ["N", "n", "No"]):
            print("\nPlease re-run script and select a different output name\n")
            exit()
        elif (i in "Y", "y", "Yes"):
            os.remove(directory + output)
            break
        else:
            break

