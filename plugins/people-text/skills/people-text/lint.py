#!/usr/bin/env python3
"""Mechanical checks for people-text. Reports problems, never fixes them.

Usage: python3 lint.py [FILE]   (reads stdin when FILE is omitted)
Prints "line: rule: fragment" for each hit and exits with 1 if anything was found.

Dash and quote checks skip frontmatter, fenced code, inline code, URLs and ">" quotes.
"""
import re
import sys

# Escaped on purpose: the repository itself must stay free of these characters.
DASH = re.compile("[\u2014\u2013]| -- ")
QUOTES = re.compile("[\u00ab\u00bb\u201c\u201d\u201e\u2018\u2019\u2039\u203a]")
UTM = re.compile(r"utm_source=(openai|chatgpt\.com)", re.I)
EMOJI = re.compile("[\U0001F000-\U0001FAFF\u2600-\u27bf\u2b00-\u2bff\uFE0F]")

FENCE = re.compile(r"^(`{3,}|~{3,})")
INLINE_CODE = re.compile(r"(`+).+?\1")
URL = re.compile(r"\]\([^)]*\)|<https?://[^>]*>|https?://\S+")
HEADING_OR_ITEM = re.compile(r"^\s*(#{1,6}|[-*+]|\d+[.)])\s")
MARKUP = re.compile(r"^[\s>#*+\-\d.)]*")

CHATBOT_START = re.compile(
    r"^(конечно|безусловно|разумеется|отличный вопрос|ниже представлен)", re.I
)
CHATBOT_END = re.compile(
    r"(?:^|[.!?)]\s+)(?:"
    r"надеюсь,? (это|мой ответ|информация) (помогл|помож)"
    r"|(сообщите|дайте знать|напишите)( мне)?,? если"
    r"|если у вас (есть|остались|возникнут) (ещё |еще )?вопросы)",
    re.I,
)


def blank(match):
    return " " * len(match.group())


def prose_lines(lines):
    """Yield (number, line) outside frontmatter and fenced code blocks."""
    in_front = bool(lines) and lines[0].strip() == "---"
    fence = None
    for number, line in enumerate(lines, 1):
        stripped = line.strip()
        if in_front:
            if number > 1 and stripped == "---":
                in_front = False
            continue
        if fence:
            if stripped.startswith(fence):
                fence = None
            continue
        opening = FENCE.match(stripped)
        if opening:
            fence = opening.group(1)
            continue
        yield number, line


def fragment(line, start, end, width=25):
    left, right = max(0, start - width), min(len(line), end + width)
    text = line[left:right].strip()
    return ("..." if left else "") + text + ("..." if right < len(line) else "")


def lint(text):
    hits = []
    lines = list(prose_lines(text.splitlines()))
    for number, line in lines:
        no_code = INLINE_CODE.sub(blank, line)
        if not line.lstrip().startswith(">"):
            plain = URL.sub(blank, no_code)
            for rule, pattern in (("dash", DASH), ("quotes", QUOTES)):
                m = pattern.search(plain)
                if m:
                    hits.append((number, rule, fragment(line, m.start(), m.end())))
        for url in URL.finditer(no_code):
            if UTM.search(url.group()):
                hits.append((number, "utm", fragment(line, url.start(), url.end())))
        if HEADING_OR_ITEM.match(line):
            m = EMOJI.search(no_code)
            if m:
                hits.append((number, "emoji", fragment(line, m.start(), m.end())))

    text_lines = [(n, line) for n, line in lines if line.strip()]
    if text_lines:
        number, line = text_lines[0]
        if CHATBOT_START.match(MARKUP.sub("", line)):
            hits.append((number, "chatbot", fragment(line, 0, 0, 50)))
        number, line = text_lines[-1]
        m = CHATBOT_END.search(MARKUP.sub("", line))
        if m:
            hits.append((number, "chatbot", fragment(line, 0, 0, 50)))
    return sorted(hits)


def main(argv):
    if len(argv) > 2:
        sys.exit("usage: lint.py [FILE]")
    if len(argv) == 2:
        with open(argv[1], encoding="utf-8") as f:
            text = f.read()
    else:
        text = sys.stdin.read()
    hits = lint(text)
    for number, rule, frag in hits:
        print("{}: {}: {}".format(number, rule, frag))
    return 1 if hits else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
