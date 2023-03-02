#!/bin/bash

grn='\e[0;32m'
red='\e[0;31m'
wht='\e[0;37m'

set -eu -o pipefail

#test for root
sudo -n true
test $? -eq 0 || (exit 1 && echo -e "${red}please run with elevated priviliges (sudo)")

# test if OS is Raspbian:
if [[ $(grep -q "NAME=\"Raspbian GNU/Linux\"" /etc/os-release) -ne 0 ]]; then
	echo -e "${red}Hmmm, seems like you're not running this on a Raspberry pi, aborting just in case. modify install script to continue at your own risk."
	exit 1
fi
echo -e "${grn}Deteced Pi, starting full system upgrade....${wht}"
: '
sudo apt-get update -y && sudo DEBIAN_FRONTEND=noninteractive apt-get upgrade -y
# install necessary packages
while read -r p; do echo -e "${grn}APT is now installing $p....${wht}" && sudo apt-get install -y $p ; done < <(cat << "EOF"
	python3
	python3-pip
	sqlite3
	apache2
	libapache2-mod-wsgi-py3 
	python3-setuptools 
	python3-dev 
	build-essential
	libsm6
	libxext6
	libgl1-mesa-glx
	libgeos++
EOF
)
echo -e "${grn}Finished installing Linux packages, moving on to Python....${wht}"

# install necessary Python Packages
while read -r p; do echo -e "${grn}Now installing $p....${wht}" && sudo pip3 install $p ; done < <(cat << "EOF"
	django==4.0.1
	numpy
	pyserial
	django-mathfilters
	svg_to_gcode
	opencv-python
	pyyaml
	matplotlib
	shapely
	svgwrite
	scikit-image
EOF
) '
echo -e "${grn}Finished installing Python packages, moving on configuring autostart....${wht}"
sed -i '7s#.*#$dir = ${PWD}#' start.sh
sudo touch /etc/systemd/system/SmartBoardBot.service
echo "[Unit]
Description=Smart Board Bot service
After=multi-user.target
[Service]
Type=simple
Restart=always
ExecStart=${PWD}/start.sh
[Install]
WantedBy=multi-user.target" >> /etc/systemd/system/SmartBoardBot.service 
sudo systemctl daemon-reload
sudo systemctl enable SmartBoardBot.service 
sudo systemctl start SmartBoardBot.service
echo -e "${grn}Successfully created and started systemd Service!"
exit 0
