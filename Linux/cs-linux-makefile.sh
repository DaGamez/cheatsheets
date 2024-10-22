#with a Makefile in directory

install:
	pip install -r requirements.txt
lint:
	pylint --disable =R,C hello
	
test:
	pytest test_hello.py
	

#desde el cmd
make install
make lint
	


