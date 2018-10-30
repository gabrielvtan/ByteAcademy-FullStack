#! /usr/bin/env bash

# Environment Variables
BLOCKCHAIN_NAME =$(cat reference/black/blockchain_name.txt)

# Initialize parameters
multi-chain create $BLOCKCHAIN_NAME

# Create blockchain
multichaind $BLOCKCHAIN_NAME -daemon

echo $BLOCKCHAIN_NAME
