my_diction = {'1':'one','2':'two'}
def diction(**my_diction1):
	for key in my_diction1:
		print my_diction1[key]
	return
diction(**my_diction)
