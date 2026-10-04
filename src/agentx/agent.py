TOOLS = ["auth", "supervisor", "rag", "data", "cloud", "sre", "mcp", "approval", "audit"]
WRITES = ("execute now", "skip approval", "destroy production",)

def run(goal, payload):
    if not goal or not str(goal).strip():
        raise ValueError("goal is empty")
    low = goal.lower()
    if any(w in low for w in WRITES):
        return {"refused": True, "reason": "destructive action requires a human", "applied": False, "tools": []}
    result = {"stages": TOOLS, "tenant": payload.get("tenant", "default")}
    return {"refused": False, "tools": TOOLS, "trace": result, "applied": False, "needs_approval": False}
