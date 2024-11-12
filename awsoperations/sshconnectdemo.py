import paramiko as paramiko
import csv

from utilities.configurations import get_config

host = get_config()['Server']['host']
port = get_config()['Server']['port']
username = get_config()['Server']['username']
password = get_config()['Server']['password']

# Connect to ec2 instance using ssh using paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(
    paramiko.AutoAddPolicy())  # It will try to public and private key, to supress this check we can add this.
ssh.connect(host, port, username, password)

try:
    # Run command in the server
    stdin, stdout, stderr = ssh.exec_command("ls -a")
    print(stdout.readlines())

    # Check the content of the file created and extract the content of the file
    stdin, stdout, stderr = ssh.exec_command("cat demofile")
    lines = stdout.readlines()
    if lines:
        print(lines[1])

    # Upload files to server using SFTP within a try-finally to ensure closure
    sftp = ssh.open_sftp()
    try:
        destination_path = "script.py"
        local_path = "/Users/rishab/PycharmProjects/end-to-end-python-automation/batchfiles/script.py"
        sftp.put(local_path, destination_path)

        # Using function to upload csv file
        csv_ec2_path = "loandoc.csv"
        csv_local_path = "/Users/rishab/PycharmProjects/end-to-end-python-automation/batchfiles/loandoc.csv"
        sftp.put(csv_local_path, csv_ec2_path)

        # Trigger the batch command to execute script.py using python
        stdin, stdout, stderr = ssh.exec_command('python3 script.py')
        print(stdout.read().decode())

        # Download file
        sftp.get("loandoc.csv",
                 "/Users/rishab/PycharmProjects/end-to-end-python-automation/outputfiles/loanoutputdoc.csv")

        # Validating if the download csv has the correct data
        with open('/Users/rishab/PycharmProjects/end-to-end-python-automation/outputfiles/loanoutputdoc.csv',
                  'r') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                if row[0] == 3432:
                    assert row[1] == 'Approved'

    finally:
        sftp.close()
finally:
    # Closing the connection
    ssh.close()
