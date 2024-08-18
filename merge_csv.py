import os
import csv
import sys

# maxInt allows for very large field values
# for handling OverflowError - credit goes to Stackoverflow user 'user1251007' for this technique https://stackoverflow.com/questions/15063936/csv-error-field-larger-than-field-limit-131072
maxInt = sys.maxsize


def get_fieldnames(directory, output, separator):
    
    fieldnames = []
    
    for file in os.listdir(directory):

        fullFilePath = directory + file

        if ((file[-4:] == ".csv") and (file != output)):
            
            with open(fullFilePath, 'r', newline='') as readCsvFile:
                readFieldnames = csv.DictReader(readCsvFile, delimiter=separator).fieldnames
                [fieldnames.append(fieldname) for fieldname in readFieldnames if fieldname not in fieldnames]
    
    return fieldnames


def merge_csv(directory, output, separator):
    
    # get fieldnames
    fieldnames=get_fieldnames(directory, output, separator)
    
    outputFullPath = directory + output
    
    while True:
        csv.field_size_limit(sys.maxsize)
        # decrease the maxInt value by factor 10 
        # as long as the OverflowError occurs.
        try:
            with open(outputFullPath, 'w') as writeCsvFile:
                csvwriter = csv.DictWriter(writeCsvFile, fieldnames=fieldnames)
                csvwriter.writeheader()
            
                # create a set to check if row is a duplicate
                writtenRows = set()
            
                # cycle through all directories
                for file in os.listdir(directory):

                    # only work on csvs and ignore the output file (if it exists)
                    if ((file[-4:] == ".csv") and (file != output)):
                        
                        print(f"\n'working on file {file}'\n")
                        file = directory + file
                        
                        # read csv
                        with open(file, newline='') as readCsvFile:
                            reader = csv.DictReader(readCsvFile, delimiter=separator)
                            
                            for rowReader in reader:
                            
                                # sort by fieldnames (this is for our set as we our hash lookup to have consistent orders, dictWriter does not need it sorted as it is a dictionary)
                                rowSet = tuple(rowReader.items()) # you cannot add dicts to sets, you need to add a tuple
                                rowSet= tuple(sorted(rowSet, key = lambda i: fieldnames.index(i[0])))
                                
                                if rowSet in writtenRows:
                                    print("\nSkipping duplicate row\n" + str(rowReader) + "\n")
                                else:
                                    writtenRows.add(rowSet)  # add to set
                                    csvwriter.writerow(rowReader) # write to buffer/file
                                    
            # returns file size
            return (round(os.path.getsize(outputFullPath)/1000000000, 2))

        except OverflowError:
            maxInt = int(maxInt/10)
                