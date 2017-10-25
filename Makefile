# Makefile
NAME= whatsthere
EXECUTABLE= ./$(NAME)/$(NAME).py
BUGREPORT= $(EXECUTABLE).log
TESTFILES= ./tests/testfiles
LOG= ./tests/test.log

WRITE= echo "\n\n"
TOLOG= >> $(LOG)


all: clean init testfiles test

# Install requirements
init:
	pip3 install -r requirements.txt

# Create testfiles with different filenames, extensions and sizes
testfiles:
	./tests/extmaker.py $(TESTFILES)/ 5

# Test all default program functions
test:
	$(WRITE) "default testing\n" $(TOLOG)
	$(EXECUTABLE) $(TOLOG)

	$(WRITE) "wrong directory name test\n" $(TOLOG)
	$(EXECUTABLE) asdf $(TOLOG)
	$(EXECUTABLE) -1 $(TOLOG)

	$(WRITE) "wrong option name test\n" $(TOLOG)
	$(EXECUTABLE) ./. wrong_option 99 $(TOLOG)

	$(WRITE) "testfiles subdirectory testing\n" $(TOLOG)
	$(EXECUTABLE) $(TESTFILES) total 99 $(TOLOG)

	$(WRITE) "testfiles subdirectory / display only three most important\n" $(TOLOG)
	$(EXECUTABLE) $(TESTFILES) total 3 $(TOLOG)

	$(WRITE) "testfiles subdirectory / display only three most important\n" $(TOLOG)
	$(EXECUTABLE) $(TESTFILES) total 3 $(TOLOG)

	$(WRITE) "testfiles subdirectory / display entries\n" $(TOLOG)
	$(EXECUTABLE) $(TESTFILES) entries 99 $(TOLOG)

	$(WRITE) "testfiles subdirectory / display directories\n" $(TOLOG)
	$(EXECUTABLE) $(TESTFILES) dirs 99 $(TOLOG)

	$(WRITE) "testfiles subdirectory / display files\n" $(TOLOG)
	$(EXECUTABLE) $(TESTFILES) files 99 $(TOLOG)

	$(WRITE) "testfiles subdirectory / display extensions" $(TOLOG)
	$(EXECUTABLE) $(TESTFILES) sizes 99 $(TOLOG)

	$(WRITE) "testfiles subdirectory / display extensons with debug information" $(TOLOG)
	$(EXECUTABLE) $(TESTFILES) entries 99 -d $(TOLOG)

	$(WRITE) "Adding the program's log file to the test report" $(TOLOG)
	cat $(BUGREPORT) $(TOLOG)

	less $(LOG)

clean:
	rm -rf $(LOG)
	rm -rf $(BUGREPORT)
	rm -rf $(TESTFILES)

# Executed by default
.PHONY: clean init testfiles test
