str_original = 'Hello'

bytes_encoded = str_original.encode(encoding='utf-8')
print(bytes_encoded)


str_decoded = bytes_encoded.decode()
print(str_decoded)