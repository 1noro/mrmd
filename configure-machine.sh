#!/bin/bash
# run as ROOT

apt update
apt upgrade -y
apt install -y gnupg git python3-gnupg 

timedatectl set-timezone Europe/Madrid
