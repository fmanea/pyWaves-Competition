#!/bin/bash
while true
do
  # loop infinitely
echo "'Running first process" >&2  
until python pyWavesWalletCheckSend.py; do
    echo "'pyWavesWalletCheckSend.py' crashed with exit code $?. Restarting..." >&2
    sleep 1
done
done
