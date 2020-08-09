import os
from User import User,get_users
from passwords import generate_passwords


def generate_bash_file(input_file: str,output_file='./change_passwords.sh'):

    users = get_users(input_file)
    with open(output_file,'w+') as f:
        f.write('echo "Started"\n')
        for user in users:
            f.write(r'sudo echo -e "{0}\n{1}" | passwd "{2}"'.\
                format(user.new_pass,user.new_pass,user.user_name)+'\n')
        # make the file executable
        os.chmod(output_file, 0o777)



if __name__ == '__main__':
    import sys
    import sys
    assert len(sys.argv) >= 2, "Expected to have a path for the users file"
    file = sys.argv[1]
    if len(sys.argv) == 3:
        out_file = sys.argv[2]
    else:
        out_file = './change_passwords.sh'
    generate_passwords(file)
    generate_bash_file(file,out_file)
