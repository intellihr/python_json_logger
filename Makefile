test:
	flake8 --exclude 'setup.py,tests/snapshots/*' . && pytest .
