def print_lol(the_list,level):
	"""第一个参数为位置参数，可以为任意python列表
	    第二个参数为遇到嵌套列表时候插入制表符名为"level"。"""
	for each_item in the_list:
		if isinstance(each_item,list):
			print_lol(each_item,level+1)
		else:
			for tab_stop in range(level):
				print("\t",end='')
			print(each_item)


movies=[
	"The Holy Grail",1975,"Terry Jones&Terry Gilliam",91,
		["Graham Chapman",
			["Michael Palin","John Cleese","Terry Gilliam","Eric Idle","Terry Jones"]]]

print(movies)

print_lol(movies,2)

