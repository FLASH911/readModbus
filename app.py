from pymodbus.client.sync import ModbusTcpClient

client = ModbusTcpClient('127.0.0.1')
client.write_coil(2, True)
result = client.read_coils(2,1)
print(result.bits[0])
client.close()

#sudo '/home/zed/diagslave' -m tcp
