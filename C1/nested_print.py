def nested_print(the_list):
	for item in the_list:
		if isinstance(item, list):
			nested_print(item)
		else:
			print(item)

