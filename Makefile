init:
	# Create symlink for pre-commit hook.
	ln -sf ../../tool/pre-commit.sh .git/hooks/pre-commit

	# Install dependencies.
	sudo pip3 install -r requirements.txt

check:
	# Run tests.

run-server:
	# Run server.
	sudo python3 run.py

run-neo4j:
	# Run Neo4j docker container.
	docker run \
		--publish=7474:7474 --publish=7687:7687 \
		--volume=${HOME}/neo4j/data:/data \
		neo4j:3.0
