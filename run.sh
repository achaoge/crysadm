#!/bin/bash
LOG=/var/log/crysadm.log
echo 'Start crysadm on'  $(date) >> $LOG

sudo pkill redis-server
sudo pkill python3.4

BASE_DIR="$( cd "$( dirname "$0"  )" && pwd  )"                                                             
ls ${BASE_DIR}/ >> $LOG 2>&1
                                     
echo $PATH >> $LOG           
echo $LD_LIBRARY_PATH >> $LOG                                            
sudo /etc/init.d/redis-server restart
sudo redis-server >> $LOG 2>&1 &                                              
sudo python3.4 ${BASE_DIR}/crysadm/crysadm_helper.py >> $LOG 2>&1 &
sudo python3.4 ${BASE_DIR}/crysadm/crysadm.py >> $LOG 2>&1 & 
