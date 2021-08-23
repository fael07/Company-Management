from django import template

register = template.Library()

@register.filter(name='ano')
def _ano(valor):
    return str(valor)[:4]

@register.filter(name='grana')
def _grana(valor):
    value = str(valor)[:-3]
    size = len(value)
    new = []
    count = 0
    for c in range(size-1, -1, -1):
        count += 1
        if count % 3 == 0 and count != size:
            new.append(value[c])
            new.append('.')
        else:
            new.append(value[c])
    return ''.join(new)[::-1] + f',{str(valor)[-2:]}'