#!/usr/bin/python
import sys
from optparse import OptionParser
from lockfile import LockFile as lock
import subprocess as sp
import time

parser = OptionParser();
parser.add_option("-p", "--program", dest="program",
        help="program");
parser.add_option("-n", "--nodes", dest="nodes",
        help="number of nodes");   
        
(options, args) = parser.parse_args();

if not options.program or not options.nodes:
        print "Usage %s -p program -n number_of_nodes" % sys.argv[0]
        sys.exit(1)    

program = options.program
sp.call(['scp', program, "root@192.168.122.10:/root/nfs-shared/"])
program_name=program.split('/')[-1]
program_exec = program_name.split('.')[0]
time.sleep(3)
sp.call("ssh root@192.168.122.10 'mpicc /root/nfs-shared/"+program_name+" -o /root/nfs-shared/"+program_exec+"'",shell=True)

runCount = int(options.nodes)
pCount = 0
allRun = 0
someRun = 0
choice = [0]

stateFile = 'pstate.txt'


with lock(stateFile):
	fd = open(stateFile, 'r')
	state = fd.readline().split()
	pCount = len(state)
	if pCount == 0:
		print "Please check pstate.txt"
		sys.exit(1)
	state = [int(elem) for elem in state]
	choice = sorted(range(pCount), key=lambda k: state[k])
	allRun = runCount/pCount
	someRun = runCount%pCount
	fd.close()
	fd = open(stateFile, 'w')
	if allRun > 0:
		for pos in range(len(state)):
			if state[pos] == 0 and pos <> 0:
				sp.call(['virsh', 'resume', 'VM'+str(pos)])
				sp.call('ssh root@192.168.122.'+str(10+pos)+' mount -a', shell=True)
			state[pos] += allRun
		
	if someRun > 0:
		choice = choice[:someRun]
		for pos in choice:
			if state[pos] == 0 and pos <> 0:
				sp.call(['virsh', 'resume', 'VM'+str(pos)])
				sp.call('ssh root@192.168.122.'+str(10+pos)+' mount -a', shell=True)
			state[pos] += 1
	else:
		choice = []
	state = [str(elem) for elem in state]
	fd.write(" ".join(state)+"\n")
	fd.close()

# print "Debug: ", choice, allRun, pCount
fd = open('.mpi_hostfile', 'w')
for pos in choice:
	fd.write('192.168.122.'+str(10+pos)+'\n')
	# print "C:", '192.168.122.'+str(10+pos)+'\n'
for rep in range(allRun):
	for pos in range(pCount):
		fd.write('192.168.122.'+str(10+pos)+'\n')
		# print "A:", '192.168.122.'+str(10+pos)+'\n'
fd.close()

sp.call(['scp', '.mpi_hostfile', "root@192.168.122.10:/root/nfs-shared/"])
time.sleep(15)

output = sp.check_output("ssh root@192.168.122.10 'mpirun -np "+ str(runCount)+" --machinefile /root/nfs-shared/.mpi_hostfile /root/nfs-shared/"+program_exec+"'",shell=True)

with lock(stateFile):
	fd = open(stateFile, 'r')
	state = fd.readline().split()
	if allRun > 0:
		state = [str(int(elem)-allRun) for elem in state]
	for pos in choice:
		state[pos] = str(int(state[pos])-1)
	for pos in range(len(state)):
		if state[pos] == '0' and pos <> 0:
			sp.call(['virsh', 'suspend', 'VM'+str(pos)])
	fd.close()
	fd = open(stateFile, 'w')
	fd.write(" ".join(state)+"\n")
	fd.close()

print(output)
