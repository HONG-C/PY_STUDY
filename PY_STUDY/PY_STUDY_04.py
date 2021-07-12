#챕터 31
print("챕터 31")

#사용자 정의 예외처리

class BigNumberError(Exception):
  def __init__(self,msg):
    self.msg=msg
  def __str__(self):
    return self.msg

try:
  print("한자리 숫자 나누기 전용 계산기입니다.")
  num1=int(input("첫번째 숫자를 입력하세요:"))
  num2=int(input("두번째 숫자를 입력하세요:"))
  if num1>=10 or num2>=10:
    raise BigNumberError("입력값:{0},{1}".format(num1,num2))
  print("{0}/{1}={2}".format(num1,num2,int(num1/num2)))
except ValueError:
  print("잘못된 값을 입력하였습니다 한자리만 입력하세용")
except BigNumberError as err:
  print("에러가 발생했다")
  print(err)
finally:#프로그램 끝날때 무조건 실행
  print("계산기를 사용해 주셔서 감사합니다.")

print("\n\n")


#챕터 32
print("챕터 32")

print("\n\n")


#챕터 33
print("챕터 33")

print("\n\n")


#챕터 34
print("챕터 34")
# import theater_module
# theater_module.price(3)

# import theater_module as mv
# mv.price(3)

# from theater_module import *
# price(3)
from theater_module import price,price_morning

price(5)
price_morning(6)
# price_soldier(7)
#임포트 하지 않았기에 이 구문은 오류를 발생시킴!
from theater_module import price_soldier as ps
ps(5)

import travel.thailand
trip_to=travel.thailand.ThailandPackage()
trip_to.detail()

# import travel.thailand.ThailandPackage()
#이렇게 사용을 불가!(오류발생)

#from 구문은 가능!
# from travel.vietnam import VietnamPackage
# trip_to=VietnamPackage()
# trip_to.detail()

#요렇게도 가능
# from travel import vietnam
# trip_to=vietnam.VietnamPackage()
# trip_to.detail()

#__all__

#__init__.py에 all에 구문을 추가하지 않으면 아래 구문은 오류를 일으킴
from travel import*
#패키지 안에서 공개,비공개 할것을 설정 가능(__all__에 추가하면 공개 가능)
trip_to=thailand.ThailandPackage()
trip_to.detail()
trip_to=vietnam.VietnamPackage()
trip_to.detail()

#패키지,모듈 위치
import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))
#travel패키지를 라이브러리 있는곳으로 옮겨서 실행 가능!
#thailand.py 직접 실행하려면? 쉘에서 cd travel로 경로 이동 후 python thailand.py 타이핑!


print("\n\n")


#챕터 35
print("챕터 35")
#pip install
#파이썬은 이미 만들어놓은 패키지가 많기 때문에 굳이 일일이 만들 필요 없음!

#구글에 pip 들어가서 찾아보기!
#pip list:설치한 패키지들
#pip show 모듈이름:모듈 정보 보여줌
#pip install --upgrade 모듈이름
#pip uninstall 모듈이름:모듈제거

from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())
print("\n\n")

#챕터 36
print("챕터 36")

#내장함수

#input:사용자 입력을 받는 함수
language=input("무슨 언어 좋냐")
print("{0}은 아주 좋소".format(language))

#dir:어떤 객체를 넘겨줬을때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
print(dir())
import random
print(dir())#어떤걸 쓸수 있는지!
import pickle
print(dir())

print(dir(random))

print("\n\n")
lst=[1,2,3]
print(dir(lst))#append,sort 등등 리스트에서 사용할 수 있는 함수들이 표시!

print("\n\n")
name='jim'
print(dir(name))
#구글에 list of python builtins 검색
#파이썬 내에서 쓸수 있는 내장함수 검색 가능

print("\n\n")

#챕터 37
print("챕터 37")

#외장함수
#구글에 list of python modules 라고 검색하면 python module index에 들어가서 모듈 정보를 알수 있음
#사용 예제

#glob:경로 내 폴더/파일 목록 조회(윈도우 dir)

import glob
print(glob.glob("*.py"))
#확장자가 py인 모든 파일

#os:운영체제에서 제공하는 기본 기능
import os
print(os.getcwd())#현재 디렉토리

folder="sample_dir"
if os.path.exists(folder):
  print("이미 존재하는 폴더입니다")
  os.rmdir(folder)
  print(folder,"폴더를 삭제하였습니다")
else:
  os.makedirs(folder)#폴더생성
  print(folder,"폴더를 생성하였습니다")

print(os.listdir())#경로내 폴더,파일 조회

#time:시간 관련 함수
import time
print(time.localtime())
print(time.strftime("%Y-%M-%d %H:%M:%S"))

import datetime
print("오늘 날짜는",datetime.date.today())

#timedelta:두 날짜사이의 간격
today=datetime.date.today()#오늘 날짜 저장
td=datetime.timedelta(days=100)#100일 저장
print("우리가 만난지 100일은",today
+td)

print("\n\n")

#챕터 38
print("챕터 38")
print("복습 끝!")
print("\n\n")
