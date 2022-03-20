my_file = open('test.txt')

lines = my_file.readlines()

for i in lines:
	print(i)

my_file.seek(0)
print(my_file.readline())
print(my_file.readline())
print(my_file.readline())

my_file.close()
