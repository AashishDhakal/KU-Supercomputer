#!/bin/sh
echo $1
echo $2
useradd -p $(openssl passwd -1 $2 ) $1
mkdir -p /mnt/lustre/$1
chown $1:$1 /mnt/lustre/$1
scp /etc/passwd mds:/etc/
# SLURM resources limits
sacctmgr create user name=rajendra DefaultAccount=Physics Partition=normal,short --immediate
sacctmgr modify user rajendrap set GrpTRES=cpu=12 MaxJobs=2 --immediate


##scp /etc/shadow mds:/etc/
# Create a sync file for pushing user credentials to the nodes
##echo "MERGE:" > syncusers
##echo "/etc/passwd -> /etc/passwd" >> syncusers
##echo "/etc/group -> /etc/group" >> syncusers
##echo "/etc/shadow -> /etc/shadow" >> syncusers
# Use xCAT to distribute credentials to nodes
#xdcp cnode[1-5,7-9] -F syncusers
##xdcp compute -F syncusers
#rm syncusers