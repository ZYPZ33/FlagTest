#!/bin/sh
executable_name="flagsGame"
install_directory="/usr/local/bin"
desktop_directory="/usr/share/applications/"
sed 's/flags\//\/usr\/share\/flags\//g' flags.py > flagsInstall.py
input="y"
test -e ${install_directory}/${executable_name}&& \
  read -p "Do you want to replace the already installed version [Y/n]" input

if [ "${input}" = "y" ] || [ "${input}" = "Y" ] || [ "${input}" = "" ]
then install flagsInstall.py ${install_directory}/${executable_name}&&\
  cp -r flags/ /usr/share/flags/&&\
  cp flags.desktop ${desktop_directory}
  echo "${executable_name} installed at ${install_directory}"
fi
