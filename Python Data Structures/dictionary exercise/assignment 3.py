# Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

email_list = dict()
for line in handle:
    if line.startswith('From '):
        email = line.split()[1]
        email_list[email] = email_list.get(email, 0) + 1

grt_word = None
grt_count = None
for k, v in email_list.items():
    if grt_word == None or grt_count < v:
        grt_word = k
        grt_count = v
print (grt_word, grt_count)
