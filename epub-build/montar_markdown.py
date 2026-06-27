#!/usr/bin/env python3
"""Monta o markdown mestre do livro, na ordem do index.json, para conversão EPUB via pandoc."""
import json
import os
import re

LIVRO_DIR = "/home/claude/entrega/olhos-do-silencio-revisado/livro"
OUT_DIR = "/home/claude/epub-build/md"

# Arquivos de abertura/encerramento que NÃO devem entrar no corpo do livro
# (vão em metadados ou são páginas de navegação do site, não conteúdo de prosa)
SKIP = {"extras.md", "about-author.md"}

with open(os.path.join(LIVRO_DIR, "index.json"), encoding="utf-8") as f:
    index = json.load(f)

def clean(text):
    # Normaliza CRLF -> LF
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    # Remove comentários HTML usados como "opções comentadas" (dedicatoria/epigrafe)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    # Remove linhas em branco excessivas deixadas pelos comentários removidos
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    return text

def to_markdown_paragraphs(text):
    """O site original trata cada quebra de linha simples como um novo
    parágrafo (renderer customizado em JS). O markdown padrão (e o pandoc)
    exige uma linha em branco entre blocos para separar parágrafos --
    senão tudo se funde num único <p>. Esta função insere a linha em
    branco que falta, sem duplicar onde ela já existe."""
    lines = text.split("\n")
    out_lines = []
    for i, line in enumerate(lines):
        out_lines.append(line)
        is_last = i == len(lines) - 1
        next_is_blank = (not is_last) and lines[i + 1].strip() == ""
        cur_is_blank = line.strip() == ""
        if not is_last and not cur_is_blank and not next_is_blank:
            out_lines.append("")
    return "\n".join(out_lines)

chapters = []
for entry in index["capitulos"]:
    arquivo = entry["arquivo"]
    if arquivo in SKIP:
        continue
    path = os.path.join(LIVRO_DIR, arquivo)
    if not os.path.exists(path):
        print(f"AVISO: arquivo não encontrado: {arquivo}")
        continue
    with open(path, encoding="utf-8") as f:
        raw = f.read()
    body = clean(raw)
    body = to_markdown_paragraphs(body)
    chapters.append((entry, body))

print(f"Total de seções incluídas: {len(chapters)}")

os.makedirs(OUT_DIR, exist_ok=True)

# Escreve um markdown mestre único, com \newpage entre seções para forçar
# quebra de página no EPUB (pandoc respeita \newpage como page-break-before)
master_path = os.path.join(OUT_DIR, "livro-completo.md")
with open(master_path, "w", encoding="utf-8") as out:
    for i, (entry, body) in enumerate(chapters):
        if i > 0:
            out.write("\n\n\\newpage\n\n")
        out.write(body)
        out.write("\n")

print(f"Markdown mestre gerado em: {master_path}")
print(f"Tamanho: {os.path.getsize(master_path)} bytes")
