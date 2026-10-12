---
name: "people-text"
description: "Use when writing or editing any text that must read as human-written (posts, articles, channel content, work texts, resumes) so it does not look AI-generated. Also use for check-only requests (\"это похоже на нейросеть?\", \"проверь, не ИИ ли\", \"только проверь\", \"не правь\"): return a verdict with evidence and do not rewrite."
---

# people-text

Rules for writing text that reads as written by a person. Based on the Russian Wikipedia essay "Википедия:Признаки сгенерированности текста" (ВП:ПРГЕН). The signs are observations, not proof of generation, and detectors are unreliable. The goal is concrete, living text, not just evading checks.

Apply when drafting new text and when editing an existing draft. When editing, point out each violation found and fix it. Write in the language of the request (usually Russian). Punctuation: only "-" (hyphen), never the em dash `—`, en dash `–` or `--`; straight double quotes "", never guillemets `«»` or curly quotes `“”`.

## Check-only mode

Switch to it when the user asks to check rather than fix: "это похоже на нейросеть?", "проверь, не ИИ ли", "только проверь", "не правь". Do not rewrite anything. Run the linter on the text (see "Mechanical check"), then read it against sections 1-8 and answer in this shape:

```
Вердикт: сомнительный
- "играет ключевую роль в развитии отрасли" - инфляция значимости (1)
- "быстро, надёжно и удобно" - правило трёх (4)
Остатки чат-бота: "Надеюсь, это помогло!"
```

The verdict has three steps. "Чистый" means no tells or one weak tell. "Сомнительный" means a few tells that a person could also leave. "Похоже на сгенерированный" means several tells from different sections, or chatbot residue. Each piece of evidence is a quote of at most 15 words plus the pattern name and its section number. Chatbot residue (greetings, "надеюсь, помогло", knowledge-date disclaimers) goes on its own line, or is omitted when there is none. Keep it short: no retelling of the text and no advice unless the user asked for it. The signs are not proof, so do not claim certainty beyond the verdict.

## Pass levels

Edit in passes and stop at the first level that is enough.

1. Run the linter on the source text and note its hits.
2. Mark the tells from sections 1-8, then fix only the marked spots. Everything else stays word for word.
3. Restructure (reorder, merge or cut paragraphs) only when the user asked for a rewrite or the draft is your own.
4. Run the linter on the final text before handing it over. Fix every hit or say why it stays.

If the text has no noticeable tells, return it unchanged and say so in one line, for example "Текст чистый, править нечего." Edit only what you found. Never change facts, numbers, names, dates or quotations.

## When not to edit

Leave the text alone when the user asked only for a check, or when it has no noticeable tells. Do not touch quotations, code, ">" blockquotes, names, numbers and dates, even if they contain marker words. If a fix needs a fact you do not have (metrics in a resume, numbers in a personal story), ask the user instead of inventing it. If the user points to one paragraph, the rest of the text stays exactly as it was.

## 1. Concreteness over the average
- Models pick statistically average phrasing and drop rare details. Do the opposite: a specific fact, number, name, or date instead of "совершил революцию в промышленности".
- Do not inflate importance of ordinary things. Banned: "служит напоминанием", "играет ключевую/важную роль", "подчёркивает важность", "символизирует устойчивое влияние", "поворотный момент", "неизгладимый след", "непоколебимо преданный". Also the pattern "хотя это малоизвестно, это символизирует...".
- Do not look for symbolism or deep meaning where there is none.
- No promotional tone: "богатое культурное наследие", "захватывающая дух красота", "расположен в самом сердце", "может похвастаться", "продолжает очаровывать", "яркий", "разнообразный".

## 2. Shallow analysis and sources
- No tails "что подчёркивает/отражает/демонстрирует/выделяет/содействует...". An inanimate fact or event cannot "underline" anything; a person does.
- Do not prove significance by listing media ("освещался в нескольких национальных изданиях, включая..."). Do not quote policy language ("независимое освещение").
- Do not cite a source inline for trivial or undisputed facts.
- No vague authorities: "по словам экспертов", "отраслевые отчёты", "некоторые критики утверждают". Name the author or drop the claim.
- Do not generalize one source's view into a wide group's view.

## 3. Caveats, conclusions, structure
- No didactic caveats: "важно/критично/необходимо отметить", "стоит учесть/запомнить", "значения могут варьироваться".
- No "Заключение" section and no summary sentence closing every paragraph: "вкратце", "в заключение", "в целом", "подводя итог", "таким образом".
- No template "Несмотря на [плюсы], [тема] сталкивается с трудностями... перспективы светлые". If there is a problem, name it concretely, no consoling ending.
- In replies (a thread, a chat, an answer to an email) the answer or decision goes in the first sentence. Context and reasons come after it.
- Do not define the title as a term ("'Влияние X на Y' относится к..."). Start with substance.

## 4. Constructions and rhythm
- No "не только... но и..." and "это не просто X, это Y".
- No forced rule of three (three adjectives, three short phrases). Use as many items as really exist.
- Participial phrases must agree with the subject: "Используя этот метод, результаты улучшаются" is wrong. No chancery filler ("окружающая среда вокруг нас").
- Merisms "от X до Y" only when there is a real scale between the extremes.
- Do not swap a name or term for synonyms ("главный герой", "ключевой игрок", "упомянутый субъект"). Repeat the name.
- Avoid marker words and English calques: "погружаться", "гобелен", "переплетение", "нюанс", "способствовать", "являться", "представляет собой", "в рамках", "данный".
- Do not start paragraphs with "кроме того", "более того", "вдобавок". Vary sentence length: short next to long.
- Keep English terms the author uses (API, pull request, деплой, фича) as written. Do not translate or transliterate them for the sake of purity, and do not mix two spellings of one term.

## 5. Chancery and filler

Канцелярит makes text heavier without adding meaning. Prefer the verb, the subject and the plain word.

| Group | Было | Стало |
|---|---|---|
| Verbal noun instead of a verb | осуществлять проверку документов | проверять документы |
| Verbal noun with a light verb | оказать помощь в проведении анализа | помочь проанализировать |
| "в целях" | в целях снижения затрат | чтобы снизить затраты |
| "имеет место" | имеет место задержка поставок | поставки задерживаются |
| "на сегодняшний день", "в настоящее время" | на сегодняшний день сервисом пользуются 40 команд | сервисом пользуются 40 команд |
| "производить" | производится замена оборудования | оборудование меняют |
| "является" | ошибка является причиной сбоя | из-за ошибки сервис упал |
| Chain of genitives | повышение качества обслуживания клиентов компании | клиентов компании обслуживают лучше |

A chain of three or more genitives is a signal to rebuild the sentence around a verb. "В настоящее время" is usually just deleted: present tense already says "now".

## 6. Formatting
- Headings in sentence case, not Каждое Слово С Заглавной.
- No bold on key terms in the middle of sentences, no "key takeaways" bolding.
- No vertical lists of the form "1. **Заголовок**: пояснение" for connected prose. Use paragraphs; lists only where they are really needed.
- No emoji, especially in headings and lists.
- No em dash. Use comma, parentheses, colon, or a hyphen.
- No Markdown symbols (##, **, ---) if the platform does not render them.

## 7. Service traces and links
- Remove chatbot phrases: "Конечно", "Безусловно", "Вы абсолютно правы", "Надеюсь, это помогло", "Сообщите мне, если хотите", "Ниже представлен подробный обзор".
- Remove knowledge disclaimers: "по состоянию на [дата]", "на момент моего обучения", "в предоставленных результатах поиска", "конкретных деталей мало, но...". If data is missing, say so, do not generate text around the gap.
- Strip `utm_source=openai`, `utm_source=chatgpt.com` and other service artifacts from links.
- Verify every link, DOI, ISBN: the page opens, the source really says what is attributed to it, author and year match. For books give a page. A plausible but nonexistent source is worse than no source.

## 8. Final check
Re-read every sentence and ask: what is concrete here? If nothing, delete it or replace it with a fact. Add what a model does not have: own experience, real numbers, a position with arguments.

## Mechanical check

`lint.py` in this skill's directory (`${CLAUDE_SKILL_DIR}/lint.py`) catches what a model tends to miss and fixes nothing. Run it on the source text before marking tells and on the final text before handing it over:

```bash
python3 "${CLAUDE_SKILL_DIR}/lint.py" draft.md
printf '%s' "$TEXT" | python3 "${CLAUDE_SKILL_DIR}/lint.py"
```

It prints "line: rule: fragment" and exits with 1 when something is found. The rules are dash, quotes, utm, chatbot and emoji.

If Python is not available, check by hand. Look for the em dash, en dash and `--` used as a dash outside code, links, frontmatter and ">" quotes. Look for guillemets and curly quotes. Look for `utm_source=openai` and `utm_source=chatgpt.com` in links. Read the first and last lines for chatbot phrases ("Конечно", "Ниже представлен", "Надеюсь, это помогло", "Сообщите, если хотите"). Check headings and list items for emoji.
