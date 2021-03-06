import csv



### for reading
with open('filpath/file.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')
    
    
    ### for write
    with open('file.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow(['John Smith', 'Accounting', 'November'])
    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])

              
###############################
              
              
for row in reader:
        content = list(row[i] for i in included_cols)
        col3Reformat = content[2].split(":")      #  a:b:c this will read col 3 value and split ,convert into list for each element  [a,b,c]
         for i in col3Reformat:
              print(i)                    # print a b c in each line
              
        
