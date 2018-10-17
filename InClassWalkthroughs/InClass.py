def float_to_int(float_list):
	int_list = []
	for f in float_list:
		int_list.append(int(f))
	return int_list
	
def string_sandbox(string_list):
	cap_list = []
	for s in string_list:
		cap_list.append(s[:1].upper() + s[1:])
	return " ".join(cap_list)

def int_to_str(int_list):
	return ' '.join([str(i) for i in int_list]) 


if __name__ == "__main__":
	 floats = [float(i) for i in range(100)]
	 #ints = float_to_int(floats)
	 #print(ints)
	 #strings = ['s' + str(f) for f in floats]
	 #print(strings)
	 #print(string_sandbox(strings))
	 print(int_to_str(floats))
	 # which =
	 # strings = []
	 # for f in floats:
	 # 	string.append('s' + str(f))
	# print(float_to_int(floats))
	# floats = []
	# for i in range(100):
	# 	floats.append(float(i))
	
	#print(floats)