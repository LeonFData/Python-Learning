# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.


name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

hr_counts = dict()
for line in handle:
    if line.startswith('From ') and ':' in line:
        hour = line.strip().split(':')[0].split()[-1]
        hr_counts[hour] = hr_counts.get(hour, 0) + 1


hr_list = []
for h, c in hr_counts.items():
    hr_list.append((h,c))

hr_list.sort()
    
for i, j in hr_list:
    print (i, j)
