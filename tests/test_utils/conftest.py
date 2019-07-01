import pytest
from urllib.request import urlretrieve
import tarfile

data_url = 'http://sagarverma.github.io/others/motor_data.tar'
urlretrieve(data_url, "/tmp/motor_data.tar")

tar = tarfile.open("/tmp/motor_data.tar")
tar.extractall(path="/tmp/")
tar.close()
