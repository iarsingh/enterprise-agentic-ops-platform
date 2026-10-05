from agentx.progression import capstone

def test_capstone_supervisor():
    out = capstone("explain outage for tenant acme", "acme")
    assert out["supervisor"] is True
    assert out["applied"] is False
    assert "sre" in out["agents"]

def test_capstone_refuses_skip_approval():
    out = capstone("execute now on production", "acme")
    assert out["refused"] is True

