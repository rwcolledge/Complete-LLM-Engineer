from code.volume01.chapter15.text_to_numbers import decode_numbers, encode_text


def test_round_trip() -> None:
    text = "LLM"
    assert decode_numbers(encode_text(text)) == text
