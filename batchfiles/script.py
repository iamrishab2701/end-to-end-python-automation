import csv


# Define the logic to determine status
def determine_status(account_number):
    if account_number % 2 == 0:
        return "Approved"
    else:
        return "Rejected"


with open("loandoc.csv", 'r') as csvFile:
    reader = csv.reader(csvFile)
    rows = [row for row in reader]

    # Add header for the status column if it's not already there
    if "Status" not in rows[0]:
        rows[0].append("Status")

    # Update each row with the calculated status
    for row in rows[1:]:  # Skip the header
        account_number = int(row[0])  # Convert the account number to an integer
        status = determine_status(account_number)
        if len(row) < 2:  # check if status column is empty
            row.append(status)
        else:
            row[1] = status

    # Write the updated data back to the same file
    with open('loandoc.csv', mode='w',
              newline='') as outFile:
        writer = csv.writer(outFile)
        writer.writerows(rows)
    print("Status column updated successfully in the original CSV file.")
