import csv

# Reading the value from CSV
csv_path = '/Users/rishab/PycharmProjects/end-to-end-python-automation/utilities/loanapp.csv'
with open(csv_path, 'r') as read_file:
    reader = csv.reader(read_file, delimiter=',')
    name = []
    status = []
    for row in reader:
        name.append(row[0])
        status.append(row[1])
print(name)
print(status)
sam_index = name.index('sam')
sam_loan_status = status[sam_index]
print(f'Sam loan status is {sam_loan_status}')

# Writing the value to CSV
with open(csv_path, 'a') as write_file:
    writer = csv.writer(write_file)
    writer.writerow(["Daniel","rejected"])