# The following Makefile holds different useful rules for automating several
# tasks such us checking code quality, testing and code coverage

# Make sure a rule is executed even if no file changes are detected
.PHONY: install
install:
	: && \
	virtualenv -p python3.10 venv && \
	. venv/bin/activate && \
	pip install -r requirements/required.txt && \
	pip install -r requirements/dev.txt && \
	echo "../../../../src/" > venv/lib/python3.10/site-packages/lab.pth && \
	:
