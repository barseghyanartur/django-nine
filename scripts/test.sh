reset
./scripts/uninstall.sh
./scripts/install.sh
#python examples/simple/manage.py test django_nine --traceback -v 3
python src/nine/tests/test_versions.py
