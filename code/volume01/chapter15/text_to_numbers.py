def encode_text(text: str) -> list[int]:
    return [ord(character) for character in text]


def decode_numbers(numbers: list[int]) -> str:
    return "".join(chr(number) for number in numbers)


if __name__ == "__main__":
    sentence = "Hello, LLM Engineer!"
    encoded = encode_text(sentence)
    decoded = decode_numbers(encoded)
    print(encoded)
    print(decoded)
