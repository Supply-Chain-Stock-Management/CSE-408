#!/bin/bash

docker run -d --name kong \
  --network=host \
  -e "KONG_DATABASE=off" \
  -e "KONG_PROXY_LISTEN=0.0.0.0:8000" \
  -e "KONG_ADMIN_LISTEN=0.0.0.0:8001" \
  kong:latest
