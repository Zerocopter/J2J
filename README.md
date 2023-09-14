# J2J
Small utility to convert certain Java serialized objects into JSON

Usuage:

Show help:
 J2J.py --help

Deserialize Java object:
 J2J.py -i \<inputfile\> \[-o \<outputfile\>\]

Check if file is a serialized Java object, or search directory for Java objects:
 J2J.py -s \<FileOrDirectory\>



SBOM
--------------------------------------

javaobj
--------------------------------------
python-javaobj is a python library that provides functions for reading and writing (writing is WIP currently) 
Java objects serialized or will be deserialized by ObjectOutputStream. 
This form of object representation is a standard data interchange format in Java world.

The javaobj module exposes an API familiar to users of the standard library marshal, pickle and json modules.

https://pypi.org/project/javaobj-py3/
