KeyNote:
```
I see the missing for someone and especially by me when deploy environment to run faust django example from faust
Please following the preparation environment to your system before you start using this repos
```
#### 1. install rocksdb by following guide
[https://python-rocksdb.readthedocs.io/en/latest/installation.html](https://python-rocksdb.readthedocs.io/en/latest/installation.html)
This requires librocksdb-dev>=5.0
```
apt-get install python-virtualenv python-dev librocksdb-dev
virtualenv venv
source venv/bin/activate
pip install python-rocksdb
```
if your librocksdb-dev is previous version please following
```
apt-get install build-essential libsnappy-dev zlib1g-dev libbz2-dev libgflags-dev
git clone https://github.com/facebook/rocksdb.git
cd rocksdb
mkdir build && cd build
cmake ..
make
make install-shared INSTALL_PATH=/usr
export CPLUS_INCLUDE_PATH=${CPLUS_INCLUDE_PATH}:`pwd`/../include
export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:`pwd`
export LIBRARY_PATH=${LIBRARY_PATH}:`pwd`
```
##### 2. Please ensure we have at least python3.6 for ready to use if not it's have to install manually by following this link
[https://websiteforstudents.com/installing-the-latest-python-3-7-on-ubuntu-16-04-18-04/](https://websiteforstudents.com/installing-the-latest-python-3-7-on-ubuntu-16-04-18-04/)
```
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.6 python3.6-dev python3.6-venv
```

Directory Layout
- ``proj/``

  This is the main Django project.

  We have also added a ``proj/__main__.py`` that executes if you do
  ``python -m proj``, and it will work as the manage.py for the project.

  This is also installed by setup.py as an entry point, so after
  ``python setup.py install`` or ``python setup.py develop`` the
  ``proj`` command will be available::

        $ python setup.py develop
        $ proj runserver

    The above is the same as running ``manage.py runserver``, but it will
    be installed in the system path.

- ``faustapp/``

    This is a Django App that defines the Faust app used by the project,
    and it also configures Faust using Django settings.

    This faustapp is also installed by setup.py as the ``proj-faust`` program,
    and can be used to start a Faust worker for your Django project by doing::

        $ python setup.py develop
        $ proj-faust worker -l info

- ``accounts/``

    This is an example Django App with stream processors.
