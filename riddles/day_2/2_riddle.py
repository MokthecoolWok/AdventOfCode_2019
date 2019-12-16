import csv

data = []


# read through every row in file
def csvReader():
    file_data = open('input_data', 'r')
    csv_reader = csv.reader(file_data, delimiter=',')
    data.clear()

    for row in csv_reader:
        # loop through every number in row
        for number in row:
            # append to data-Array
            data.append(int(number))


# Part 1 of Day 2
def calculateGravityAssist():
    for index in range(0, len(data), 4):
        if data[index] == 1:
            # access value from index+1/2/3 as positional value, then call this position to store new value
            data[data[index + 3]] = data[data[index + 1]] + data[data[index + 2]]
        elif data[index] == 2:
            # access value from index+1/2/3 as positional value, then call this position to store new value
            data[data[index + 3]] = data[data[index + 1]] * data[data[index + 2]]
        elif data[index] == 99:
            break

    return data[0]


# Part 2 of Day 2
for noun in range(100):
    for verb in range(100):
        csvReader()
        # reset program back to default value
        data[1] = noun
        data[2] = verb

        if calculateGravityAssist() == 19690720:
            print("{}:{}".format(noun, verb))
            print(100 * noun + verb)

