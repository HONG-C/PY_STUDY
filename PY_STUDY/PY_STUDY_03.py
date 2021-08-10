#챕터 21

print("챕터 21")
#여러줄 주석=컨트롤 슬래시
print("\n\n")


#챕터 22
print("챕터 22")
print("\n\n")
#로봇 만들때 쓰임처:drive 모듈 만들때 기억!

#챕터 23
print("챕터 23")
#일반 유닛(부모클래스)
class Unit:#생성자
  def __init__(self,name,hp):
    self.name=name#self가 없는 name은 인자로 전달받은 변수!
    self.hp=hp
    print("{0}유닛이 생성되었습니다".format(self.name))
    print("체력{0}".format(self.hp))

#클래스 내의 함수=메서드
#상속  
#공격 유닛(자식클래스)
class AttackUnit(Unit):
  def __init__(self,name,hp,damage):
    Unit.__init__(self,name,hp)
    self.damage=damage
   
#메소드 생성
  def attack(self,location):#메소드 앞에는 무조건 self 적기!
    print("{0}:{1}방향으로 적군을 공격합니다.[공격력{2}]"\
    .format(self.name,location,self.damage))

  def damaged(self,damage):
    print("{0}:{1}데미지를 입었습니다.".format(self.name,damage))
    self.hp-=damage
    print("{0}:현재 체력은 {1} 입니다.".format(self.name,self.hp))
    if self.hp<=0:
      print("{0}:파괴되었습니다.".format(self.name))


medic1=Unit("메딕",40)
# marine3=Unit("마린")
#이렇게 필요한 인자 빠지면 객체 생성 불가!
wraith1=AttackUnit("레이스",80,5)
print("유닛이름:{0},체력{1}".format(medic1.name,medic1.hp))
wraith1.damaged(25)
print("유닛이름:{0},체력:{1}".format(wraith1.name,wraith1.hp))
wraith1.damaged(25)

print("\n\n")



#챕터 24

print("챕터 24")
#다중상속
#날 수 있는 기능을 가진 클래스
class Flyable:
  def __init__(self,flying_speed):
    self.flying_speed=flying_speed

  def fly(self,name,location):
    print("{0}:{1} 방향으로 날아갑니다.[속도{2}]"\
    .format(name,location,self.flying_speed))


#공중 공격 유닛 클래스(다중상속)부모가 여러 명
class FlyableAttackUnit(AttackUnit,Flyable):
  def __init__(self,name,hp,damage,flying_speed):
    AttackUnit.__init__(self,name,hp,damage)
    Flyable.__init__(self,flying_speed) 

wraith2=FlyableAttackUnit("빼앗은 레이스",80,6,5)
valkyrie=FlyableAttackUnit("발키리",200,6,5)
valkyrie.fly(valkyrie.name,"3시")
print("\n\n")



#챕터 25

print("챕터 25")
#건물(pass,super)
#다중상속때는 사용 금지!마지막에 있는 함수에 대해서만 init함수 호출 하므로!
class BuildingUnit(Unit):
  def __init__(self,name,hp,location):
    #Unit.__init__(self,name,hp,0)
    super().__init__(name,hp)#super 쓸때는 self생략!
    self.location=location

#서플라이 디폿:건물, 1개건물=8 유닛
supply_depot=BuildingUnit("서플라이 디폿",500,"7시")

# super 예시

class t_Unit:
  def ___init__(self):
    print("Unit 생성자")
    
class t_Flyable:
  def __init__(self):
    print("Flyable 생성자")

class t_FlyableUnit(t_Unit,t_Flyable):
  def __init__(self):
    super().__init__()

# 드랍쉽
dropship=t_FlyableUnit()
print("\n\n")


#챕터 26

print("챕터 26")
print("\n\n")



#챕터 27

print("챕터 27")
print("\n\n")


#챕터 28

print("챕터 28")
print("\n\n")


#챕터 29

print("챕터 29")
try:
  
  print("한자리 전용 나누기 전용 계산기입니다")
  nums=[]
  nums.append(int(input("첫번째 숫자를 입력하세요:")))
  nums.append(int(input("두번째 숫자를 입력하세요:")))
  #nums.append(int(nums[0]/nums[1]))
  nums.append(int(nums[0]/nums[1]))
  print("{0}/{1}={2}".format(nums[0],nums[1],nums[2]))
  if nums[0]>=10 and nums[1]>=10:
    raise ValueError


except ValueError:
  print("에러!잘못된 값을 입력하였습니다!")
except ZeroDivisionError as err:
  print(err)
# except:
#   print("알수 없는 에러가 발생하였습니다")
#   나머지 모든 에러에 대해선는 요걸로 처리 가능!
except Exception as err:
  print(err)

print("\n\n")


#챕터 30

print("챕터 30")
print("\n\n")



