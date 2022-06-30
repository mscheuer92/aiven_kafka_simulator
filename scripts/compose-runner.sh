#!/usr/bin/env bash
#######################################################################################################################
# Script Name    : compose-runner.sh
# Description    : run cycle of compose commands for a Python project
#######################################################################################################################
set -e
set -x

COMPOSE=$(command -v docker-compose)


# shellcheck disable=SC2086,SC2154
${COMPOSE} down -v --remove-orphans &&\
MY_UID="$(id -u)" MY_GID="$(id -g)" DOCKER_BUILDKIT=1 ${COMPOSE} ${1} build  &&\
MY_UID="$(id -u)" MY_GID="$(id -g)" ${COMPOSE} ${1} config &&\
if MY_UID="$(id -u)" MY_GID="$(id -g)" ${COMPOSE} ${1} up ${2}
then
    echo "** ${1} succeeded **"
else
    echo "** ${1} failed **"
    exit 1
fi
