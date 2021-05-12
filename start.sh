#!/bin/sh

docker-compose -f traefik/traefik-configurations/docker-compose.yml up -d
docker-compose -f traefik/apps/jitsi/docker-compose.yml up -d
docker-compose -f traefik/apps/mailu/docker-compose.yml up -d
docker-compose -f traefik/apps/rocketchat/docker-compose.yml up -d
docker-compose -f traefik/apps/searx/docker-compose.yml up -d




