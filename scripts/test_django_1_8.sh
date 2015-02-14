reset
./scripts/uninstall.sh
./scripts/install_django_1_8.sh
python examples/simple/manage.py test nine --traceback -v 3 --settings=simple.settings_django_1_8
