import movietrends.pirateripper as pirateripper 

def setup():
    pirateripper.getTrs()
    print("SETUP!")

def teardown():
    print("TEAR DOWN!")

def test_basic():
    print("I RAN!")
