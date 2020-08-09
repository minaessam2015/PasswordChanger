import os
import random
import string
import email_users
from User import User,get_users,save_users


def generate_passwords(file: str):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = [str(i) for i in range(10)]
    
    assert os.path.exists(file), "Provided file for users does not exist"
    users = get_users(file)

    for u in users:
        # numbers 5 digits
        d = random.sample(digits,4)
        # uppder 2 characters
        up = random.sample(upper,2)
        # lower 2 characters
        lo = random.sample(lower,2)
        pass_combined = [d,up,lo]
        shuffled_index = random.sample([0,1,2],3) 
        new_pass = pass_combined[shuffled_index[0]]+pass_combined[shuffled_index[1]]\
            +pass_combined[shuffled_index[2]]
        new_pass_str = ''
        for chr in new_pass:
            new_pass_str += chr
        print(new_pass_str)
        old_pass = u.new_pass
        u.old_pass = old_pass
        u.new_pass = new_pass_str

    save_users(file,users)

if __name__ =='__main__':
    import sys
    assert len(sys.argv) == 2, "Expected to have a path for the users file"
    file = sys.argv[1]
    generate_passwords(file)