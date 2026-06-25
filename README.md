# Olhos do Silêncio — Leitor de eBook

Leitor digital estático feito em HTML, CSS e JavaScript puro. Transforma capítulos em Markdown em uma experiência de leitura imersiva, inspirada em Kindle e Apple Books.

---

## Como usar

O projeto faz requisições locais via `fetch()`, então **não funciona abrindo o `index.html` diretamente** no navegador (limitação de segurança dos navegadores modernos). Você precisa de um servidor local simples.

### Opção 1 — VS Code (recomendada)

1. Instale a extensão **Live Server** (ritwickdey.LiveServer)
2. Abra a pasta `ebook/` no VS Code
3. Clique com o botão direito em `index.html` → **Open with Live Server**
4. O navegador abrirá automaticamente em `http://127.0.0.1:5500`

### Opção 2 — Python

```bash
cd ebook
python -m http.server 8000
```
Acesse `http://localhost:8000`

### Opção 3 — Node.js

```bash
cd ebook
npx serve .
```
Acesse o endereço que aparecer no terminal.

---

## Estrutura de arquivos

```
ebook/
├── index.html          # aplicação principal
├── style.css           # estilos e temas
├── script.js           # lógica do leitor
├── assets/             # imagens e fontes extras (opcional)
└── livro/
    ├── index.json      # metadados e ordem dos capítulos
    ├── prologo.md
    ├── cap01.md
    ├── cap02.md
    └── ...
```

---

## Adicionando ou editando capítulos

Abra `livro/index.json`. Ele controla tudo: título, autor, descrição e a ordem exata de leitura.

```json
{
  "titulo": "Olhos do Silêncio",
  "autor": "Autor",
  "descricao": "Uma frase de apresentação do livro.",
  "capitulos": [
    { "arquivo": "prologo.md", "titulo": "Prólogo", "ato": "Prólogo" },
    { "arquivo": "cap01.md",   "titulo": "Capítulo 1 — A Demolição", "ato": "Ato I" }
  ]
}
```

Para **adicionar um capítulo**, crie o arquivo `.md` na pasta `livro/` e adicione uma entrada no array `capitulos`. O campo `ato` agrupa capítulos no índice lateral — use o mesmo texto para capítulos do mesmo bloco.

Para **reordenar**, basta mudar a ordem das entradas no JSON.

---

## Recursos do leitor

| Recurso | Detalhe |
|---|---|
| **3 temas** | Escuro, Sépia, Claro |
| **Tipografia** | 4 tamanhos de fonte, 3 espaçamentos, 3 larguras de coluna |
| **Progresso** | Barra no topo + indicador de capítulo (ex: 7 de 34) |
| **Tempo de leitura** | Estimativa por capítulo (~220 palavras/min) |
| **Busca** | Pesquisa em texto completo em todos os capítulos |
| **Marcador** | Salva a posição atual com um clique |
| **Persistência** | Reabre exatamente no capítulo e posição onde parou |
| **Teclado** | Setas, Page Up/Down, Home, End, Esc |
| **Responsivo** | Desktop, tablet e celular |
| **Performance** | Carrega só o capítulo atual; pré-carrega o anterior e o próximo |

---

## Markdown suportado

O leitor interpreta em tempo real via [marked.js](https://marked.js.org/):

```
# Título principal
## Subtítulo de capítulo

Parágrafo normal com **negrito** e *itálico*.

> Citação em blockquote

---  (divisória)

- lista
- de itens

![imagem](caminho/imagem.jpg)
[link](https://exemplo.com)
```

---

## Personalização rápida

**Mudar o livro:** edite `livro/index.json` com o novo título, autor e lista de capítulos.

**Mudar cores de destaque:** no `style.css`, a variável `--accent` (padrão `#8b1a1a`, vermelho vinho) é usada em todos os elementos de realce. Troque por qualquer cor.

**Mudar a fonte:** substitua a importação do Google Fonts no `index.html` e atualize `--font-body` e `--font-display` no topo do `style.css`.

---

## Dependências externas

Apenas uma, carregada via CDN:

- **marked.js** `^9` — converte Markdown para HTML no navegador

Nenhum framework, nenhum build step, nenhuma instalação necessária.
