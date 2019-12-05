#!/bin/bash
exec {lock_fd}>/root/lockfile || exit 1
flock -n "$lock_fd" || { echo "ERROR: flock() failed." >&2; exit 1; }
echo "Lock acquired..."
sleep 10
flock -u "$lock_fd"
