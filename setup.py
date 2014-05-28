def get_readme():
    with open('README.md') as file:
        return file.read()

from distutils.core import setup
setup(
  name = 'posical',
  py_modules = ['posical'],
  version = '0.1.1',
  description = 'Calendar reform for Python',
  author = 'Z. D. Smith',
  author_email = 'zd@zdsmith.com',
  url = 'https://github.com/subsetpark/posical',
  download_url = 'https://github.com/subsetpark/posical/releases/tag/0.1',
  long_description = get_readme(),
  install_requires = 'nonzero',
  keywords = ['calendar', 'comte', 'date', 'humanism'],
  classifiers = [],
)
