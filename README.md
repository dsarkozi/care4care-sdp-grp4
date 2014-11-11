# Software Development Project
## Care4Care -- Group 4

### Setting up a virtual environment

You should set this up when you cloned the repository, because you need the file `requirements` which is located at the root. Or you can directly download it from here using the *Raw* link when visualizing the file in GitHub.

Make sure you have a fully-functional Python 3.4 interpreter up and running and write the following lines in a terminal in the folder where you want the new virtual environment to be, where `env` represents its name. Adapt this at your liking

1. `pyvenv-3.4 env` If this line works flawlessly, skip this
  1. Execute `pyvenv-3.4 --without-pip env`
  2. `source env/bin/activate`
  3. `curl https://bootstrap.pypa.io/get-pip.py | python`
  4. `deactivate`
2. `source env/bin/activate`
3. `pip install -r requirements` where `requirements` is the (path to the) requirements file at the root of the GitHub project
4. `deactivate`
5. You're good to go !

### Setup instructions for Eclipse PyDev

1. Open Eclipse (setup the workspace of your choice when prompted)
2. Go to *File > Import...*
3. Select *Git > Projects from Git* (you must have *EGit* installed for that I think)
4. Select *Clone URI*
5. Paste the URI of the GitHub project in the *URI* field : https://github.com/dsarkozi/care4care-sdp-grp4.git
This should fill the following two fields in.
6. Fill the *Authentication* field space with your GitHub credentials, then click *Next*
7. Click *Next* after assuring that the branch *master* is selected
8. Change the directory as you wish and click *Next*
9. Make sure to *Import existing projects* and click *Next*
10. Make sure that the *Care4Care* project is selected, then click *Finish*
11. You can setup the [virtual environment](#setting-up-a-virtual-environment) here before proceeding with the next steps
11. (optional) You should have a prompt saying that the Python interpreter is not configured. If not, skip this
  1. Proceed with *Manual Config* (if prompted)
  2. In the *Python Interpreters* section, click *New...*
  3. Click *Browse...* and go to the interpreter executable in your Python virtual environment (should be `env/bin/python` with `env` the name of your virtual environment folder), adapt the *Interpreter Name* at your liking and click *OK* to ok
  4. At this point, you should have a prompt requesting what you want to add in your system PYTHONPATH. Make sure that you have everything checked, namely three folders from your local Python 3.4 `lib` folder and one folder from the `lib` folder of your virtual environment, and click *OK* to ok twice
12. Right-click on the project and click *Properties*
13. In *PyDev - Django*, set the *Django manage.py* field to *manage.py* and the *Django settings module* field to *Care4Care.settings*
14. In *PyDev - Interpreter/Grammar*, set *Grammar Version* to `3.0` and *Interpreter* as the one from your virtual environment, then click *OK* to ok. If your virtual environment isn't in the dropdown, click on the link under the dropdown and follow the optional steps from 11., then try again
15. Open the PyDev Perspective to start working
16. You're good to go !

### Setup instructions for PyCharm

1. Open PyCharm
2. Click *Check out from Version Control* and click *GitHub*
3. Fill the form in with your GitHub credentials, then click *Login*
4. Select the GitHub project from the *Vcs Repository URL* dropdown, change *Parent Directory* and *Directory name* as you wish and click *Clone*
5. You should have a prompt asking if you want to open the directory specified. Click *No*
6. You can setup the [virtual environment](#setting-up-a-virtual-environment) here before proceeding with the next steps
6. Click *Open Directory*
7. Select *Care4Care* in the *care4care-sdp-grp4* folder
8. Go to *File > Settings...*
9. In *Project Interpreter* on the left, change the *Project Interpreter* dropdown on the right to the one from your virtual environment. If it's not in the dropdown, follow these steps
  1. In the dropdown, click *Show All*
  2. Click on the green + and then *Add Local*
  3. Set the path as `env/bin/python`, where `env` is the name of your virtual environment, then click *OK* to ok
  4. Select the newly added environment in the list, then click *OK* to ok
10. Click *OK* to ok
11. You're good to go !
