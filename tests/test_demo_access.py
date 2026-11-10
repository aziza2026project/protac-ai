from protac_nexus.demo_access import (
    DEMO_EMAIL,
    DEMO_ROLE,
    DEMO_USERNAME,
    is_demo_user,
    block_demo_write,
)


class FakeStreamlit:
    def __init__(self):
        self.messages = []

    def warning(self, message):
        self.messages.append(message)


def test_demo_identity_constants_are_stable():
    assert DEMO_EMAIL == "demo@protacnexus.local"
    assert DEMO_USERNAME == "Demo User"
    assert DEMO_ROLE == "demo"


def test_demo_user_detected_from_session_flag_or_role():
    assert is_demo_user({"demo_mode": True})
    assert is_demo_user({"user_role": "demo"})
    assert not is_demo_user({"user_role": "member"})


def test_demo_write_is_blocked_and_explained():
    fake_st = FakeStreamlit()
    blocked = block_demo_write({"demo_mode": True}, fake_st, "Submission")
    assert blocked is True
    assert len(fake_st.messages) == 1
    assert "disabled in Demo Mode" in fake_st.messages[0]


def test_non_demo_write_is_not_blocked():
    fake_st = FakeStreamlit()
    blocked = block_demo_write({"user_role": "member"}, fake_st, "Submission")
    assert blocked is False
    assert fake_st.messages == []
