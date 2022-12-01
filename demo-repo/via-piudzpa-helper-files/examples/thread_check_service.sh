#!/bin/bash

expected_nproc=3
service_name="etech-worker.service"
sleep_time=30

while :
do
        nproc=$(/usr/bin/systemd-cgtop --raw -n2 | /bin/grep "$service_name" | /usr/bin/tail -1 | /usr/bin/awk '{ print $2 }' | /bin/sed -r 's/[-]+/0/g')
        echo "Running: $nproc , Expected: $expected_nproc , Service name: $service_name"

        if [[ $nproc -eq "" ]]
        then
                echo "Not running (string missing)"
        elif [[ $nproc -eq 0 ]]
        then
                echo "Not running (eq 0)"
        elif [[ $nproc -eq $expected_nproc ]]
        then
                echo "All OK"
        elif [[ $nproc -lt $expected_nproc ]]
        then
                echo "Less than expected. Executing restart"
                /usr/bin/sudo /bin/systemctl restart $service_name
                message="Running: $nproc Expected: $expected_nproc"
        elif [[ $nproc -gt $expected_nproc ]]
        then
                echo "More threads than expected"
        fi
        echo "Sleeping for $sleep_time seconds"
        sleep $sleep_time
done