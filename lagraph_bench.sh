#!/bin/bash

sudo -v
sudo ./fix_freq.sh
mkdir -p results
BIN="./build/main"

for file in data/*.mtx; do
    graph=$(basename "$file" .mtx)
    for algo in burkhard sandia; do
        echo "now: $graph $algo"
        OUT_FILE="results/lagr-${graph}-${algo}.csv"
        sync
        echo 3 | sudo tee /proc/sys/vm/drop_caches > /dev/null
        taskset -c 0-7 "$BIN" "$file" "$algo" "$OUT_FILE"
        echo "ready: $graph $algo"
    done
done
