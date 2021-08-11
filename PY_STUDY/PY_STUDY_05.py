#기억 포인트
#c언어에선 &&이지만 파이썬에선 &
'''
*있는 문장 주석처리할 때
컨트롤+슬래시(물음표)
'''
class drive_time:
    def __init__(self,angle,speed,time):
      self.angle=angle
      self.speed=speed

class drive_time_A(drive_time):
    def __init__(self,angle,speed,time):
      drive_time.__init__(self,angle,speed,time)
      
