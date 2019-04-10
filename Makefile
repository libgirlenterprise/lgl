test:
	$(eval CONTAINER := $(shell docker run -d lgl-ubuntu sleep 1800))
	docker cp . $(CONTAINER):/home/user/lgl

prepare:
	docker build . -t lgl-ubuntu

shell:
	$(eval CONTAINER := $(shell docker run -d lgl-ubuntu sleep 1800))
	docker cp . $(CONTAINER):/home/user/lgl
	docker exec -it $(CONTAINER) /bin/bash
