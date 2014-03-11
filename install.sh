#!/bin.sh
install_dir="~/bin"
mkdir -p ${install_dir}
install ./toru ${install_dir}
install ./toen ${install_dir}
install ./t2.py ${install_dir}
echo "t2 successfully installed :)! Check it with \"toru hello\""
