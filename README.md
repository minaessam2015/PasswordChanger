# PasswordChanger
A python package to generate random passwords for each user and mail them about it. It can generate these numbers periodically.
## Updates
In this version a fields called keep in the users file. When set to false this users password doesn't get changed during password generation and enails aren't sent to him/her.
## Usage
Up to this point the feature of periodically creating passwords is not implemented
1. Download the files
2. To generate new passwords you nee to have your users listed in a CSV file with the following fields "Name,UserName,Mail,Password,OldPassword"
3. To generate new passwords for each user run "python generate_passwords.py path_to_users_file path_to_run_script_to_be_created (optional)"
4. run "sudo path_to_run_script_created_ before (default is change_passwords.sh)"
5. to email users about their new passwords run "python email_users.py path_to_users_file"
6. If you have a "users" file already with the new passwords you can skip all the steps and start from step 4

## generator_config.py
contains the configuration for the program like the mail to use to send the new passwords from and many other configurations
