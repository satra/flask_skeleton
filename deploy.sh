#!/bin/sh

ansible-playbook ops/deploy.yml -i ops/hosts --private-key=$HOME/Downloads/main.pem
