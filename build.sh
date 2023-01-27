echo "cleaning"
sh ./clean.sh
wait
python3 setup.py sdist bdist_wheel
wait
python3 -m twine upload dist/*
echo "done"
wait
echo "cleaning"
sh ./clean.sh
echo "Finished"