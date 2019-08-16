symbols = '$¢£¥€¤'
output = [ord(symbol) for symbol in symbols if ord(symbol) > 127 ]
print(output)