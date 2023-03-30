#!/bin/bash
# send a request with curl and count the body size
curl -s $1 | wc -c
