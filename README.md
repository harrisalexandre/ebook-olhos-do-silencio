# Olhos do Silêncio

> **Algumas casas guardam memórias. Outras... guardam algo que nunca deveria ter despertado.**

**Olhos do Silêncio** é um romance de terror psicológico, suspense e mistério que conduz o leitor por uma investigação onde realidade, culpa e insanidade tornam-se praticamente indistinguíveis.

Nada acontece por acaso.

Cada capítulo revela uma nova peça de um quebra-cabeça perturbador.

Cada resposta gera perguntas ainda piores.

E, quando você acreditar ter entendido tudo...

...será tarde demais.

---

## 📖 Leia agora

A versão online pode ser acessada em:

**https://harrisalexandre.github.io/ebook-olhos-do-silencio/**

---

## Sobre o projeto

Este repositório contém uma experiência de leitura digital desenvolvida inteiramente em **HTML, CSS e JavaScript puro**, transformando arquivos Markdown em um eBook moderno, inspirado na experiência de leitura de dispositivos como Kindle e Apple Books.

Todo o conteúdo é carregado dinamicamente, preservando uma navegação fluida, limpa e focada exclusivamente na história.

---

# Recursos do leitor

* 🌙 Temas Claro, Escuro e Sépia
* 📖 Experiência de leitura semelhante ao Kindle
* 🔍 Busca em todos os capítulos
* 📑 Marcadores de leitura
* 💾 Salvamento automático do progresso
* 📱 Interface totalmente responsiva
* ⌨️ Navegação por teclado
* 📊 Barra de progresso da leitura
* ⏱️ Tempo estimado de leitura por capítulo
* ⚡ Carregamento otimizado dos capítulos

---

# Estrutura do projeto

```
ebook/
├── index.html
├── style.css
├── script.js
├── assets/
└── livro/
    ├── index.json
    ├── prologo.md
    ├── cap01.md
    ├── cap02.md
    └── ...
```

---

# Como executar

Como os capítulos são carregados utilizando `fetch()`, o projeto precisa ser servido por um servidor HTTP local.

## VS Code (recomendado)

1. Instale a extensão **Live Server**
2. Abra a pasta do projeto
3. Clique em **Open with Live Server**

---

## Python

```bash
python -m http.server 8000
```

Depois acesse:

```
http://localhost:8000
```

---

## Node.js

```bash
npx serve .
```

---

# Organizando os capítulos

Toda a estrutura do livro é controlada pelo arquivo:

```
livro/index.json
```

Exemplo:

```json
{
  "titulo": "Olhos do Silêncio",
  "autor": "Harris Alexandre",
  "descricao": "Romance de terror psicológico.",
  "capitulos": [
    {
      "arquivo":"prologo.md",
      "titulo":"Prólogo",
      "ato":"Prólogo"
    }
  ]
}
```

Para adicionar novos capítulos:

1. Crie um novo arquivo `.md`
2. Adicione-o ao `index.json`
3. Defina o título e o ato correspondente

A ordem dos capítulos segue exatamente a ordem definida no JSON.

---

# Markdown suportado

O leitor utiliza **marked.js** para converter Markdown em HTML.

São suportados:

* Títulos
* Subtítulos
* Negrito
* Itálico
* Citações
* Listas
* Separadores
* Imagens
* Links

---

# Personalização

É possível alterar facilmente:

* título do livro;
* autor;
* descrição;
* ordem dos capítulos;
* cores da interface;
* tipografia;
* temas.

Tudo sem necessidade de frameworks ou processo de build.

---

# Tecnologias

* HTML5
* CSS3
* JavaScript Vanilla
* Markdown
* marked.js

---

# Créditos

## Autor

**Harris Alexandre**

Engenheiro de Software

---

## História

**Olhos do Silêncio**

Escrito por **Harris Alexandre**

---

## Desenvolvimento

Leitor digital desenvolvido por **Harris Alexandre**

---

## Revisão

**Harris Alexandre**

---

## Licença

Este projeto foi desenvolvido para fins de leitura e distribuição da obra **Olhos do Silêncio**.

Todos os direitos da história, personagens, universo e conteúdo pertencem ao autor.

---

> *"Existem lugares onde o silêncio não representa paz... representa algo esperando para ser ouvido."*
