/**
 * VORTEX — recebe os leads do site e grava na planilha
 * "Leads - Plano de Crescimento".
 *
 * Cada lead vira uma linha nova. As colunas são preenchidas pelo
 * NOME DO CABEÇALHO (linha 1), então a ordem das colunas pode mudar
 * sem quebrar nada. Cabeçalhos que o site não conhece ficam em branco.
 *
 * Como instalar: veja automacao/LEIA-ME.md
 */

var SHEET_NAME = 'Página1'; // nome da aba que recebe os leads

function doPost(e) {
  var lock = LockService.getScriptLock();
  lock.waitLock(20000);
  try {
    var d = JSON.parse((e && e.postData && e.postData.contents) || '{}');

    // proteção básica contra robôs e envios vazios
    if (d.website) return json_({ ok: true });
    if (!d.nome || !d.whatsapp) return json_({ ok: false, erro: 'nome e whatsapp obrigatórios' });

    // o script fica dentro da própria planilha (Extensões → Apps Script)
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var sheet = ss.getSheetByName(SHEET_NAME) || ss.getSheets()[0]; // se a aba mudar de nome, usa a primeira
    var headers = sheet.getRange(1, 1, 1, sheet.getLastColumn()).getValues()[0];

    var temAnuncio = !!(d.utm_source || d.fbclid || d.gclid || d.utm_campaign);
    var valores = {
      // colunas no padrão do formulário de leads da Meta
      'id': 'site-' + new Date().getTime(),
      'created_time': Utilities.formatDate(new Date(), 'America/Sao_Paulo', "yyyy-MM-dd'T'HH:mm:ssXXX"),
      'ad_id': d.ad_id,
      'ad_name': d.utm_content,
      'adset_id': d.adset_id,
      'adset_name': d.utm_medium,
      'campaign_id': d.campaign_id || d.utm_id,
      'campaign_name': d.utm_campaign,
      'form_id': 'site',
      'form_name': 'Landing Page Vortex (site)',
      'is_organic': temAnuncio ? 'false' : 'true',
      'platform': d.utm_source || 'site',
      // perguntas do formulário
      'Qual dessas situações mais representa o momento da sua empresa hoje?': d.desafio,
      'Qual é aproximadamente o faturamento mensal da sua empresa?': d.faturamento,
      'Se começassem a entrar mais oportunidades nos próximos meses, sua empresa conseguiria atender?': d.capacidade,
      'Quando você gostaria de começar a trabalhar o crescimento da empresa?': d.momento,
      'Em qual segmento sua empresa atua?': d.segmento,
      'Nome completo': d.nome,
      'Número do WhatsApp': d.whatsapp,
      'Email': d.email,
      'Nome da empresa': d.empresa,
      'lead_status': 'novo',
      // colunas extras (só são preenchidas se você criar esses cabeçalhos)
      'utm_source': d.utm_source, 'utm_medium': d.utm_medium, 'utm_campaign': d.utm_campaign,
      'utm_content': d.utm_content, 'utm_term': d.utm_term, 'fbclid': d.fbclid, 'gclid': d.gclid,
      'pagina': d.pagina
    };

    var linha = headers.map(function (h) {
      var v = valores[String(h).trim()];
      return limpa_(v);
    });
    sheet.appendRow(linha);

    return json_({ ok: true });
  } catch (err) {
    return json_({ ok: false, erro: String(err) });
  } finally {
    lock.releaseLock();
  }
}

// TESTE: selecione "testeLead" no topo do editor e clique em Executar.
// Uma linha de teste aparece na planilha (pode apagar depois).
function testeLead() {
  var r = doPost({ postData: { contents: JSON.stringify({
    nome: 'TESTE - pode apagar', whatsapp: '+5500000000000', empresa: 'Teste', segmento: 'Teste',
    desafio: 'Teste', faturamento: 'Teste', capacidade: 'Teste', momento: 'Teste'
  }) } });
  Logger.log(r.getContent());
}

// teste rápido: abra o link /exec no navegador e deve aparecer "ok"
function doGet() {
  return ContentService.createTextOutput('ok');
}

// evita fórmulas maliciosas e textos gigantes
function limpa_(v) {
  if (v === undefined || v === null) return '';
  v = String(v).slice(0, 500);
  if (/^[=+\-@]/.test(v)) v = "'" + v;
  return v;
}

function json_(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj)).setMimeType(ContentService.MimeType.JSON);
}
