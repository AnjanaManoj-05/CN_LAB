def xor(a, b):
    """XOR between two binary strings of equal length (include first bit)."""
    result = ""
    for i in range(len(a)):
        result += '0' if a[i] == b[i] else '1'
    return result


def divide(dividend, divisor):
    """Perform Mod-2 division and return remainder."""
    divisor_len = len(divisor)
    tmp = dividend[0:divisor_len]

    for i in range(divisor_len, len(dividend)):
        if tmp[0] == '1':
            tmp = xor(tmp, divisor)[1:] + dividend[i]
        else:
            tmp = xor(tmp, '0' * divisor_len)[1:] + dividend[i]

    # Final step
    if tmp[0] == '1':
        tmp = xor(tmp, divisor)[1:]
    else:
        tmp = xor(tmp, '0' * divisor_len)[1:]

    return tmp  # remainder of length (len(divisor)-1)


def crc_encode(data, divisor):
    """Encode data using CRC."""
    appended_data = data + '0' * (len(divisor) - 1)
    remainder = divide(appended_data, divisor)
    transmitted = data + remainder
    return transmitted, remainder


def crc_check(received, divisor):
    """Check for errors in received data."""
    remainder = divide(received, divisor)
    return all(bit == '0' for bit in remainder)


# ---------------- MAIN PROGRAM ----------------
if __name__ == "__main__":
    data = input("Enter dataword (binary): ").strip()
    divisor = input("Enter divisor (generator polynomial in binary): ").strip()

    transmitted, remainder = crc_encode(data, divisor)
    print(f"\nCRC Remainder: {remainder}")
    print(f"Transmitted Frame: {transmitted}")

    print("\n--- Receiver Side ---")
    received = input("Enter received frame (to check for error): ").strip()

    if crc_check(received, divisor):
        print("✅ No error detected in received data.")
    else:
        print("❌ Error detected in received data.")
