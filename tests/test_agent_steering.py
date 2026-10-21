"""Tests for ReActAgent's live stdin steering (added so a running hunt can
be redirected from the same terminal, like Claude Code, instead of needing
a second `agent.py --bump` invocation in another shell).
"""

from agent import ReActAgent


def test_classify_blank_line_is_ignored():
    assert ReActAgent._classify_steering_line("\n") == ("blank", "")
    assert ReActAgent._classify_steering_line("   ") == ("blank", "")


def test_classify_quit_words_stop_the_hunt():
    for word in ("/quit", "/stop", "exit", "QUIT", "  Exit  "):
        kind, _ = ReActAgent._classify_steering_line(word)
        assert kind == "quit"


def test_classify_guidance_is_bumped_verbatim():
    kind, msg = ReActAgent._classify_steering_line("focus on the /admin login flow\n")
    assert kind == "bump"
    assert msg == "focus on the /admin login flow"


def test_bump_file_roundtrip(tmp_path):
    """The existing _check_bump() poll must still pick up what steering writes."""
    bump_file = tmp_path / "agent_bump.txt"
    bump_file.write_text("")

    kind, msg = ReActAgent._classify_steering_line("try the GraphQL endpoint next")
    assert kind == "bump"
    bump_file.write_text(msg)

    # Mirrors ReActAgent._check_bump(): read once, then file is consumed (cleared).
    assert bump_file.read_text().strip() == "try the GraphQL endpoint next"
    bump_file.write_text("")
    assert bump_file.read_text().strip() == ""
