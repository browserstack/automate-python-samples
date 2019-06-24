import json
import sys
import subprocess

try:
	file_name = sys.argv[1]
	json_name = sys.argv[2]
except IndexError:
	print("Please provide test script and browserconfig as first and second argument, respectively, from command line.")
	sys.exit(1)

with open(json_name, "r") as f:
    obj = json.loads(f.read())

num_of_tests = len(obj)
process = []
for counter in range(num_of_tests):
	cmd = "python3 %s %s %s" % (file_name, json_name, counter)
	process.append(subprocess.Popen(cmd, shell=True))

for counter in range(num_of_tests):
	process[counter].wait()

