#!/bin/bash
set -e
cmd=$1
commit=$2
if [ "$cmd" == "-b" ]; then
  echo "Building Project"
  python3 setup.py sdist bdist_wheel
  wait
  echo "Done"
elif [ "$cmd" == "-c" ]; then
  echo "Cleaning..."
  rm -rf ./build ./dist ./suplyd_odoo.egg-info
  wait
  echo "Done"
elif [ "$cmd" == "-g" ]; then
    echo "Preparing to Deploy.."
    git add .
    wait
    git commit -m "$commit"
    wait
    git push origin
    wait
    echo "Pushed to git"
elif [ "$cmd" == "-d" ]; then
    echo "Preparing to Deploy.."
    git add .
    wait
    git commit -m "$commit"
    wait
    git push origin
    wait
    echo "Pushed to git"
    echo "Now deploying to PIP."
    python3 -m twine upload dist/*
    wait
    echo "Done"
    echo "Cleaning..."
    rm -rf ./build ./dist ./suplyd_odoo.egg-info
    wait
    echo "Finished"
fi