#!/usr/bin/python
import sys,os
from optparse import OptionParser
from virtinst.util import *
import subprocess as sp
import time


if sys.version_info < (2,5):
        import lxml.etree as ET
else:
        import xml.etree.ElementTree as ET
 
 
parser = OptionParser();
parser.add_option("-c", "--config", dest="config",
        help="config file");

 
(options, args) = parser.parse_args();
 
if not options.config:
        print "Usage %s -c config_file" % sys.argv[0]
        sys.exit(1)
        
settings = open(options.config,'r')
lines = settings.readlines()
settings.close()
n = int(lines[0])
nvm = 0
ip_base = '192.168.122.'
for line in lines[1:]:
	print('Creating VM '+str(nvm+1))
	vals = line.split()
	mem = int(vals[0])
	hdd = int(vals[1])
	ncp = 1
	if len(vals)>2:
		ncp = int(vals[2])
		
	
		
	if nvm==0:
		cpy_src = 'image-configs/Master-template.img'
		cpy_xml = 'image-configs/Master-template.xml'
	else:
		cpy_src = 'image-configs/Slave-template.img'
		cpy_xml = 'image-configs/Slave-template.xml'
	
	cpy_to = '/var/lib/libvirt/images/vm'+str(nvm)+'.img'
		
	if hdd< 512:
		print("Disk size should be equal to or greater than 512MB");
		sys.exit(1);
		
	print('Allocating space for VM '+str(nvm+1))
		
	if hdd>512:
		sp.call(['truncate','-r',cpy_src,cpy_to])
		sp.call(['truncate','-s','+'+str(hdd-512)+'M',cpy_to])
		sp.call(['virt-resize','--expand','/dev/sda1',cpy_src,cpy_to])
	else:
		sp.call(['cp',cpy_src,cpy_to])
		
	print('Setting parameters for VM '+str(nvm+1))
	sp.call(['cp',cpy_xml,'tmp.xml'])
	xml_set = ET.parse('tmp.xml')
	vm_name = 'VM'+str(nvm)
	name = xml_set.find('name')
	name.text = vm_name
	uuid = xml_set.find('uuid')
	uuid.text = uuidToString(randomUUID())	
	mac = xml_set.find('devices/interface/mac')
	mac.attrib['address'] = randomMAC(type='qemu')
	disk = xml_set.find('devices/disk/source')
	disk.attrib['file'] = cpy_to
	memory = xml_set.find('memory')
	memory.text = str(mem*1024)
	cmemory = xml_set.find('currentMemory')
	cmemory.text = str(mem*1024)
	vcpu = xml_set.find('vcpu')
	vcpu.text = str(ncp)
	
	xml_set.write('vm-xmls/'+vm_name+'.xml')
	
	sp.call(['losetup', '/dev/loop0', cpy_to])
	out = sp.check_output(['kpartx','-av','/dev/loop0'])
	mnt = out.split()[2]
	print("debug: mnt = "+mnt)
	vm_mnt = vm_name+'_mnt'
	sp.call(['mkdir', '-p',vm_mnt])
	sp.call(['mount','/dev/mapper/'+mnt,vm_mnt])
	
	sp.call("echo 'address "+ip_base+str(10+nvm)+"' >> "+vm_mnt+"/etc/network/interfaces ",shell=True)
	#print('debug: nvm '+str(nvm))
	#print("debug:")
	#print(sp.check_output("cat "+vm_mnt+"/etc/network/interfaces",shell=True))
	sp.call("echo "+vm_name+" > "+vm_mnt+"/etc/hostname ",shell=True)
	#print("debug:")
	#print(sp.check_output("cat "+vm_mnt+"/etc/hostname ",shell=True))
	time.sleep(5)
	sp.call(['umount',vm_mnt])
	
	sp.call(['kpartx','-d','/dev/loop0'])
	sp.call(['losetup','-d','/dev/loop0'])
	
	print('Defining VM '+str(nvm+1))
	sp.call(['virsh','define','vm-xmls/'+vm_name+'.xml'])
	
	sp.call(['rm','tmp.xml'])
	#sp.call(['rm','-rf',vm_mnt])
	
	
	print('')
	nvm = nvm+1

stateFile = open('pstate.txt','w')
zeros = '0 '*n
stateFile.write(zeros)
stateFile.close()


print("Starting & Suspending VM's ")
vm_name = 'VM'+str(0)
sp.call(['virsh','start',vm_name])
for x in range(n-1):
	vm_name = 'VM'+str(x+1)
	sp.call(['virsh','start',vm_name])
	time.sleep(7)
	sp.call("ssh root@"+ip_base+str(10+x+1)+" 'mount -a' ",shell=True)
	sp.call(['virsh','suspend',vm_name])
	
	
