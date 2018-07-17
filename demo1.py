movies=[
	"The Holy Grail",1975,"Terry Jones&Terry Gilliam",91,
		["Graham Chapman",
			["Michael Palin","John Cleese","Terry Gilliam","Eric Idle","Terry Jones"]]]

print(movies)

#利用创建一个递归函数解决处理，来实现多层列表的for each 循环输出。
def print_lol(the_list):
	for each_item in the_list:
		if isinstance (each_item,list):
			print_lol(each_item)
		else:
			print(each_item)

print_lol(movies)
