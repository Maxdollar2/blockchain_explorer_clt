from setuptools import setup, find_packages


VERSION = '0.0.1'

setup(name='blockchain_explorer_clt',
      version=VERSION,
      description="a tiny blockchain explorer supporting different blockchains",
      long_description='just enjoy',
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='python blockchain exploerer Bitcoin terminal',
      author='mayotq',
      author_email='mayotq@gmail.com',
      url='https://github.com/mayotq/blockchain_explorer_clt',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
                        'requests',
                        ],
      entry_points={
      'console_scripts':[
                         'blockchain_explorer_clt = blockchain_explorer_clt.explore.argparse:main'
                         ]
      },
      )
