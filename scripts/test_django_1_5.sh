reset
./scripts/uninstall.sh
./scripts/install_django_1_5.sh
#python examples/simple/manage.py test nine --traceback -v 3 --settings=simple.settings_django_1_5
python src/nine/tests/test_versions.py