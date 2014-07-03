#!/bin/sh
set -x
install_dir="$HOME/bin"
mkdir -p ${install_dir}
install ./toru ${install_dir}
install ./toen ${install_dir}
install ./t2.py ${install_dir}
set +x
echo "t2 successfully installed :) ! Check it with \"toru hello\""
