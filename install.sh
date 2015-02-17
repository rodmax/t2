#!/bin/sh
set -x  # Print a trace of simple commands and their arguments
install_dir="$HOME/bin"
mkdir -p ${install_dir}
install ./toru ${install_dir}
install ./toen ${install_dir}
install ./t2.py ${install_dir}
set +x

echo "> toru hello"
toru hello
ret=$?

if [ "$ret" != "10" ]; then
    echo "Something gone wrong, check for pip dependency installed by: pip install -r requirements.txt"
else
    echo "t2 successfully installed. Check it with \"toru hello\""
fi

