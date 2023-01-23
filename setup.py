from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='0.1.0',
    description='Clean folder script',
    url='https://github.com/MarySavchuk3/Module_7.git',
    author='Savchuk Mariia',
    author_email='maria.savchuk2013@gmail.com',
    packages=find_namespace_packages(),
    entry_points={'console_scripts':['clean-folder=clean_folder.main:main_func']}
   )
