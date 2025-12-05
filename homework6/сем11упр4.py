def test_caesar():
    key = 5
    cipher = Caesar(key)
    text1 = "привет"
    text1_encode = cipher.encode(text1)
    text1_decode = cipher.decode(text1)
    assert text1_decode == text1, "Error: decode(encode(text)) != text"
    
    text2 = "Привет,!."
    text2_encode = cipher.encode(text2)
    text2_decode=cipher.decode(enc2)
    assert text2_decode == text2, "Error: знаки препинания"
    
    alphabet = Caesar.alphabet
    encode3= cipher.encode(alphabet)
    decode3=cipher.decode(enc3)
    assert decode3 == alphabet, "Error: encode/decode нарушает алфавит"
    
    for i in range(len(Caesar.alphabet)):
        c = Caesar(k)
        t = "тест"
        assert c.decode(c.encode(t)) == t, f"Error при key={i}"

    print("код верный")
test_caesar()