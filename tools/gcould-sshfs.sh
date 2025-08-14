#!/usr/bin/env bash

# Mount Google Cloud VM filesystem via SSHFS using gcloud SSH configuration
# Usage: ./gcloud-sshfs.sh <instance-name> [gcloud-options...]
# Example: ./gcloud-sshfs.sh my-vm --zone=us-central1-a
# Press Ctrl+C to unmount and exit

set -euo pipefail

INSTANCE="$1"
MOUNT_DIR="$HOME/mnt/$INSTANCE"

# Trap to unmount on exit
cleanup() {
    if mountpoint -q "$MOUNT_DIR" 2>/dev/null; then
        echo "Unmounting $MOUNT_DIR..."
        fusermount -u "$MOUNT_DIR" 2>/dev/null || true
    fi
}
trap cleanup EXIT INT TERM

DRYRUN_OUTPUT="$(gcloud compute ssh "$INSTANCE" "${@:2}" --dry-run 2>/dev/null)"

echo
echo "dry run output: $DRYRUN_OUTPUT"
echo

USERHOST="$(echo "$DRYRUN_OUTPUT" | grep -o '[^[:space:]]*@[^[:space:]]*')"
SSH_CMD="$(echo "$DRYRUN_OUTPUT" | sed "s/ $USERHOST.*//" | sed 's/ -t / /g')"

mkdir -p "$MOUNT_DIR"
sshfs -o ssh_command="$SSH_CMD" "$USERHOST:/" "$MOUNT_DIR"

echo "Mounted $USERHOST:/ at $MOUNT_DIR"
echo
echo "Press Ctrl+C to unmount and exit"

# Keep script running
while true; do
    sleep 1
done
