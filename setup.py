from setuptools import setup
setup(
  name = 'convis',
  packages = ['convis','convis.filters'],
  version = '0.6.4',
  install_requires = ["matplotlib", "litus", "numpy", "future"],
  description = 'Convolutional Vision Model',
  author = 'Jacob Huth',
  author_email = 'jahuth@uos.de',
  url = 'https://github.com/jahuth/convis',
  download_url = 'https://github.com/jahuth/convis/tarball/0.6.4',
  keywords = ['vision model', 'retina model'],
  classifiers = [],
)
