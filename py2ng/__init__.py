import inspect
from marshmallow import Schema, fields

TYPE_MAP = {
    fields.Bool: 'bool',
    fields.Boolean: 'bool',
    fields.Constant: 'any',
    fields.DateTime: 'Date',
    fields.Decimal: 'number',
    fields.Dict: 'object',
    fields.Email: 'string',
    fields.Field: 'any',
    fields.Float: 'number',
    fields.Function: 'any',
    fields.Int: 'number',
    fields.Integer: 'number',
    fields.List: 'any[]',
    fields.LocalDateTime: 'Date',
    fields.LocalDateTime: 'Date',
    fields.Mapping: 'any',
    fields.Method: 'any',
    fields.Nested: 'any',
    fields.Number: 'number',
    fields.Raw: 'any',
    fields.Str: 'string',
    fields.String: 'string',
    fields.TimeDelta: 'any',
    # fields.Tuple: 'any',
    fields.URL: 'string',
    fields.Url: 'string',
    fields.UUID: 'string',
}


def to_camel(snake):
    tkns = snake.split('_')
    return tkns[0] + ''.join(t.title() for t in tkns[1:])


def filter_schemas(module):
    schemas = [(name, obj) for (name, obj)
               in inspect.getmembers(module)
               if inspect.isclass(obj)
               and issubclass(obj, Schema)
               and obj is not Schema]  # ignore lines that import Marshmallow.Schema
    return schemas


def sch_to_intrf(name, schema, conv_camel=False):
    name = name.replace('Schema', '') + 'Interface'
    fields = []
    indent = ' ' * 4

    for k, v in schema._declared_fields.items():
        ts_type = TYPE_MAP.get(type(v), 'any')
        fields.append(
            f'{indent}{k if not conv_camel else to_camel(k)}: {ts_type},')
    fields = '\n'.join(fields)
    CONTENT = f'''export interface {name} {{
{fields}
}}
    '''
    print(CONTENT)
