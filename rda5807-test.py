''' Пример работы с RDA5807
    Самая стабильная работа получилась при работе с адресам 0х11  '''

from machine import SoftI2C, Pin
import time, machine

i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)
#addr = i2c.scan()  # 16, (17=0x11), 96
#print(addr)



def rda_write(): # отправляем данные в RDA
    i2c.writeto_mem(0x11, 0x02, b'\xe3\x01')
    #i2c.writeto_mem(0x11, 0x03, b'\x10')
    #i2c.writeto_mem(0x11, 0x04, b'\x00\x10')
    i2c.writeto_mem(0x11, 0x05, b'\x08\x82')
    #i2c.writeto_mem(0x11, 0x06, b'\x00\x00')
    #i2c.writeto_mem(0x11, 0x07, b'\x42\x00')
    #i2c.readfrom(0x11, 2)
  
    


rda_write()
# time.sleep_ms(1000)
# h = i2c.readfrom_mem(0x11, 0x0a, 1)
# h = int.from_bytes(h, 'big')
# print(100*(int(h))+87.0)




