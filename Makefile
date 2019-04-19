test:
	$(eval CONTAINER := $(shell docker run -d lgl-ubuntu sleep 1800))
	docker cp . $(CONTAINER):/home/user/lgl

prepare:
	docker build . -t lgl-ubuntu

shell: launch
	docker exec -it $(CONTAINER) /bin/bash

launch:
	$(eval CONTAINER := $(shell docker run -v $(PWD):/mnt -d lgl-ubuntu sleep 1800))
	docker cp . $(CONTAINER):/home/user/lgl
clean:
	rm -rf dist/* lgl.egg-info/
DIST:
	python3 setup.py bdist_wheel
upload-pypi:
	make clean
	make DIST
	twine upload --repository pypi dist/*
