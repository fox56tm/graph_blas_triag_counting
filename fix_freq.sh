#!/bin/sh

sudo systemctl stop unattended-upgrades
sudo systemctl stop bluetooth

echo 1 | sudo tee /sys/devices/system/cpu/cpu*/cpuidle/state1/disable > /dev/null
echo 1 | sudo tee /sys/devices/system/cpu/cpu*/cpuidle/state2/disable > /dev/null
echo 1 | sudo tee /sys/devices/system/cpu/cpu*/cpuidle/state3/disable > /dev/null
echo 1 | sudo tee /sys/devices/system/cpu/cpu*/cpuidle/state4/disable > /dev/null
echo 1 | sudo tee /sys/devices/system/cpu/intel_pstate/no_turbo > /dev/null

for i in /proc/irq/*/smp_affinity; do
    echo f00 | sudo tee $i > /dev/null 2>&1
done
