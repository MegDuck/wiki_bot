import wikipedia as wiki



def languages(readable=True, readable_out='stdout', readable_out_only_values=False):
	"""
	readable - display languages list in readable for humans format
	readable_out - (куда нужно отправлять вывод, переправляет в указанную функцию)
	e.g:
	def out_def(value):
		print(value)
	...

	readable_only_values - (вывод только значений(  русский, французский..)

	"""
	if readable == True:
		for i in wiki.languages():
			if readable_out_only_values == True:
				i = wiki.languages()[i]
			else:
				i = {i: wiki.languages()[i]}
			if readable_out == 'stdout':
				print(i)
			else:
				readable_out(i)
	else:
		return wiki.languages()




def search(page="", lang="en", results=1, def_input='stdin'):
	"""
	page - приблизительное имя страницы которую вы ищете.
	lang - язык на котором нужно найти страницу
	results - количество результатов
	def_input - функция для проброса через нее ввода интересующей страницы, e.g
	def get_input(values, results):
		counter = 1
		for i in values:
			print(counter, i)
			counter += 1
		value = input()
		return values[int(value)]


	"""
	wiki.set_lang(lang)

	if def_input == 'stdin':
		try:
			results = int(input("количество результатов: "))
		except ValueError:
			None
		current_page=input("page search: ")
		counter = 1
		# отображаем все результаты
		values = wiki.search(query=current_page, results=results)
		for i in values:
			print(f"{counter}: {i}")
			counter += 1
		value = input("choose number: ")
		try:
			page=values[int(value)-1]
		except ValueError:
			print('NAN given')
		except IndexError:
			print('choose number from given to you!')
	else:
		page=def_input(results=results)
	# инициализируем контент таблицы
	wiki_page=wiki.WikipediaPage(title=page)
	return '\n'.join(wiki_page.content.split('\n')[:5])

print(search(page="python"))














#print(languages(readable_out_only_values=False))
