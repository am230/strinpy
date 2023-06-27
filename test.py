
import strinpy

condition = True
output = strinpy.build([
    'text\n',
    condition and 'condition text\n',
    condition and ['condition text list\n'],
    condition and (lambda: 'supplier text\n'),
    [
        'text list\n',
        [
            'in text list\n'
        ]
    ]
])
print(output)