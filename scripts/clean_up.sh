find . -name "*.pyc" -exec rm -rf {} \;
rm MANIFEST.in~
rm .hgignore~
rm .gitignore~
rm -rf build/
rm -rf dist/
rm -rf examples/static/

mkdir examples/static/
