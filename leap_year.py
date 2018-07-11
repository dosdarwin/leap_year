def is_leap():
	year = int(input('what year is it now:'))
	if  year % 4 == 0:
		print('It a leap year')
	else:
		print('It is not a leap year')
is_leap()