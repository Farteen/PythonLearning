"""递归打印list列表中的元素"""
def nested_print(the_list):
	"""首层循环"""
	for item in the_list:
		"""判断是否是一个list,如果是,那么递归调用"""
		if isinstance(item, list):
			nested_print(item)
		else:
			"""反之打印"""
			print(item)

movies = [1,2,[3,4,[5,6]]]
nested_print(movies)