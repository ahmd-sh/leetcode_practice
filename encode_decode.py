# DISCLAIMER: scrappiest brute force because i'm not paying for LC premium

strs = ["mr", ".", "anderson"]

# ENCODE
encoded = ""

for s in strs:
    encoded += f"{len(s)}^#{s}"


# DECODE
decoded = []
i, encoding_len = 0, 2
while i < len(encoded):
    for j in range(i+1, len(encoded)-encoding_len):
        if encoded[j : j+encoding_len] == "^#":
            word_len = int(encoded[i:j])
            break
    decoded.append(encoded[j+encoding_len : j+encoding_len+word_len])
    i = j+encoding_len+word_len


# FOR MY SANITY
if decoded == strs:
    print("It works, trust me bro")
else:
    print("insert sorry excuse for my lack of skills")