# modified from orginial DEWPython setup.py by Eisenh
# Original at https://github.com/mmelwani/DEWPython
# specified utf-8 encoding, updated resource handling and
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='DEWPython_mod',
    version='2.0.0',
    author='Eisenh',
    author_email='andrew@eisenhawer.ca',
    description='Python-Implemented Deep Earth Water Model',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Eisenh/DEWPython_mod',
    packages=setuptools.find_packages(),
    download_url = 'https://github.com/Eisenh/DEWPython_mod/archive/refs/heads/master.zip',
    install_requires=[
        'numpy',
        'pandas',
        'matplotlib',
      ],
    #package_dir={'': 'DEWPython'},
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent"
    ],
    include_package_data=True
)
