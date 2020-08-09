
class User(object):
    def __init__(self,name=None,user_name=None,mail=None,old_pass=None,new_pass=None):
        self.name = name
        self.user_name = user_name
        self.mail = mail
        self.old_pass = old_pass
        self.new_pass = new_pass
    def __repr__(self):
        return "Name: {0}, User Name: {1}\nNew Password: {2}\nOld Password: {3}".format(\
            self.name,self.user_name,self.new_pass,self.old_pass)
    
    def __str__(self):
        return self.__repr__()
    
def get_users(filename: str):
    """
    Return a ditc of the information from users file
    """
    users = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for i,a_contact in enumerate(contacts_file):
            if i == 0 or (a_contact.strip() == ''):
                # skip the first line
                continue
            #Name,UserName,Mail,Password,OldPassword
            fields = a_contact.split(',')
            user = User(name=fields[0],user_name=fields[1],mail=fields[2],\
                new_pass=fields[3],old_pass=fields[4])
            users.append(user)
            
    return users

def save_users(filename: str,users: list):
    """
    Save the users into a csv format
    """

    with open(filename,mode='w+') as f:
        f.write('Name,UserName,Mail,Password,OldPassword\n')
        for u in users:
            f.write(f'{u.name},{u.user_name},{u.mail},{u.new_pass},{u.old_pass}'+'\n')