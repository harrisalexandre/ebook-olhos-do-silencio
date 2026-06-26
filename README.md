# 👁️ Olhos do Silêncio

> *"Os monstros mais perigosos raramente vivem nas sombras."*

**Olhos do Silêncio** é um romance de terror psicológico, suspense e mistério que acompanha o jornalista **Caio Morel** durante a investigação de uma pequena estátua de pedra avermelhada envolvida por décadas de desaparecimentos, lendas e mortes inexplicáveis.

À medida que a investigação avança, o que parecia ser apenas mais um caso sobrenatural revela algo muito mais perturbador.

Talvez nunca tenha existido um monstro.

Talvez sempre tenha existido apenas um espelho.

---

## 📖 Leia online

A história pode ser lida gratuitamente em:

**https://harrisalexandre.github.io/ebook-olhos-do-silencio/**

---

# Uma experiência de leitura

Este projeto não é apenas um livro em HTML.

Foi desenvolvido para proporcionar uma experiência semelhante à de leitores digitais modernos, transformando capítulos escritos em Markdown em um eBook completo, elegante e responsivo, utilizando apenas **HTML, CSS e JavaScript puro**.

O objetivo é que o leitor esqueça que está diante de um navegador e simplesmente mergulhe na história.

---

# Recursos

* 📖 Interface inspirada em Kindle e Apple Books
* 🌙 Temas Claro, Escuro e Sépia
* 💾 Continuação automática da leitura
* 🔖 Marcadores de página
* 🔍 Busca em todos os capítulos
* 📊 Barra de progresso
* ⏱️ Tempo estimado de leitura
* 📱 Layout totalmente responsivo
* 🖼️ Imagens com ampliação em tela cheia
* ⌨️ Navegação por teclado
* ⚡ Carregamento otimizado dos capítulos

---

# Estrutura do projeto

```text
ebook/
├── index.html
├── style.css
├── script.js
├── assets/
└── livro/
    ├── index.json
    ├── prologo.md
    ├── cap01.md
    ├── ...
```

Todo o conteúdo do livro é escrito em **Markdown**, enquanto `index.json` organiza a estrutura da obra, os atos e a ordem dos capítulos.

---

# Executando localmente

Como os capítulos são carregados via `fetch()`, é necessário utilizar um servidor HTTP local.

### VS Code

Instale a extensão **Live Server** e abra o `index.html`.

### Python

```bash
python -m http.server 8000
```

### Node.js

```bash
npx serve .
```

---

# Organização da obra

A estrutura do livro é definida em:

```text
livro/index.json
```

Nele é possível alterar:

* título
* autor
* descrição
* capítulos
* atos
* ordem da leitura

Os capítulos são arquivos Markdown independentes, facilitando revisões e futuras expansões da história.

---

# Tecnologias

* HTML5
* CSS3
* JavaScript (Vanilla)
* Markdown
* marked.js

Sem frameworks.

Sem build.

Sem dependências complexas.

---

# Sobre o autor

**Harris Alexandre** é engenheiro de software e escritor independente.

Apaixonado por tecnologia, design e narrativas imersivas, desenvolveu tanto a obra quanto toda a experiência de leitura digital apresentada neste projeto.

**Olhos do Silêncio** marca sua estreia na ficção.

---

# Licença

O código deste projeto está disponível para fins de estudo e referência.

A história **Olhos do Silêncio**, seus personagens, universo, textos, mapas, ilustrações e demais conteúdos criativos são protegidos por direitos autorais e pertencem exclusivamente ao autor.

---

> *"Algumas histórias terminam quando a última página é virada. Outras continuam observando."*
