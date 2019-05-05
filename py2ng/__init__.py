import inspect
from marshmallow import Schema, fields

TYPE_MAP = {
    fields.Integer: 'number',
    fields.Float: 'number',
    fields.String: 'string',
    fields.Boolean: 'bool',
}


def to_camel(snake):
    tkns = snake.split('_')
    return tkns[0] + ''.join(t.title() for t in tkns[1:])


def filter_schemas(module):
    schemas = [(name, obj) for (name, obj)
               in inspect.getmembers(module)
               if inspect.isclass(obj)
               and issubclass(obj, Schema)]
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
