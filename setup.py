from distutils.core import setup
setup(
  name = 'multilabel',
  py_modules = ['multilabel'],
  version = '0.1',
  description = 'A Python module that will create multi-line xlabels in matplotlib with left-side titles',
  author = 'Ross Cohen',
  author_email = 'rjc55@njit.edu',
  url = 'https://github.com/BossColo/multilabel',
  download_url = 'https://github.com/BossColo/multilabel/tarball/0.1',
  keywords = ['Python', 'matplotlib', 'xlabels'],
  install_requires = ['bisect', 'matplotlib', 'datetime'],
  classifiers = [],
)