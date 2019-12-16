import csv

data = open('manhattan_data', 'r')


# read through every row in file
def csvReader():
    file_data = open('manhattan_data', 'r')
    csv_reader = csv.reader(file_data, delimiter=',')

    for row in csv_reader:
        # loop through every number in row
        for number in row:
            # append to data-Array
            data.append(number)


csvReader()
print(data)
