# Py2ng

Converts a Marshmallow Schema to TypeScript interface

## Usage

First, `pip install py2ng`

Then

`ng2py path/to/file/with/schema.py`

This will print out the converted interface. If you want the outputted keys to be
in lowerCamelCase, pass the `--camel-case` flag

`ng2py path/to/file/with/schema.py --camel-case`