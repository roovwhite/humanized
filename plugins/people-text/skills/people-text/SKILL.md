---
name: "people-text"
description: "Use when writing or editing any text that must read as human-written (posts, articles, channel content, work texts, resumes) so it does not look AI-generated."
---

# people-text

Rules for writing text that reads as written by a person. Based on the Russian Wikipedia essay "Википедия:Признаки сгенерированности текста" (ВП:ПРГЕН). The signs are observations, not proof of generation, and detectors are unreliable. The goal is concrete, living text, not just evading checks.

Apply when drafting new text and when editing an existing draft. When editing, point out each violation found and fix it. Write in the language of the request (usually Russian). Punctuation: only "-" (hyphen), never the em dash; straight double quotes "", never guillemets.

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
- Do not define the title as a term ("'Влияние X на Y' относится к..."). Start with substance.

## 4. Constructions and rhythm
- No "не только... но и..." and "это не просто X, это Y".
- No forced rule of three (three adjectives, three short phrases). Use as many items as really exist.
- Participial phrases must agree with the subject: "Используя этот метод, результаты улучшаются" is wrong. No chancery filler ("окружающая среда вокруг нас").
- Merisms "от X до Y" only when there is a real scale between the extremes.
- Do not swap a name or term for synonyms ("главный герой", "ключевой игрок", "упомянутый субъект"). Repeat the name.
- Avoid marker words and English calques: "погружаться", "гобелен", "переплетение", "нюанс", "способствовать", "являться", "представляет собой", "в рамках", "данный".
- Do not start paragraphs with "кроме того", "более того", "вдобавок". Vary sentence length: short next to long.

## 5. Formatting
- Headings in sentence case, not Каждое Слово С Заглавной.
- No bold on key terms in the middle of sentences, no "key takeaways" bolding.
- No vertical lists of the form "1. **Заголовок**: пояснение" for connected prose. Use paragraphs; lists only where they are really needed.
- No emoji, especially in headings and lists.
- No em dash. Use comma, parentheses, colon, or a hyphen.
- No Markdown symbols (##, **, ---) if the platform does not render them.

## 6. Service traces and links
- Remove chatbot phrases: "Конечно", "Безусловно", "Вы абсолютно правы", "Надеюсь, это помогло", "Сообщите мне, если хотите", "Ниже представлен подробный обзор".
- Remove knowledge disclaimers: "по состоянию на [дата]", "на момент моего обучения", "в предоставленных результатах поиска", "конкретных деталей мало, но...". If data is missing, say so, do not generate text around the gap.
- Strip utm_source=openai, utm_source=chatgpt.com and other service artifacts from links.
- Verify every link, DOI, ISBN: the page opens, the source really says what is attributed to it, author and year match. For books give a page. A plausible but nonexistent source is worse than no source.

## 7. Final check
Re-read every sentence and ask: what is concrete here? If nothing, delete it or replace it with a fact. Add what a model does not have: own experience, real numbers, a position with arguments.