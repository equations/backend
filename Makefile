init:
	# Create symlink for pre-commit hook.
	ln -sf ../../tool/pre-commit.sh .git/hooks/pre-commit

	# Install dependencies.
	pip3 install -r requirements.txt

check:
	# Run tests.
