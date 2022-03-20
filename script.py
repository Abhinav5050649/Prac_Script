from translate import Translator

translator = Translator(to_lang='fr')
try:
	with open('Intro.txt', mode='r') as my_file:
		text = my_file.read()
		translation = translator.translate(text)
		with open('./newfile.txt', mode='w') as my_file2:
			my_file2.write(translation)
except FileNotFoundError as e:
	print('check your file path silly!')
	raise e
