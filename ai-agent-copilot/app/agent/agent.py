# Minimal agent loop (placeholder)
from app.tools.crm_tool import crm_lookup
from app.tools.kb_tool import kb_search
from app.tools.sql_tool import run_sql
from app.guards.safety import sanitize

def run_agent(question: str, user_id: str):
    q = sanitize(question)
    # naive tool routing
    if "customer" in q.lower():
        data = crm_lookup(user_id)
        return (f"Customer snapshot: {data}", ["crm:customer_profile"])
    docs = kb_search(q)
    if "revenue" in q.lower():
        rows = run_sql("SELECT * FROM faux_readonly_view LIMIT 5")
        return (f"KB: {docs[:1]} SQL rows: {len(rows)}", ["kb","sql"])
    return (f"KB: {docs[:1]}", ["kb"])
