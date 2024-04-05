#!/bin/bash
while true
do
  python ssh.py --host $1 --username $2 --password $3 --port $4
  sleep 10s
done