0

import re
in_file = open('xbox.txt')
countFromEmail = 0
unique_emails = set() #using a set to maintain an unique list
for line in in_file:
    if re.findall('^From:.+@([^\.]*)\.', line):
        countFromEmail += 1
        line = line.replace("From:","") #replacing the string
        line = line.strip() # then trimming the white spaces
        unique_emails.add(line) #adding to the set
    # if re.findall('^To:.+@([^\.]*)\.', line):
    #     line = line.replace("To:","") #replacing the string
    #     line = line.strip() #then trimming the white spaces
    #     unique_emails.add(line) #adding to the set
for email in enumerate(unique_emails):
    print(email)
    