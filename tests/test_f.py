import movietrends.f as f
import os

testFile = '/tmp/sometestfile.test'
testContent = 'asdf'

def teardown():
    os.remove(testFile)

def test_basic():
    f.spit(testFile, testContent)
    assert(f.slurp(testFile) == testContent)
