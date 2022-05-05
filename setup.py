from setuptools import setup

readme = open('README.md').read()

setup(name='mw_mass_profile',
      version='0.0.0',
      long_description=readme,
      author='Marius Cautun',
      url='https://github.com/MariusCautun/Milky_Way_mass_profile',
      license='GNU GENERAL PUBLIC LICENSE',
      packages=setuptools.find_packages() + ['data'],
      package_dir={'data': 'data'},
      package_data={'data':  ['MW_enclosed_mass_profile.txt', 'MW_rotation_Eilers_2019.txt']},
      zip_safe=False)
