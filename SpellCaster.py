#! /usr/bin/env python
 
# include uinput and time
import uinput, time
 
def PetrificusTotalus():
  # Full Body Bind - Score 141-143
  events = (uinput.KEY_P, uinput.KEY_T,  uinput.KEY_F ,  uinput.KEY_C ,  uinput.KEY_L ,  uinput.KEY_S)
  device = uinput.Device(events)

  time.sleep(1)

  pulse_time = 0.75
  sleep_time1 = 0.70
  sleep_time2 = 0.728
  sleep_time3 = 0.70
  sleep_time4 = 0.70
  sleep_time5 = 0.70
  sleep_time6 = 0.70  
  
  device.emit(uinput.KEY_P,1)  
  device.emit(uinput.KEY_P,0)  
  time.sleep(pulse_time)  
  device.emit(uinput.KEY_P,1)  
  device.emit(uinput.KEY_P,0)
  time.sleep(sleep_time1)

  device.emit(uinput.KEY_T,1)  
  device.emit(uinput.KEY_T,0)  
  time.sleep(pulse_time)  
  device.emit(uinput.KEY_T,1)  
  device.emit(uinput.KEY_T,0)
  time.sleep(sleep_time2)

  device.emit(uinput.KEY_F,1)  
  device.emit(uinput.KEY_F,0)  
  time.sleep(pulse_time)  
  device.emit(uinput.KEY_F,1)  
  device.emit(uinput.KEY_F,0)
  time.sleep(sleep_time3)

  device.emit(uinput.KEY_C,1)  
  device.emit(uinput.KEY_C,0)  
  time.sleep(pulse_time)  
  device.emit(uinput.KEY_C,1)  
  device.emit(uinput.KEY_C,0)
  time.sleep(sleep_time4)

  device.emit(uinput.KEY_T,1)  
  device.emit(uinput.KEY_T,0)  
  time.sleep(pulse_time)  
  device.emit(uinput.KEY_T,1)  
  device.emit(uinput.KEY_T,0)
  time.sleep(sleep_time5)

  device.emit(uinput.KEY_L,1)  
  device.emit(uinput.KEY_L,0)  
  time.sleep(pulse_time)  
  device.emit(uinput.KEY_L,1)  
  device.emit(uinput.KEY_L,0)
  time.sleep(sleep_time6)

  device.emit(uinput.KEY_S,1)  
  device.emit(uinput.KEY_S,0)  
  time.sleep(pulse_time)  
  device.emit(uinput.KEY_S,1)  
  device.emit(uinput.KEY_S,0)

def LocomotorWibbly():
  # Jelly Legs Curse - Score - 133
  events = (uinput.KEY_L, uinput.KEY_C,  uinput.KEY_M ,  uinput.KEY_T ,  uinput.KEY_W ,  uinput.KEY_B, uinput.KEY_Y)
  device = uinput.Device(events)
  
  time.sleep(1)

  pulse_time = 0.74
  sleep_time1 = 0.82
  sleep_time2 = 0.85
  sleep_time3 = 0.99
  sleep_time4 = 0.71
  sleep_time5 = 0.99
  sleep_time6 = 1.1
  
  device.emit(uinput.KEY_L,1)  
  device.emit(uinput.KEY_L,0)  
  time.sleep(pulse_time)  
  device.emit(uinput.KEY_L,1)  
  device.emit(uinput.KEY_L,0)
  time.sleep(sleep_time1)

  device.emit(uinput.KEY_C,1)  
  device.emit(uinput.KEY_C,0)
  time.sleep(pulse_time)  
  device.emit(uinput.KEY_C,1)  
  device.emit(uinput.KEY_C,0)
  time.sleep(sleep_time2)

  device.emit(uinput.KEY_M,1)  
  device.emit(uinput.KEY_M,0)  
  time.sleep(pulse_time)  
  device.emit(uinput.KEY_M,1)  
  device.emit(uinput.KEY_M,0)
  time.sleep(sleep_time3)

  device.emit(uinput.KEY_T,1)  
  device.emit(uinput.KEY_T,0)  
  time.sleep(pulse_time)  
  device.emit(uinput.KEY_T,1)  
  device.emit(uinput.KEY_T,0)
  time.sleep(sleep_time4)

  device.emit(uinput.KEY_W,1)  
  device.emit(uinput.KEY_W,0)  
  time.sleep(pulse_time)
  device.emit(uinput.KEY_W,1)  
  device.emit(uinput.KEY_W,0)
  time.sleep(sleep_time1)

  device.emit(uinput.KEY_B,1)  
  device.emit(uinput.KEY_B,0)  
  time.sleep(pulse_time)  
  device.emit(uinput.KEY_B,1)  
  device.emit(uinput.KEY_B,0)
  time.sleep(sleep_time5)

  device.emit(uinput.KEY_L,1)  
  device.emit(uinput.KEY_L,0)  
  time.sleep(pulse_time)  
  device.emit(uinput.KEY_L,1)  
  device.emit(uinput.KEY_L,0)
  time.sleep(sleep_time6)

  device.emit(uinput.KEY_Y,1)  
  device.emit(uinput.KEY_Y,0)  
  time.sleep(pulse_time)  
  device.emit(uinput.KEY_Y,1)  
  device.emit(uinput.KEY_Y,0)

def MimbleWimble():
  # Toung tying Spell - Score 138-137
  events = (uinput.KEY_M, uinput.KEY_I,  uinput.KEY_B ,  uinput.KEY_W ,  uinput.KEY_L )
  device = uinput.Device(events)
  
  time.sleep(1)

  pulse_time = 0.75
  sleep_time1 = 0.838
  sleep_time2 = 0.83
  sleep_time3 = 0.83
  sleep_time4 = 0.83
  sleep_time5 = 1.1

  device.emit(uinput.KEY_M,1)  
  device.emit(uinput.KEY_M,0)  
  time.sleep(pulse_time)  
  device.emit(uinput.KEY_M,1)  
  device.emit(uinput.KEY_M,0)
  time.sleep(sleep_time1)

  device.emit(uinput.KEY_M,1)  
  device.emit(uinput.KEY_M,0)  
  time.sleep(pulse_time)  
  device.emit(uinput.KEY_M,1)  
  device.emit(uinput.KEY_M,0)
  time.sleep(sleep_time2)

  device.emit(uinput.KEY_B,1)  
  device.emit(uinput.KEY_B,0)  
  time.sleep(pulse_time)  
  device.emit(uinput.KEY_B,1)  
  device.emit(uinput.KEY_B,0)
  time.sleep(sleep_time3)

  device.emit(uinput.KEY_W,1)  
  device.emit(uinput.KEY_W,0)  
  time.sleep(pulse_time)  
  device.emit(uinput.KEY_W,1)  
  device.emit(uinput.KEY_W,0)
  time.sleep(sleep_time4)

  device.emit(uinput.KEY_M,1)  
  device.emit(uinput.KEY_M,0)  
  time.sleep(pulse_time)  
  device.emit(uinput.KEY_M,1)  
  device.emit(uinput.KEY_M,0)
  time.sleep(sleep_time5)

  device.emit(uinput.KEY_L,1)  
  device.emit(uinput.KEY_L,0)  
  time.sleep(pulse_time)  
  device.emit(uinput.KEY_L,1)  
  device.emit(uinput.KEY_L,0)

def main():
  print '3'
  time.sleep(1)
  print '2'
  time.sleep(1)
  print '1'
  time.sleep(1)  
  print 'go!'    

  # LocomotorWibbly()  # Jelly Legs Curse - Score - 133
  PetrificusTotalus() # Full Body Bind - Score 141-143
  # MimbleWimble() # Toung tying Spell - Score 138-137


if __name__ == '__main__':
  main()
  
