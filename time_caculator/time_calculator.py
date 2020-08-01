def add_time(start, duration):
  time,day = start.split()

  startLeft = int(time.split(':')[0])
  startRight = int(time.split(':')[1])
  durationLeft = int(duration.split(':')[0])
  durationRight = int(duration.split(':')[1])
  resultHr = startLeft + durationLeft
  resultMin = startRight + durationRight

  if resultMin > 59:
    resultMin -= 60
    resultHr += 1
  
  while resultHr > 12:
    resultHr -= 12
    day = "PM" if day == "AM" else "AM"

  new_time = f"{resultHr}:{str(resultMin).zfill(2)} {day}"



  return new_time