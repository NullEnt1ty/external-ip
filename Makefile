.PHONY: build clean

build: clean
	python3 setup.py sdist bdist_wheel

clean:
	rm -r build dist *.egg-info
