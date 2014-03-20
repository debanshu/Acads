Virtual Cluster
===============

An automated virtual cluster creation machinery with support for running mpi-jobs. This was created as the term project for the course Cloud Computing.

Implemented using kvm.

####DEPENDENCIES:
The following are package dependencies as found in ubuntu/debian repositories.
- python
- virtinst
- qemu-kvm
- qemu-utils
- libvirt0
- libvirt-bin
- python-libvirt
- python-lockfile 
- libguestfs-tools

After the installation of the above dependencies, please run (possibly with root permissions):
update-guestfs-appliance



####File Details:
- cluster-admin.py: create and initialze the cluster
- cluster-runtime.py: give a C program to run on the cluster using the mpi framework.
- pstate.txt: store the current state of a node in the cluster. Used for dynamic balancing of load.



####TODO:
- Upload Master & Guest Images for the Cluster base hdd.
- Make code independent of specific ssh-keys for the mpi calls.


####Team Details:
- Khannan Sundar	
- Debanshu Sinha


