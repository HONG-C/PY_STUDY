#기억 포인트
#c언어에선 &&이지만 파이썬에선 &
'''
*있는 문장 주석처리할 때
컨트롤+슬래시(물음표)
'''
#부모 클래스 
class drive_time:
    def __init__(self,angle,speed,time):
      self.angle=angle
      self.speed=speed
      self.time=time
#클래스 내의 함수=메서드
#상속  
class drive_time_A(drive_time):
    def __init__(self,angle,speed,time):
      drive_time.__init__(self,angle,speed,time)
      
#메소드 생성
    def attack(self):#메소드 앞에는 무조건 self 적기!
      print("조향각:{0}속도:{12시간:{2}"\#\이거 쓰면 다음줄로 이어짐 
    .format(self.angle,self.speed,self.damage))