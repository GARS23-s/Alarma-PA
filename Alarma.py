import time
import winsound
class alarma:
     def __init__(self,freq,dur):
           self.dur=dur
           self.freq=freq
           
     def fallo(self):
           
           
           
           reintento=0
           while reintento==0:
             clave=("230499")
             contraseña=input("INTRODUZCA LA CONTRASEÑA PARA INGRESAR A LA CASA")
             if contraseña==clave:
                  print("BIENVENIDO, TENGA UN BUEN DIA")
                  reintento=1
             else:
               
                print("INTRODUZCA LA CONTRASEÑA CORRECTA PARA APAGAR LA ALARMA Y PODER ENTRAR A LA CASA")
                freq=self.freq
              
                dur=self.dur
                
                s=0
                while(s!=4):
                 
                 winsound.Beep(freq, dur)
                 time.sleep(0.30)
                 winsound.Beep(freq, dur)
                 time.sleep(0.30)
                 s=s+1
                reintento=0      
                



O1=alarma(2500,900)
O1.fallo()
