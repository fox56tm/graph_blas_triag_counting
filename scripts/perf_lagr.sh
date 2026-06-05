#!/bin/bash

sudo -v
sudo ./scripts/fix_freq.sh
BIN="./build/main"
algo="sandia"
FLAME_DIR="flame_graphs"
mkdir -p "$FLAME_DIR"
for file in data/amazon-2008.mtx data/roadNet-CA.mtx data/web-NotreDame.mtx; do
    graph=$(basename "$file" .mtx)
    echo "now: $graph $algo"
    sync
    echo 3 | sudo tee /proc/sys/vm/drop_caches > /dev/null
    sudo perf record -g -F 99 --call-graph dwarf taskset -c 0-7 "$BIN" "$file" "$algo" temp_c.csv
    sudo perf script -i perf.data | /home/dmitry-sergeev/utilits/FlameGraph/stackcollapse-perf.pl | /home/dmitry-sergeev/utilits/FlameGraph/flamegraph.pl > "${FLAME_DIR}/${graph}_flame_c.svg"
    rm -f temp_c.csv
    echo "ready: $graph $algo"
done
