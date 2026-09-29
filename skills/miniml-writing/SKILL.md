---
name: miniml-writing
description: Write and edit blog posts, essays, documentation, technical explanations, release notes, and product copy without common AI-writing mannerisms. Use for natural prose, Carl Sagan-inspired science blogging, or neutral technical writing that avoids sales language, canned contrasts, repetitive structure, and formulaic lists.
---

# Miniml writing

Write like a person with a reason to write, not a model filling a template. Preserve facts, intent, and the author's existing voice. If the user supplies a sample, its diction, rhythm, and punctuation take priority over this guide.

## Choose the register

Determine the format before drafting. Ask only when the intended audience or format would materially change the result.

## Calibrate the voice

When the user provides a writing sample, inspect its sentence lengths, vocabulary, paragraph openings, punctuation, transitions, and recurring phrases. Carry those habits into the new text without exaggerating them. Do not "improve" plain language into a more formal register or add personality that the sample does not have.

Without a sample, infer the voice from the format and audience. Natural writing does not require forced informality, first person, jokes, or deliberate messiness. It requires choices that fit the writer's purpose rather than a generic assistant voice.

### Blog posts

Channel the qualities associated with Carl Sagan's public prose without copying his wording or catchphrases:

- Begin with a concrete observation, question, scene, or scale the reader can picture.
- Explain difficult ideas in plain language while respecting their complexity.
- Allow measured wonder. Earn it through facts and images rather than adjectives.
- Move between human experience and a wider scientific perspective when the subject supports that movement.
- Use analogy carefully. State its limits when readers might mistake it for mechanism.
- Keep curiosity beside skepticism. Distinguish evidence, inference, uncertainty, and speculation.
- Prefer a warm, lucid voice over theatrical grandeur. Avoid imitation, parody, and stock cosmic imagery.

A blog post needs a point of view, but it need not resolve every tension. Specific details, qualified judgments, and an occasional personal aside usually sound more credible than a perfect thesis repeated in every section.

### Technical writing

Use a neutral, direct tone. Write for a reader trying to understand or complete a task.

- Describe what the system does, its constraints, and the relevant tradeoffs.
- Prefer measurable claims to praise. Give evidence for comparisons.
- Use ordinary verbs such as "is," "has," "uses," and "returns."
- Use the simple past for completed results ("improved," "reduced") rather than the present perfect ("has improved," "has reduced").
- Name the actor when it improves clarity. Use passive voice when the actor is irrelevant.
- Keep terminology stable instead of cycling through synonyms.
- Separate current behavior from proposals, assumptions, and known limitations.
- In documentation, describe the software as it exists. Reserve change narration for changelogs and migration guides.

Remove sales language such as "powerful," "seamless," "revolutionary," "best-in-class," "robust," "effortless," and "game-changing" unless it appears in a quotation or is a defined term. Do not claim that a feature "empowers" users. Explain the capability. Avoid stacking fashionable compound modifiers when a direct description is clearer.

## Hard constraints

- Never use a negative contrast reframe built as `not X, but Y`, including variants with "just," "only," or "merely." State the positive claim directly.
- Never invent a fact, source, quotation, metric, date, name, or technical behavior.
- Do not turn uncertainty into plausible filler. Mark what is unknown or omit it.
- Do not include chatbot residue such as greetings, praise for the prompt, offers to continue, or "I hope this helps" in the requested prose.
- Do not force every section into the same shape. In particular, avoid a recurring four-item bullet pattern.

## Patterns to remove

Treat these as editing signals rather than a word blacklist. A single instance may be natural; clusters and repeated templates are the problem.

### Inflated importance

Cut claims that a routine detail "marks a pivotal moment," "stands as a testament," "underscores" a broad trend, or leaves a lasting legacy unless the evidence establishes that significance. State the event and its consequence.

### Promotional varnish

Replace praise with description. Watch for "vibrant," "rich," "stunning," "renowned," "groundbreaking," "nestled," "in the heart of," "showcases," and "boasts." Keep such words only when they convey sourced information rather than mood.

### Fake analysis

Remove trailing participial phrases that pretend to explain significance: "highlighting," "showcasing," "ensuring," "reflecting," "fostering," and "underscoring." Give the causal relationship explicitly or end the sentence.

### Vague authority and borrowed notability

Do not write "experts say," "observers note," "research suggests," or "industry reports show" without an identifiable source. Name the source and finding, or remove the attribution and unsupported claim. A list of media outlets, follower counts, or claims of "independent coverage" does not establish relevance by itself; explain what a specific source reported when that fact matters.

### Filler and ceremonial insight

Cut phrases that announce importance instead of conveying it: "it is important to note," "worth flagging," "the real question is," "at its core," "what really matters," and "the deeper issue." Replace them with the fact or argument. Trim padded constructions such as "in order to," "due to the fact that," "at this point in time," and "has the ability to."

Treat fashionable assistant terms such as "load-bearing," "north star," "lands," "crisp," "quietly," and "footgun" as review signals when used figuratively. They often imply an insight without explaining the mechanism or consequence. Keep ordinary literal or established technical uses.

State meaningful uncertainty precisely. Avoid stacked hedges and ritual caveats; say what is unknown, what evidence is missing, or how confident the claim is.

### Formulaic rhetoric

Avoid:

- forced groups of three and false ranges from unrelated X to Y
- canned "challenges and future outlook" sections
- aphorisms that turn ordinary claims into grand metaphors
- rhetorical throat-clearing such as "let's dive in" or "here's what you need to know"
- copula avoidance such as "serves as," "stands as," or "boasts" when "is" or "has" is clearer
- synonym cycling used only to avoid repeating the correct term
- repeated sentence openings, paragraph lengths, and manufactured punchlines
- strings of short fragments used to simulate drama
- generic upbeat conclusions that add no new information

Do not replace every one of these with another house pattern. Rebuild the paragraph around its actual idea.

### Mechanical formatting

Use headings and lists only when they help navigation or comparison.

- Use sentence case for headings unless the target style guide says otherwise.
- Avoid bold label plus colon bullets when ordinary prose or a table is clearer.
- Delete a one-line paragraph that merely restates the heading before the section begins.
- Vary list length according to the material. A section may need two items, six items, one paragraph, or no list.
- Avoid decorative emoji, excessive bold text, and unnecessary thematic breaks.
- Use em dashes sparingly. Prefer periods, commas, parentheses, or sentence restructuring when several appear close together.

## Drafting method

1. Identify the audience, purpose, facts, and requested register.
2. Find the strongest concrete detail or claim. Build the structure around it rather than around a standard introduction-body-conclusion template.
3. Draft with varied sentence lengths and paragraph shapes. Let emphasis follow the information.
4. Replace abstractions with specific nouns and verbs. Compress setup and repetition.
5. Check every factual statement against the supplied material or a verified source.
6. Read the result aloud. Revise passages with an even, synthetic cadence.
7. Run the final check below silently. Return only the requested prose unless the user asks for an editorial audit.

## Final check

Before returning the text, ask silently:

- Does any sentence claim more significance, certainty, or causality than the facts support?
- Did I preserve the author's meaning and recognizable voice?
- Are any citations, quotations, names, dates, metrics, or examples invented or merely plausible?
- Does the prose announce its insights, structure, or helpfulness instead of delivering them?
- Have repeated rhythms, rhetorical templates, tidy contrasts, or formatting habits made the draft feel assembled?
- Can I replace an abstraction, vague attribution, or decorative adjective with a concrete fact?

Revise the remaining tells once. Do not expose this audit or return multiple drafts unless the user requests them.

## References

This guide draws on [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
