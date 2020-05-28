"""zang setup.py"""

from setuptools import find_packages, setup


setup(name="zang",
      author='Avaya Inc.',
      author_email='cpaassupport@avaya.com',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: MIT License',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Topic :: Utilities'],
      description=('This Python pacakge is an open source tool built to '
                   'simplify interaction with the Avaya CPaaS telephony platform.'),
      install_requires=['requests', 'python-dateutil'],
      extras_require={
          ":python_version<'3.4'": ['enum'],
      },
      keywords='zang api wrapper',
      license='MIT License',
      packages=find_packages(exclude=['tests', 'tests.*', 'docs']),
      url='http://docs.avayacloud.io',
      test_suite='tests',
      version="1.0.0")
