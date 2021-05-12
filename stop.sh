#!/bin/sh

docker-compose -f ~/traefik/traefik-configurations/docker-compose.yml down
docker-compose -f ~/traefik/apps/jitsi/docker-compose.yml down
docker-compose -f ~/traefik/apps/mailu/docker-compose.yml down
docker-compose -f ~/traefik/apps/rocketchat/docker-compose.yml down
docker-compose -f ~/traefik/apps/searx/docker-compose.yml down




