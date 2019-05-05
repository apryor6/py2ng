# Py2ng

Converts a Marshmallow Schema to TypeScript interface

## Usage

First, `pip install py2ng`

Then

`py2ng path/to/file/with/schema.py`

This will print out the converted interface. If you want the outputted keys to be
in lowerCamelCase, pass the `--camel-case` flag

`py2ng path/to/file/with/schema.py --camel-case`

### Example output

```bash
py2ng app/api/doodads/widget.py --camel-case
```

Where app/api/doodads/widget.py contains

```python
class WidgetSchema(ma.Schema):
    an_int = ma.fields.Integer()
    a_float = ma.fields.Float()
    a_str = ma.fields.String(256)
```

Results in

```typescript
export interface WidgetInterface {
    anInt: number,
    aFloat: number,
    aStr: string,
}
    
```
