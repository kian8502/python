#-*- coding:utf-8 -*-
import os
import sys
import io
import turtleDef as td
#import traderecord as tr

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'euc-kr')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'euc-kr')

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
savePath="D:/Documents/Python/turtle/code/"
#savePath="C:/Users/animo/OneDrive/문서/python/turtle/code/"
=======
savePath="C:/Users/animo/OneDrive/문서/python/turtle/code/"
>>>>>>> remotes/origin/master
=======

savePath="D:/Documents/Python/turtle/code/"
#savePath="C:/Users/animo/OneDrive/문서/python/turtle/code/"
>>>>>>> eaf139570a9f9e57dedab0d085684f995218c975
=======

#savePath="D:/Documents/Python/turtle/code/"
savePath="C:/Users/animo/OneDrive/문서/python/turtle/code/"
>>>>>>> 3aee10c6d3b1182383311b0ef25921df9266e45e

try:
    if not(os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("Failed to create directory!!!!!")
        raise

stockName=td.stockName()
<<<<<<< HEAD
account=1200000
N=float(input("N: "))
riskPer=0.01
now=td.date(input("오늘자 입력 1 or else :"))
#기초정보
def info(stockName):
    with open(savePath+"%s.txt"% stockName, 'a', encoding="utf-8") as f:
        enterP=td.firstPoint() #첫진입 포인트
        pramiding=float(input("피라미딩 포인트 0.5 or 1 : "))
        f.write("입력일 : "+str(now)+"\n")
        #f.write("%s회차"% i+"\n")
        f.write("진입포인트 : "+str(enterP)+"\n")
        f.write("ATR : "+str(N)+"\n")
        f.write("\n")
        Limit=td.accountLimit(account,riskPer) #한도
        f.write("손실한도 : "+str(Limit)+"\n")
        amount=(td.contractAmount(Limit,N)) #거래량
        f.write("거래량 : "+str(amount)+"\n") 
        f.write("구매금액 : "+str(td.price(enterP,amount))+"\n")
        f.write("Pramiding포인트 : "+str(td.nextPoint(enterP,N,pramiding))+"\n") #추가포인트
        f.write("Drop포인트 : "+str(td.stopPoint(enterP,N))+"\n") #정지포인트
        f.write("\n")
#포인트 추적
def tradePoint(stockName):
    with open(savePath+"%s.txt"% stockName, 'a', encoding="utf-8") as f:
        lastP=float(input("직전 Drop포인트 : "))
        trail=td.trailPoint(lastP,N)
        f.write("Trail포인트 : "+str(trail)+"\n") #트레일포인트        
        f.write("\n")

#turtle(stockName)
call = input("1 = all, 2 = trail ")
if call == "1":
    info(stockName)
if call == "2":
    tradePoint(stockName)

=======
#Limit=td.accountLimit(account,td.riskLimit)

def turtle(stockName):
    i=1
    #반복횟수
    #j=int(input("반복횟수: "))
    j=1
    while i <= j:
        account=td.entireaccount() #보유계정금
        #print("%s회차"% i)
        enterP=td.firstPoint() #첫진입 포인트
        N=float(input("N: "))
        riskPer=0.01
        with open(savePath+"%s.txt"% stockName, 'a', encoding="utf-8") as f:
            now=td.date(input("오늘자 입력 1 or else :"))
            #riskPer=float(input("리스크 비율 : "))
            pramiding=float(input("피라미딩 포인트 0.5 or 1 : "))
            f.write("입력일 : "+str(now)+"\n")
            #f.write("%s회차"% i+"\n")
            f.write("진입포인트 : "+str(enterP)+"\n")
            f.write("ATR : "+str(N)+"\n")
            f.write("\n")
            nextP=td.nextPoint(enterP,N,pramiding)
            f.write("정지포인트 : "+str(td.stopPoint(enterP,N,pramiding))+"\n") #정지포인트
            f.write("다음포인트 : "+str(nextP)+"\n")
            f.write("\n")
            Limit=td.accountLimit(account,riskPer) #한도
            f.write("손실한도 : "+str(Limit)+"\n")
            amount=(td.contractAmount(Limit,N)) #거래량
            f.write("거래량 : "+str(amount)+"\n") 
            #f.write("계정금액 : "+str(td.changeAccount(account,N,i))+"\n") #계정금액
            f.write("구매금액 : "+str(td.price(enterP,amount))+"\n")
            f.write("\n")
        i+=1

turtle(stockName)
>>>>>>> 3aee10c6d3b1182383311b0ef25921df9266e45e
""" call = input("1 = turtle, 2 = record : ")

if call == "1":
    turtle(stockName)
if call == "2":
    record(stockName)
 """