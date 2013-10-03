import json, os, sys

file_name = sys.argv[1]

with open("browsers.json", "r") as f:
    obj = json.loads(f.read())

num_of_tests = len(obj)

for counter in range(num_of_tests):
	os.system("python "+str(file_name)+ " " +str(counter)+" &")
