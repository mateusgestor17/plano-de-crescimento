# Gera arquivos únicos de prévia (tudo embutido) em previa/
# Uso: python3 tools/gerar-previa.py
import base64, os, re
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OBRIGADO = 'plano-de-crescimento-obrigado'

def b64(path):
    mime = 'image/png' if path.endswith('.png') else 'image/jpeg'
    return 'data:%s;base64,%s' % (mime, base64.b64encode(open(path, 'rb').read()).decode())

def lib(name):
    return '<script>' + open(os.path.join(R, 'assets/js', name)).read().replace('</script', '<\\/script') + '</script>'

def embutir_imagens(s, prefixo):
    for pasta in ['assets/img/clientes', 'assets/img/resultados', 'assets']:
        for f in sorted(os.listdir(os.path.join(R, pasta))):
            if f.endswith(('.png', '.jpg')):
                s = s.replace(prefixo + pasta + '/' + f, b64(os.path.join(R, pasta, f)))
    return s

os.makedirs(os.path.join(R, 'previa'), exist_ok=True)

# página principal
s = open(os.path.join(R, 'index.html')).read()
s = embutir_imagens(s, '')
s = s.replace("THANK_YOU_URL: '%s/'" % OBRIGADO, "THANK_YOU_URL: 'vortex-obrigado-previa.html'")
s = s.replace("<script>\n(function () {\n  'use strict';", lib('gsap.min.js') + lib('ScrollTrigger.min.js') + "\n<script>\n(function () {\n  'use strict';", 1)
_s = re.sub(r'<!--.*?-->', '', s, flags=re.S)
assert 'src="assets' not in _s and 'href="assets' not in _s, 'sobrou caminho na página principal'
open(os.path.join(R, 'previa/vortex-site-previa.html'), 'w').write(s)

# página de obrigado
s = open(os.path.join(R, OBRIGADO, 'index.html')).read()
s = embutir_imagens(s, '../')
for n in ['gsap.min.js', 'ScrollTrigger.min.js']:
    s = s.replace('<script src="../assets/js/%s" defer></script>' % n, lib(n))
    s = s.replace('<script src="../assets/js/%s"></script>' % n, lib(n))
s = s.replace('<a href="../">', '<a href="vortex-site-previa.html">')
assert '../assets' not in s, 'sobrou caminho na página de obrigado'
open(os.path.join(R, 'previa/vortex-obrigado-previa.html'), 'w').write(s)
print('prévias geradas')
