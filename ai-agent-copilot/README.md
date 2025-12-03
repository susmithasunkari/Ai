# AI Agent — Support & Risk Ops Copilot (Medium→Hard)

LLM agent that answers with sources, calls tools (CRM/search/DB), and logs actions to reduce handle time and deflect tickets.

## Features
- Tool‑use via adapters (CRM, KB search, read‑only SQL)
- Hybrid retrieval (BM25 + vectors) with metadata filters
- Guardrails: PII redaction, prompt‑injection defenses
- EKS‑ready FastAPI service with SSO
- Canary deploy & rollback; latency/quality SLOs

## Quick Start
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```
