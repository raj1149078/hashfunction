import random

IDlist = []
valuelist = []

IDlist = random.sample(range(1000, 2000), 500)
valuelist = random.sample(range(1, 1500), 500)

for i in range(len(IDlist)):
	print(IDlist[i], ",", end= "")

def display_hash(m):
	
	for i in range(len(m)): 
		print(i, end = " ")	
		for j in m[i]: 
			print("->", end = " ") 
			print(j, end = " ")	
		print() 
m = [[] for _ in range(47)] 


def hashf(key): 
	return key % len(m) 

def newAdd(m, key, value): 
	hash_key = hashf(key) 
	m[hash_key].append((key, value)) 

for i in range (len(IDlist)):
    newAdd(m, IDlist[i], valuelist[i])

display_hash (m)

arr = [IDlist[150], IDlist[162], IDlist[76], IDlist[425], IDlist[195], 
		IDlist[235], IDlist[62], IDlist[78], IDlist[80], IDlist[365],
		IDlist[40], IDlist[70], IDlist[11], IDlist[462], IDlist[350], 
		IDlist[362], IDlist[10], 2020, 2021, 945]

def search (key):
	index = hashf(key)
	count = 0
	for i in range(len(m[index])):
		count += 1
		if m[index][i][0] == key:
			print('Student ID- ', key , 'Found Value: ', m[index][i][1],"--- Computation Time:", count)
			return count

	print("Not found", "--- Computation Time:", count)
	return count

for i in range(20):
	count = search(arr[i])
