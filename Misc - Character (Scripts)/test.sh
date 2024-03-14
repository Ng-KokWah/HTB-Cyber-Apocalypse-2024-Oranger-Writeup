#!/bin/bash

# IP address and port to connect to
IP="94.237.62.117"
PORT="49011"

# Connect using nc
nc "$IP" "$PORT" << EOF
$(seq 0 200)
EOF
