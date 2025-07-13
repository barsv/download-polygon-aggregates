---
applyTo: ".github/copilot-instructions.md"
---

# 🧠 Guidelines for Generating `.github/copilot-instructions.md`

## Core Principle: Describe, Don't Prescribe

When generating `copilot-instructions.md`, prefer **descriptive statements** over **imperative commands**.

### ❌ Avoid (imperative tone):
- "Use PyArrow for parquet files"
- "Always apply `searchsorted()` for filtering"
- "Never use boolean indexing"

### ✅ Prefer (descriptive tone):
- "The project uses PyArrow for parquet files"
- "Timestamp filtering used `searchsorted()` for performance"
- "Boolean indexing was avoided due to efficiency concerns"

---

## Why This Matters

- **Flexibility**: Descriptive guidance allows context-aware reasoning.
- **Evolution**: Hard rules become outdated as the codebase evolves.
- **Autonomy**: Agents should assess applicability based on context.

---

## Key Patterns to Follow

- Explain **"what & why"** instead of dictating "how & what to do"
- Provide **architectural context**
- Include **historical reasoning**, where available

---

## Useful Phrase Templates

| Descriptive | Imperative (Avoid) |
|-------------|--------------------|
| "The project uses..." | "Use..." |
| "The architecture employs..." | "Build with..." |
| "This pattern was adopted..." | "Always do..." |
| "The codebase typically..." | "You must..." |

---

## When Directives Are Appropriate

Use direct instructions **only** for critical constraints:

- **Security**: `API keys must be in api_key.txt`
- **Compatibility**: `Frontend expects ascending time order`
- **Project conventions**: `Comments written in English`

---

🎯 **Goal**: Help future agents understand the logic and patterns of the project — not simply follow rigid rules.
