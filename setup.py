from setuptools import setup

def readme():
      with open('README.md') as f:
            return f.read()

setup(name='dumbpack',
      version='0.1',
      description='Returns a string with my name',
      long_description=readme(),
      url='https://github.com/mattmakesmaps/packaging_examples',
      author='Matt Kenny',
      author_email='matthewkenny@gmail.com',
      license='MIT',
      packages=['dumbpack'],
      zip_safe=False,
      # when installed, `say-script.py` is accessible from the cmd prompt
      scripts=['bin/say-script.py'],
      test_suite='nose.collector',
      tests_require=['nose']
      )
