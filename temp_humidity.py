import requests
import time
import adafruit_dht
import configuration as conf

KEY = conf.KEY

def pushData(temp, humidity):
    '''Takes temperature and humidity readings and pushes data to ThingSpeak cloud'''
    #Set up request url and parameters
    url = conf.url
    params = {'key': KEY, 'field1': temp, 'field2': humidity}

    #Publish values to ThingSpeak
    res = requests.get(url, params=params)
    print("Temperature : ",temp,"℃ | Humidity : ",humidity,"%")
    print("Data pushed on to the cloud successfully...")


def getData(pin):
    try:
        humidity, temperature = adafruit_dht.read_retry(11, pin)
        return humidity, temperature
    except:
        print("Error reading sensor data")
        return 0,0

if __name__ == "__main__":
    while True:
        pin = conf.PIN
        humidity, temp = getData(pin)
        if humidity!=0 or temp!=0 :
            pushData(temp,humidity)
        time.sleep(10)