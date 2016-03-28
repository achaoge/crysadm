#!/bin/bash
LOG=/var/log/crysadm.log
echo 'Stop crysadm on'  $(date) >> $LOG

sudo pkill redis-server
sudo pkill python3.4

