#!/usr/bin/env bash

docker pull rocketchat/rocket.chat:latest
docker-compose stop rocketchat
docker-compose rm -f rocketchat
docker-compose up -d rocketchat
