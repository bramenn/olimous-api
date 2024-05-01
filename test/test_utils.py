from app.utils.generate_qr import qr_str


def test_validate_type():
    qr_code = qr_str(1, 1)
    assert isinstance(qr_code, str)


def test_validate_structure():
    qr_code = qr_str(164, 6546)
    split_qr_code = qr_code.split("-")

    assert split_qr_code[0] == "164"
    assert split_qr_code[1] == "6546"
