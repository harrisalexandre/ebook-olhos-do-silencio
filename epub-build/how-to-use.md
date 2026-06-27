# Olhos do Silêncio — EPUB

## O que tem aqui

`olhos-do-silencio.epub` — arquivo final, pronto para distribuir ou enviar ao
Kindle. 2.1 MB, 42 seções (sinopse, dedicatória, epígrafe, prólogo, 30
capítulos, 4 interlúdios, epílogo), capa embutida, 4 fontes embutidas
(Cormorant Garamond regular/itálico + Cormorant SC regular/medium), sumário
navegável (toc.ncx + nav.xhtml), metadados completos (título, autor, idioma,
descrição, direitos).

## Por que EPUB serve para Kindle também

A Amazon descontinuou o conversor MOBI/KindleGen. Hoje o caminho oficial é:
1. Enviar o `.epub` direto via **Send to Kindle** (app, site ou e-mail) — a
   Amazon converte automaticamente para o formato interno (KFX) na nuvem.
2. Ou enviar pela área de "Conteúdo e dispositivos" da sua conta Amazon.

Não existe mais necessidade de gerar um `.mobi` ou `.azw3` manualmente — o
próprio EPUB bem formado é o que se envia.

## Importante: este EPUB corrige um problema de formatação que o site NÃO tem corrigido

Os capítulos originais (.md) usam quebra de linha simples entre frases, sem
linha em branco. Isso funciona no site porque o JS trata cada linha como
parágrafo, mas markdown padrão (usado pelo pandoc, e por qualquer conversor
EPUB) exige linha em branco para separar parágrafos — sem isso, o capítulo
inteiro vira um único bloco de texto colado.

**Esta correção foi aplicada SOMENTE no pipeline do EPUB** (no script
`epub-build/montar_markdown.py`, função `to_markdown_paragraphs`), não nos
arquivos `.md` originais usados pelo site. Ou seja: o EPUB está com a
formatação correta (cada frase no próprio parágrafo); o site continua
exibindo os capítulos como bloco único, do jeito que já estava.

Se decidir corrigir isso no site também no futuro, é só pedir.

## Como gerar o EPUB de novo (se editar os .md)

```bash
cd epub-build
python3 montar_markdown.py        # remonta md/livro-completo.md a partir
                                   # dos .md do livro, na ordem do index.json,
                                   # já corrigindo a formatação de parágrafos
pandoc metadata.yaml md/livro-completo.md \
  -o olhos-do-silencio.epub \
  --css=epub.css \
  --resource-path=.:images \
  --epub-cover-image=images/cover.jpg \
  --toc --toc-depth=2 \
  --split-level=2 \
  --epub-embed-font=fonts/CormorantGaramond-Variable.ttf \
  --epub-embed-font=fonts/CormorantGaramond-Italic-Variable.ttf \
  --epub-embed-font=fonts/CormorantSC-Regular.ttf \
  --epub-embed-font=fonts/CormorantSC-Medium.ttf
```

Arquivos usados no build:
- `montar_markdown.py` — monta o markdown mestre na ordem certa, limpa
  comentários HTML (das opções de dedicatória/epígrafe) e corrige parágrafos.
- `epub.css` — estilo do EPUB (capitular vermelha, Cormorant embutida,
  separadores). Pesos de fonte fixos (não-variáveis) para compatibilidade
  com firmwares Kindle mais antigos.
- `metadata.yaml` — título, autor, idioma, descrição, capa.
- `fonts/` — as 4 fontes TTF embutidas.
- `images/cover.jpg` — capa (a mesma do site).

## Testado e validado

- Estrutura EPUB: mimetype correto na 1ª posição, container.xml, content.opf
  válidos.
- 42 seções, cada uma em arquivo próprio, ordem idêntica ao index.json.
- Zero parágrafo colado (varredura automática em todos os 42 arquivos).
- Encoding UTF-8 correto em título, sumário e corpo (sem caracteres
  corrompidos).
- Renderização visual conferida via screenshot real (capa, prólogo, cap 12,
  cap 31, sumário).
