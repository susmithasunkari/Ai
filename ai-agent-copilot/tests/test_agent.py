from app.agent.agent import run_agent

def test_basic():
    ans, src = run_agent("show customer details", "u123")
    assert "Customer snapshot" in ans
