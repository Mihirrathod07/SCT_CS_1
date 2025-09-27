# caesar.py
def caesar_shift(text: str, shift: int) -> str:
    """Shift letters by `shift`. Preserve case, leave non-letters unchanged."""
    shift = shift % 26
    result = []
    for ch in text:
        if 'A' <= ch <= 'Z':
            result.append(chr(ord('A') + (ord(ch) - ord('A') + shift) % 26))
        elif 'a' <= ch <= 'z':
            result.append(chr(ord('a') + (ord(ch) - ord('a') + shift) % 26))
        else:
            result.append(ch)
    return ''.join(result)

def encrypt(text: str, shift: int) -> str:
    return caesar_shift(text, shift)

def decrypt(text: str, shift: int) -> str:
    return caesar_shift(text, -shift)

def main():
    print("=== Caesar Cipher ===")
    mode = input("Choose (e)ncrypt or (d)ecrypt: ").strip().lower()
    text = input("Enter message: ")
    while True:
        try:
            shift = int(input("Enter shift (integer, e.g. 3): ").strip())
            break
        except ValueError:
            print("Please enter a valid integer for shift.")
    if mode.startswith('e'):
        out = encrypt(text, shift)
        print("\nEncrypted message:\n", out)
    else:
        out = decrypt(text, shift)
        print("\nDecrypted message:\n", out)

if __name__ == "__main__":
    main()
