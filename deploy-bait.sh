#!/bin/bash
# Re-creates the containerized honeypot with persistent logging
# This script ensures the bait is isolated but logs are shared with the host

sudo docker run -d --name venom-bait --restart always \
  -p 80:80 -p 21:21 -p 2222:2222 \
  -v ~/project-venom/opencanary.conf:/root/.opencanary.conf \
  -v /var/tmp:/var/tmp \
  thinkst/opencanary