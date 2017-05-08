import re

data = open('something.txt');
main_sum = 0

for line in data:
	line = line.rstrip()
	numbers = re.findall('[0-9]+',line)
	temp=0
	for num in numbers:
		temp = temp + int(num)
	main_sum+=temp

print(main_sum);