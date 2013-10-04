import json, sys, subprocess

file_name = sys.argv[1]
json_name = sys.argv[2]

with open(json_name, "r") as f:
    obj = json.loads(f.read())

num_of_tests = len(obj)
process = []
for counter in range(num_of_tests):
	cmd = "python "+str(file_name)+ " " +str(json_name)+ " " +str(counter)
	process.append(subprocess.Popen(cmd, shell=True))

for counter in range(num_of_tests):
	process[counter].wait()

