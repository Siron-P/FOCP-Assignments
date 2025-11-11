'''9.The Unicode characters corresponding to these codes: 80, 121, 116, 104, 111, 110.'''

codes = [80, 121, 116, 104, 111, 110]
charac = [chr(code) for code in codes]

ans = ''.join(charac)
print(f"Unicode characters : {ans}")