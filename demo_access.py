"""Demo-mode access helpers.

This public demo identity is for exploration only. It is NOT authentication.
Never use these flags as authorization for production data or privileged actions.
"""
from __future__ import annotations

DEMO_EMAIL = "demo@protacnexus.local"
DEMO_USERNAME = "Demo User"
DEMO_ROLE = "demo"


def is_demo_user(session_state) -> bool:
    """Return True when the current Streamlit session is the public demo user."""
    return bool(session_state.get("demo_mode", False)) or session_state.get("user_role") == DEMO_ROLE


def block_demo_write(session_state, st, action: str = "This action") -> bool:
    """Display a safe notice and return True when a write must be blocked."""
    if is_demo_user(session_state):
        st.warning(
            f"{action} is disabled in Demo Mode. "
            "No real request, payment, email, or database change has been made."
        )
        return True
    return False
