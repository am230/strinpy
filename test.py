import strinpy
condition = True
output = strinpy.build(['a', condition and 'b', condition and ['text'], condition and (lambda: 'supplier')])
print(output)
