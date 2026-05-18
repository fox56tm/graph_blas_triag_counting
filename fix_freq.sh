#!/bin/sh

sudo systemctl stop unattended-upgrades
sudo systemctl stop bluetooth

echo 1 | sudo tee /sys/devices/system/cpu/cpu*/cpuidle/state1/disable > /dev/null
echo 1 | sudo tee /sys/devices/system/cpu/cpu*/cpuidle/state2/disable > /dev/null
echo 1 | sudo tee /sys/devices/system/cpu/cpu*/cpuidle/state3/disable > /dev/null
echo 1 | sudo tee /sys/devices/system/cpu/cpu*/cpuidle/state4/disable > /dev/null
echo 1 | sudo tee /sys/devices/system/cpu/intel_pstate/no_turbo > /dev/null

sudo systemctl stop sysstat-collect.timer
sudo systemctl stop apt-daily-upgrade.timer
sudo systemctl stop fwupd-refresh.timer
sudo systemctl stop anacron.timer
sudo systemctl stop systemd-tmpfiles-clean.timer
sudo systemctl stop update-notifier-download.timer

echo 90 | sudo tee /sys/class/power_supply/BAT0/charge_control_end_threshold > /dev/null

for i in /proc/irq/*/smp_affinity; do
    echo f00 | sudo tee $i > /dev/null 2>&1
done
