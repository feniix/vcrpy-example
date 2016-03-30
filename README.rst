******************************
A vcrpy example Python project
******************************

Simple example of use of vcr to mock web services

------
Setup:
------

    #> pip install -r dev-requirements.txt
    Requirement already up-to-date: requests in /usr/local/lib/python2.7/site-packages (from -r dev-requirements.txt (line 1))
    Requirement already up-to-date: vcrpy in /usr/local/lib/python2.7/site-packages (from -r dev-requirements.txt (line 2))
    Requirement already up-to-date: tox in /usr/local/lib/python2.7/site-packages (from -r dev-requirements.txt (line 3))
    Requirement already up-to-date: six>=1.5 in /usr/local/lib/python2.7/site-packages (from vcrpy->-r dev-requirements.txt (line 2))
    Requirement already up-to-date: contextlib2 in /usr/local/lib/python2.7/site-packages (from vcrpy->-r dev-requirements.txt (line 2))
    Requirement already up-to-date: wrapt in /usr/local/lib/python2.7/site-packages (from vcrpy->-r dev-requirements.txt (line 2))
    Requirement already up-to-date: PyYAML in /usr/local/lib/python2.7/site-packages (from vcrpy->-r dev-requirements.txt (line 2))
    Requirement already up-to-date: mock in /usr/local/lib/python2.7/site-packages (from vcrpy->-r dev-requirements.txt (line 2))
    Requirement already up-to-date: virtualenv>=1.11.2 in /usr/local/lib/python2.7/site-packages (from tox->-r dev-requirements.txt (line 3))
    Requirement already up-to-date: py>=1.4.17 in /usr/local/lib/python2.7/site-packages (from tox->-r dev-requirements.txt (line 3))
    Requirement already up-to-date: pluggy<0.4.0,>=0.3.0 in /usr/local/lib/python2.7/site-packages (from tox->-r dev-requirements.txt (line 3))
    Requirement already up-to-date: funcsigs in /usr/local/lib/python2.7/site-packages (from mock->vcrpy->-r dev-requirements.txt (line 2))
    Requirement already up-to-date: pbr>=0.11 in /usr/local/lib/python2.7/site-packages (from mock->vcrpy->-r dev-requirements.txt (line 2))

-----
Test:
-----

    #> tox
    GLOB sdist-make: /Users/otaeguis/projects/src/spantree/demos/vcr/vcrpy/setup.py
    py27 inst-nodeps: /Users/otaeguis/projects/src/spantree/demos/vcr/vcrpy/.tox/dist/vcrex-0.0.1.zip
    py27 installed: contextlib2==0.5.1,funcsigs==0.4,mock==1.3.0,pbr==1.8.1,py==1.4.31,pytest==2.9.1,PyYAML==3.11,requests==2.9.1,six==1.10.0,vcrex==0.0.1,vcrpy==1.7.4,wrapt==1.10.6
    py27 runtests: PYTHONHASHSEED='1094548104'
    py27 runtests: commands[0] | py.test -v --basetemp=/Users/otaeguis/projects/src/spantree/demos/vcr/vcrpy/.tox/py27/tmp
    ============================================================== test session starts ==============================================================
    platform darwin -- Python 2.7.11, pytest-2.9.1, py-1.4.31, pluggy-0.3.1 -- /Users/otaeguis/projects/src/spantree/demos/vcr/vcrpy/.tox/py27/bin/python2.7
    cachedir: ../.cache
    rootdir: /Users/otaeguis/projects/src/spantree/demos/vcr/vcrpy, inifile:
    collected 1 items
    
    test_simple.py::test_google PASSED
    
    =========================================================== 1 passed in 0.17 seconds ============================================================
    ____________________________________________________________________ summary ____________________________________________________________________
      py27: commands succeeded
        congratulations :)

