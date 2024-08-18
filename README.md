# Merge CSVs - Union Join

## Description

This script will merge your CSVs into one file by performing a union operation, eliminating duplicate records.

An illustration of a union join can be found below: 

<img src="img/Union Join - Jack Kirby.png" width="300">

### Key Features

* **Duplicate Row Handeling**: This script efficiently handles duplicate rows by storing previously processed rows in a set. This allows for rapid duplicate checks (O(1) lookup time) before writing new rows. 
* **Handles Varying Column Orders**: This script can process CSV files with columns in different sequences, further ensuring accurate duplicate checks. 
* **Overwrite File Warning**: If your specified output file exists, the script will warn you and confirm if you wish to overwrite the file. 

## Getting Started
### Dependencies
* Python 3

### Executing script

**Step One - Clone Repo**

`git clone https://github.com/kirby-jack/merge-csvs-union-join.git`

`cd merge-csvs-union-join`

**Step Two - Launch Script**
```
python3 main.py -d '/PATH/TO/CSV/FILES' -o 'OUTPUT_NAME' -s 'SEPARATOR'
```

**Parameter Usage**

Replace `'/PATH/TO/CSV/FILES'` with the full path to the directory containing the CSV files you wish to merge. 

Replace `OUTPUT_NAME` with your desired output name. `OUTPUT_NAME` should not include a period `.`

Replace `SEPARATOR` with a valid separator value. Available `SEPARATOR` values include:
* comma
* ','
* semicolon
* ';'
* space
* ' '
* tab
* '\t'

**Step Three - Finished**

Your specified directory will now contain a merged csv called `OUTPUT_NAME.csv` (depending on your chosen `OUTPUT_NAME` name).

## Help
Run 
```
python3 main.py -h
```
If you encounter any issues, please contact me on LinkedIn - https://www.linkedin.com/in/kirby-jack/

## Authors
Jack Kirby - https://www.linkedin.com/in/kirby-jack/

## Credit
There is a piece of code for handeling very large field values, credit goes to Stackoverflow user 'user1251007' for this technique https://stackoverflow.com/questions/15063936/csv-error-field-larger-than-field-limit-131072 
