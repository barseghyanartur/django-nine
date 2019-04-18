reset
./scripts/uninstall.sh
./scripts/install_django_1_6.sh
#python examples/simple/manage.py test django_nine --traceback -v 3 --settings=simple.settings_django_1_6
python src/nine/tests/test_versions.py