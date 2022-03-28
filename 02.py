import time

def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))

if (눈이 감기면):
    start_time = time.time() # 스톱워치를 켜라

if (눈이 뜨이면):
    end_time = time.time() # 스톱워치를 꺼라

time_lapsed = end_time - start_time
time_convert(time_lapsed)