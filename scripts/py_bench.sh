#!/bin/bash
# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Dmitry Sergeev

sudo -v
sudo ./scripts/fix_freq.sh
mkdir -p results
for file in data/*.mtx; do
    graph=$(basename "$file" .mtx)
    for algo in burkhard sandia; do
        echo "now: $graph $algo"
        sync
        echo 3 | sudo tee /proc/sys/vm/drop_caches > /dev/null
        (cd src && LD_PRELOAD=/usr/local/lib/libgraphblas.so.9.4.5 \
            taskset -c 0-7 \
            uv run main.py "$graph" "$algo") > "results/bench-${graph}-${algo}.csv"
        echo "ready: $graph $algo"
    done
done
