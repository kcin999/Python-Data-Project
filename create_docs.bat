if exist docs del /f /q docs 
mkdir docs

sphinx-apidoc -F -f -t docsite_templates -o docs/ .

cd docs
.\make html