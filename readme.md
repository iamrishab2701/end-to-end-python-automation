- To run all the test cases
  behave
- To run specific feature
  behave feature file location
- To run with specific tag
  behave feature --tags='name of the tag'
- To run with log
  behave feature --no-capture
- To generate allure json 
  behave --no-capture -f allure_behave.formatter:AllureFormatter -o name of the folder
- To open allure report from the json
  allure server absolute location of the allure folder

  


- Connecting to an EC2 Instance on Mac using SSH through Terminal
  - This guide will walk you through the steps to connect to a Linux EC2 instance from a Mac using SSH.

- Prerequisites 
  - PEM Key File: Make sure you have the .pem key file associated with your EC2 instance (e.g., Jenkin_CI_Server.pem). 
  - Permissions: Ensure that your key file has the correct permissions. This prevents unauthorized access and avoids SSH errors.
  
  - Steps 
    - Step 1: 
      - Set Key File Permissions: To secure your key file, set the permissions so that only you can read it. Open a terminal on your Mac and run: chmod 400 /path/to/your-key-file.pem
      - Replace /path/to/your-key-file.pem with the path to your .pem file, for example:
      - chmod 400 /Users/rishab/Downloads/Jenkin_CI_Server.pem
    - Step 2:
      - Go to your AWS Management Console and find the Public DNS of your instance (e.g., ec2-X-XXX-XXX-XXX.us-east-2.compute.amazonaws.com).
      - Example ssh -i /Users/rishab/Downloads/Jenkin_CI_Server.pem ec2-user@ec2-X-XXX-XXX-XXX.us-east-2.compute.amazonaws.com
      - Note: Replace ec2-user with ubuntu if the instance is running Ubuntu.
    - Step 3:
      - Accept the SSH Key (First Time Only)
      - Are you sure you want to continue connecting (yes/no/[fingerprint])?
      - Type yes and press Enter to continue. This will add the server to your known hosts.
    - Step 4:
      - Closing the SSH Session
      - To disconnect from the EC2 instance, use: exit

- Linux Commands
  - To switch root user use command sudo su -
  - To enable password authentication enable type command: vi /etc/ssh/sshd_config, type i to edit. Search Password Authentication and change it to yes and type esc and :wq to save, then reload the service using service sshd reload.
  - Then setup password for your ec2-user from root by command passwd ec2-user