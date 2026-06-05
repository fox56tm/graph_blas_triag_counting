#!/bin/bash

sudo -v
sudo ./scripts/fix_freq.sh
algo="sandia"
FLAME_DIR="flame_graphs"
mkdir -p "$FLAME_DIR"
for file in data/amazon-2008.mtx data/roadNet-CA.mtx data/web-NotreDame.mtx; do
    graph=$(basename "$file" .mtx)
    echo "now: $graph $algo"
    sync
    echo 3 | sudo tee /proc/sys/vm/drop_caches > /dev/null
    sudo perf record -g -F 99 --call-graph dwarf taskset -c 0-7 bash -c "cd src && uv run python3 main.py '$graph' '$algo'"
    sudo perf script -i perf.data | /home/dmitry-sergeev/utilits/FlameGraph/stackcollapse-perf.pl | /home/dmitry-sergeev/utilits/FlameGraph/flamegraph.pl > "${FLAME_DIR}/${graph}_flame_py.svg"
    echo "ready: $graph $algo"
done
