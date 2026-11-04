# Site Vortex: página principal + página de obrigado

```
vortex-site/
├── index.html              ← página principal (domínio principal)
├── plano-de-crescimento-obrigado/index.html  ← página de obrigado (seudominio.com.br/plano-de-crescimento-obrigado/)
├── assets/
│   ├── logo-vortex.png, logo-icone.png
│   ├── img/resultados/     ← troque resultado-1.jpg ... resultado-8.jpg pelos prints reais
│   └── js/                 ← animações (GSAP + Three.js), carregadas depois da página
├── automacao/              ← script do Google Planilhas + passo a passo (LEIA-ME.md)
├── previa/                 ← arquivos únicos só para visualizar (não suba estes)
└── tools/gerar-previa.py   ← gera de novo as prévias depois de editar
```

## Antes de publicar
1. **Planilha:** siga `automacao/LEIA-ME.md` e cole a URL em `SHEETS_URL` no `index.html`.
2. **Resultados:** substitua as imagens em `assets/img/resultados/` (mesmo nome, formato retrato ~520×680).
3. **Depoimentos:** troque os textos entre [colchetes] na seção "O que nossos clientes dizem".
4. **Pixel/Tag (opcional):** cole o Meta Pixel / Google Tag no `<head>` dos dois arquivos.
   O formulário já dispara o evento `Lead` ao enviar.
5. Suba **tudo menos a pasta `previa/`** na hospedagem (Cloudflare Pages, Hostinger, Netlify...).
