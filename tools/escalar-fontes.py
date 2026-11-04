# Uso: python3 tools/escalar-fontes.py arquivo.html 1.1
# Multiplica todos os tamanhos de fonte (font-size e o atalho font:) do <style>.
import re, sys
p, F = sys.argv[1], float(sys.argv[2])
s = open(p).read()
a, b = s.index('<style>'), s.index('</style>')
css, n = s[a:b], 0
def r(m):
    global n; n += 1
    v = round(float(m.group(2)) * F * 2) / 2
    return m.group(1) + ('%g' % v) + 'px'
css = re.sub(r'(font-size:\s*)([\d.]+)px', r, css)
css = re.sub(r'(font:\s*(?:italic\s+)?\d{3}\s+)([\d.]+)px', r, css)
open(p, 'w').write(s[:a] + css + s[b:])
print(p, 'valores ajustados:', n)
