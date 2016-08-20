"""Support and convert several CAN (Controller Area Network) database formats .arxml .dbc .dbf .kcd ...

Canmatrix implements a "Python Can Matrix Object" which describes the can-communication 
and the needed objects (Boardunits, Frames, Signals, Values, ...) Canmatrix also includes
two Tools (canconvert and cancompare) for converting and comparing CAN databases. 
There are also some extract and merge options for dealing with can databases. 
        supported file formats for import:
        
            .dbc candb / Vector
        
            .dbf Busmaster (open source!)
        
            .kcd kayak (open source!)
        
            .arxml autosar system description
        
            .yaml dump of the python object
        
            .xls(x) excel xls-import, works with .xls-file generated by this lib
        
            .sym peak pcan can description
        
        supported file formats for export:
        
            .dbc
        
            .dbf
        
            .kcd
        
            .xls(x)
        
            .json Canard (open source!)
        
            .arxml (very basic implementation)
        
            .yaml (dump of the python object)
        
            .sym
"""

classifiers = """\
Development Status :: 4 - Beta
Environment :: Console
License :: OSI Approved :: BSD License
Topic :: Scientific/Engineering
"""

import sys
from setuptools import setup, find_packages
from canmatrix.version import version

doclines = __doc__.split("\n")

requirements = []
if sys.version_info < (3, 0):
    requirements.append("future")

setup(
    name = "canmatrix",
    version = version,
    maintainer = "Eduard Broecker",
    maintainer_email = "eduard at gmx dot de",
    url = "http://github.com/ebroecker/canmatrix",
    classifiers = filter(None, classifiers.split("\n")),
    description = doclines[0],
    keywords = "CAN dbc arxml kcd dbf sym",
    long_description = "\n".join(doclines[2:]),
    license = "BSD",
    platforms = ["any"],
    install_requires = requirements,
    extras_require = {
        "arxml": ["lxml"],
        "kcd": ["lxml"],
        "fibex": ["lxml"],
        "xls": ["xlrd", "xlwt"],
        "xlsx": ["xlsxwriter"],
        "yaml": ["pyaml"],
        "dbc": [],
        "dbf": [],
        "json": [],
        "sym": []
    },

    packages = find_packages(),
    entry_points={'console_scripts': ['cancompare = canmatrix.compare:main',
                                      'canconvert = canmatrix.convert:main']}
)

