Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> list1=['Cadbury','amul','nestle','vadilal','raymond','nike','spark','addidas','ITC','hyundai','maruti','kia']
>>> list2=['samsung','apple','redmi','amul','tesla','kwality','oppo','hyundai','delta','zara']
>>> #2 lists are created with brand names
>>> list(set(list1) & set(list2))
['hyundai', 'amul']
>>> #overlapping brand names in both lists
>>> for i in range(20,40):
	if i%2==0:
		print(i)

20
22
24
26
28
30
32
34
36
38
>>> #even numbers starting with 20 and ending with 40.
>>> #Assignment 1 | 12th May 2021
>>> #COMPLETED