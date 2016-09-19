init:
	# Create symlink for pre-commit hook.
	ln -sf ../../tool/pre-commit.sh .git/hooks/pre-commit

	# Install dependencies.
	sudo pip3 install -r requirements.txt

	# Copy env config to local file.
	cp .dev.conf dev.conf

check:
	# Run tests.

run-server-dev:
	./tool/run.sh

run-neo4j-dev:
	# Run Neo4j docker container.
	docker run \
		--publish=7474:7474 --publish=7687:7687 \
		--volume=${HOME}/neo4j/data:/data \
		neo4j:3.0
