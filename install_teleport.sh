#!/bin/sh
apt update
apt install -y curl
curl https://goteleport.com/static/install.sh | bash -s ${TELEPORT_VERSION}