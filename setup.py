try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = open('README.md').read()

setup(name='Milky_Way_mass_profile',
      version='0.0.0',
      long_description=readme,
      author='Marius Cautun',
      url='https://github.com/MariusCautun/Milky_Way_mass_profile',
      license='GNU GENERAL PUBLIC LICENSE',
      py_modules=['Cautun20_galpy_potential', 'Cautun20_contraction'],
      zip_safe=False)