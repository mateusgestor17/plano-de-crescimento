# Gera arquivos únicos de prévia (tudo embutido) em previa/
import base64, os, re
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def b64(path, mime):
    return 'data:%s;base64,%s' % (mime, base64.b64encode(open(path, 'rb').read()).decode())
def lib(name): return '<script>' + open(os.path.join(R, 'assets/js', name)).read().replace('</script', '<\\/script') + '</script>'
os.makedirs(os.path.join(R, 'previa'), exist_ok=True)
libs = lib('gsap.min.js') + lib('ScrollTrigger.min.js') + lib('three.min.js')

# página principal
s = open(os.path.join(R, 'index.html')).read()
for f in sorted(os.listdir(os.path.join(R, 'assets/img/clientes'))):
    s = s.replace('assets/img/clientes/' + f, b64(os.path.join(R, 'assets/img/clientes', f), 'image/png' if f.endswith('.png') else 'image/jpeg'))
for f in sorted(os.listdir(os.path.join(R, 'assets/img/resultados'))):
    s = s.replace('assets/img/resultados/' + f, b64(os.path.join(R, 'assets/img/resultados', f), 'image/jpeg'))
s = s.replace('assets/logo-horizontal.png', b64(os.path.join(R, 'assets/logo-horizontal.png'), 'image/png'))
s = s.replace('assets/logo-icone.png', b64(os.path.join(R, 'assets/logo-icone.png'), 'image/png'))
s = s.replace('assets/logo-vortex.png', b64(os.path.join(R, 'assets/logo-vortex.png'), 'image/png'))
s = s.replace("THANK_YOU_URL: 'obrigado/'", "THANK_YOU_URL: 'vortex-obrigado-previa.html'")
s = s.replace('<script>\n(function () {\n  \'use strict\';', libs + '\n<script>\n(function () {\n  \'use strict\';', 1)
_s = re.sub(r'<!--.*?-->', '', s, flags=re.S); assert 'src="assets' not in _s and 'href="assets' not in _s, 'sobrou caminho'
open(os.path.join(R, 'previa/vortex-site-previa.html'), 'w').write(s)

# página de obrigado
s = open(os.path.join(R, 'obrigado/index.html')).read()
s = s.replace('../assets/logo-vortex.png', b64(os.path.join(R, 'assets/logo-vortex.png'), 'image/png'))
for n in ['three.min.js', 'gsap.min.js', 'ScrollTrigger.min.js']:
    s = s.replace('<script src="../assets/js/%s"></script>' % n, lib(n))
assert '../assets' not in s
open(os.path.join(R, 'previa/vortex-obrigado-previa.html'), 'w').write(s)
print('prévias geradas')
