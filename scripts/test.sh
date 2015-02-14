reset
./scripts/uninstall.sh
./scripts/install.sh
python examples/simple/manage.py test nine --traceback -v 3
