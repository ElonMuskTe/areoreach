import serial
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec
import math

data ={ 'id': [],
        'x' :[],
        'y' : [],
        'z' : [],
        't' : [],
        'p' : [],
        'oxygen' : [],
        'co' : [],
        'humidity' : [],
        'gas' : [],
        'air' : [],
        'rssi' : [],
        'elements' : ['1','2','3','4','5','6','7','8','9','.','-',' ']
    }
#Stworzenie pliku w pythonie, wtedy zawsze go otworzymi nie zależnie jaki komputer będzie 
try:
            file=open('data.txt','a')
            ip = 'data.txt'
except:
    print("Jak to możliwe xD")
    
def licz(idealna,aktulana):
        wspolczynik = 1-abs((1-(math.log(aktulana)/(math.log(idealna))))/(1+(math.log(aktulana)/(math.log(idealna)))))
        return wspolczynik

ser = serial.Serial()
ser.budrate = 115200
ser.port = 'COM6'
ser.parity = serial.PARITY_NONE
ser.bytesize = 8
ser.stopbits = 1
ser.open()

def read_data():
    dane = bytes.decode(ser.read_until(),"utf-8") #wczytanie danych z arduino
    dane_podzielone = dane.split(" ")
    try:
        data['id'].append(int(dane_podzielone[0]))
    except:
        data['id'].append(0)
    try:
        data['x'].append(float(dane_podzielone[1]))
    except:
        data['x'].append(None)
    try:
        data['y'].append(float(dane_podzielone[2])) #Szeregowe wczytać połączenie
    except:
            pass
    try:
        data['z'].append(float(dane_podzielone[3]))
    except:
        pass
    try:
        data['t'].append(float(dane_podzielone[4]))
    except:
        data['t'].append(313)
    try:
        data['p'].append(int(dane_podzielone[5]))
    except:
        data['p'].append(101300)
    try:
        data['oxygen'].append(float(dane_podzielone[6]))
    except:
        data['oxygen'].append(21)
    try:
        data['co'].append(int(dane_podzielone[7]))
    except:
        data['co'].append(280)
    try:
        data['humidity'].append(float(dane_podzielone[8]))
    except:
        data['humidity'].append(21)
    try:
        data['gas'].append(int(dane_podzielone[9]))
    except:
        data['gas'].append(100)
    try:
        data['air'].append(int(dane_podzielone[10]))
    except:
        data['air'].append(2)
    try:
        data['rssi'].append(int(dane_podzielone[11]))
    except:
        pass
    print(data['id'],data['x'],data['y'],data['z'],data['t'],data['p'],data['oxygen'],data['co'],data['humidity'],data['gas'],data['air'],data['rssi'])

def graph():
    plt.clf()
    
    plt.subplot(231)
    plt.xlabel('time [s]')
    plt.ylabel('K')
    plt.plot(data['id'], data['t'], marker='o', color="blue") 
    plt.yscale('linear')
    plt.title('Temperature')
    plt.grid(True)
    
    plt.subplot(232)
    plt.plot(data['id'], data['p'], marker='o', color="green") 
    plt.xlabel('czas [s]')
    plt.ylabel('Pa')
    plt.yscale('linear')
    plt.title('pressure')
    plt.grid(True)
    
    plt.subplot(233)
    plt.xlabel('time [s]')
    plt.ylabel('m')
    plt.plot(data['id'], data['y'], marker='o', color="magenta") 
    plt.yscale('linear')
    plt.title('height[m]')
    plt.grid(True)

    plt.subplot(234)
    plt.xlabel('time [s]')
    plt.ylabel('%')
    plt.plot(data['id'], data['oxygen'], marker='o', color="cyan") 
    plt.yscale('linear')
    plt.title('O2[%]')
    plt.grid(True)

    plt.subplot(235)
    plt.xlabel('time [s]')
    plt.ylabel('ppm')
    plt.plot(data['id'],data['co'], marker='o', color="orange") 
    plt.plot(data['id'], data['gas'], marker='o', color="brown") 
    plt.yscale('linear')
    plt.title('Gas i CO2')
    plt.grid(True)
    
    plt.pause(1)
    plt.subplots_adjust(hspace=0.5)


class Baza():
    def future(self,data):
        n=54
        w=37
        if(data['id'][-1]>1):
            try:
                c=(math.sqrt((data['x'][-1] - n)**2 + (data['x'][-1] - w)**2))*73000 # ostatnie współrzędne
                result1=math.degrees(math.atan(data['y'][-1]/c))
                c=(math.sqrt((data['x'][-2] - n)**2 + (data['z'][-2] - w)**2))*73000 #Przedostatnie
                result2=math.degrees(math.atan(data['y'][-1]/c))
                x3=data['x'][0]-(data['x'][-1]-data['x'][-2])*len(data['x'])
                z3=data['z'][0]-(data['z'][-1]-data['z'][-2])*len(data['z'])
                c=(math.sqrt((x3 - n)**2 + (z3 - w)**2))*73000 #Przewidywanie
                result3=math.degrees(math.atan(data['y'][-1]/c))
                falling_speed = data['y'][-2] - data['y'][-1]  # prędkość opadania
                wind=(math.sqrt((data['x'][-1] - n)**2 + data['x'][-1] - w)**2)*73000-(math.sqrt(( data['x'][-2] - n)**2 + ( data['z'][-2] - w)**2))*73000
                #Wypiswanie danych dla mnie w osatecnej wersji nie musi być
                print(result1,"stopni ")
                print(result2,"stopni ")
                print(result3,"stopni ")
                print(falling_speed,"m/s")
                print(wind,'m/s')
            
            except:
                if(id[-1]<1):
                    pass
                elif(id[-1]>1):
                    print("dane przychodzą w niekomplecie lub samo id jest")
                else:
                    print("Coś się zniszyczło i tyle, cieżko określić co, może dizelenie przez 0 XD ")
    def calcus(self,data):
        ideal_t = 293 # temperatura w Kelvinach
        ideal_p = 101325 # ciśnienie
        ideal_oxygen = 0.21 #tlen
        ideal_co = 280 #Dwultelenk węgla
        ideal_humidity = 0.4 # Wilgotnosć
        ideal_gas = 100 #Trujące gazy w powietrzu
        ideal_air = 2 #czytość powietrza 
        global współczynik
        współczynik=licz(ideal_air,data['air'][-1])*licz(ideal_t,data['t'][-1])*licz(ideal_p,data['p'][-1])*licz(ideal_oxygen,data['oxygen'][-1])*licz(ideal_gas,data['gas'][-1])*licz(ideal_humidity,data['humidity'][-1])*licz(ideal_co,data['co'][-1])
        print(współczynik)

        
    def file(self, data):
     try:
        with open(ip, 'a') as file:  # Użyj trybu 'a' (append), aby dodać zawartość do pliku
            file.write(" ".join(str(val) for val in data['id'][-1:]))  # Zapisz tylko ostatni element z każdego klucza
            file.write(" ".join(str(val) for val in data['x'][-1:]))
            file.write(" ".join(str(val) for val in data['y'][-1:]))
            file.write(" ".join(str(val) for val in data['z'][-1:]))
            file.write(" ".join(str(val) for val in data['oxygen'][-1:]))
            file.write(" ".join(str(val) for val in data['co'][-1:]))
            file.write(" ".join(str(val) for val in data['humidity'][-1:]))
            file.write(" ".join(str(val) for val in data['gas'][-1:]))
            file.write(" ".join(str(val) for val in data['air'][-1:]))
            file.write(" ".join(str(val) for val in data['p'][-1:]))
            file.write(" ".join(str(val) for val in data['t'][-1:]))
            file.write(" ".join(str(val) for val in [współczynik]))
            file.write(" ".join(str(val) for val in data['rssi'][-1:]))
            file.write("\n")  # Nowa linia po zapisaniu jednego zestawu danych
     except Exception as e:
        print(f"Błąd w zapisie pliku {ip}: {e}")

analayze=Baza()
while (True):
    read_data()  # Odczytaj dane
    graph()  # Zaktualizuj wykres
    analayze.future(data)
    analayze.calcus(data)
    analayze.file(data)


