from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    assert encrypt_message('AABBCC', 3) == "BAA_CCB"
    assert encrypt_message('ABBCCA', 4) == "AC_CBBA"
    assert encrypt_message('AABBCC', -1) == "CCBBAA"

    with pytest.raises(TypeError) as err:
        encrypt_message(1, 3)
    assert "tipo inválido para message" in str(err.value)
    assert err.type == TypeError

    with pytest.raises(TypeError) as err:
        encrypt_message('AABBCC', '3')
    assert "tipo inválido para key" in str(err.value)
    assert err.type == TypeError
