test:
	flake8  --exclude setup.py . && pytest .
