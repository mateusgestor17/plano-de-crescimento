# Como ligar o formulário do site à planilha (5 minutos)

Planilha: **Leads - Plano de Crescimento** (no seu Google Drive)

Cada pessoa que preencher o formulário vira uma linha nova nessa planilha,
nas colunas que você já tem (`Nome completo`, `Número do WhatsApp`, as 5 perguntas,
`campaign_name` etc.). A coluna `lead_status` entra como **novo** e `form_name`
como **Landing Page Vortex (site)**, para você diferenciar dos leads que vêm do formulário da Meta.

## Passo 1: criar o script
1. Abra a planilha.
2. Clique em **Extensões → Apps Script**.
3. Apague o que estiver escrito e cole todo o conteúdo do arquivo `google-apps-script.gs`.
4. Clique no ícone de salvar 💾.

## Passo 2: publicar
1. Clique em **Implantar → Nova implantação**.
2. Na engrenagem ⚙️ ao lado de "Selecione o tipo", escolha **App da Web**.
3. Preencha:
   - **Executar como:** Eu (seu e-mail)
   - **Quem pode acessar:** Qualquer pessoa
4. Clique em **Implantar** e depois em **Autorizar acesso**. Escolha sua conta Google.
   Se aparecer "O Google não verificou este app", clique em **Avançado → Acessar (não seguro)**.
   Isso é normal: o script é seu e só grava na sua planilha.
5. Copie a **URL do app da Web**. Ela termina em `/exec`.

## Passo 3: colar a URL no site
No arquivo `index.html` (página principal), procure por `SHEETS_URL` e cole a URL entre as aspas:

```js
SHEETS_URL: 'https://script.google.com/macros/s/AKfy.../exec',
```

Salve e publique o site de novo. Pronto!

## Testar
- Abra a URL `/exec` no navegador. Deve aparecer **ok**.
- Preencha o formulário do site. Em poucos segundos a linha aparece na planilha.

## Se você mudar o script depois
Use **Implantar → Gerenciar implantações → ✏️ Editar → Versão: Nova versão → Implantar**.
Assim a URL continua a mesma e você não precisa mexer no site.

## Rastreamento dos anúncios (UTMs)
Se o link dos anúncios tiver UTMs, elas vão para a planilha automaticamente:

| No link do anúncio | Vai para a coluna |
|---|---|
| `utm_source` | `platform` |
| `utm_campaign` | `campaign_name` |
| `utm_medium` | `adset_name` |
| `utm_content` | `ad_name` |

Sugestão para os anúncios da Meta (campo "Parâmetros de URL"):
```
utm_source=facebook&utm_medium={{adset.name}}&utm_campaign={{campaign.name}}&utm_content={{ad.name}}&campaign_id={{campaign.id}}&adset_id={{adset.id}}&ad_id={{ad.id}}
```
