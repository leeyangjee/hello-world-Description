import turtle as t
t.shape("turtle")

t.up() # 펜을 들어서 선을 없앤다.
t.speed(0) # 속도 제일 빠르게
t.forward(250) # 앞으로 250만큼 이동
t.left(90) # 반시계 방향으로 90도 회전

t.pensize(2) # 펜 굵기를 2로 조금 두껍게
t.down() # 펜을 내려 그림그릴 준비를 한다.

t.forward(250) # 앞으로 250만큼 이동

for x in range(4): # 4번 반복
    t.left(90) # 반시계 방향으로 90도 회전
    t.forward(500) #모든 변이 500인 정사각형 그리기.

t.up() # 펜을 들어 선을 없앤다.

t.goto(-100,100) # 거북이를 (-100,100)으로 좌표 이동
t.fillcolor("black") # 검은색으로 채운다.
t.begin_fill() # 색을 채우기 시작

for x in range(4): # 4번 반복
    t.fd(100) # 앞으로 100만큼 이동
    t.left(90) # 반시계 방향으로 90도 회전
t.end_fill() # 색채우기 끝

t.goto(0,0) # 거북이를 (0,0)으로 이동

import random

a = random.randint(1, 360) #각도를 1 ~ 360도까지 랜덤으로 뽑음
t.setheading(a) # 뽑은 각도를 a에 대입

# 1만큼씩 움직여서 벽에 닿을 때까지 이동

for x in range(100): # 100번 반복
    t.speed(0) # 속도는 가장 빠르게
    t.pensize(1) # 펜 굵기 1
    t.down() # 펜을 내린다.
    while True:
        t.fd(2) # 앞으로 2만큼 이동
        a = t.xcor() # a에 현재 x좌표 대입
        b = t.ycor() # b에 현재 y좌표 대입
        t.goto(a,b)

        if a <= -250: # a가 -250보다 작을 때
            break # 반복문을 빠져나옴
        if a >= 250: # a가 250보다 클 때
            break  # 반복문을 빠져나옴
        if b <= -250: # b가 -250보다 작을 때
            break # 반복문을 빠져나옴
        if b >= 250: # b가 250보다 클 때
            break # 반복문을 빠져나옴
        if -200 <= a <=-100 and 100 <= b <=200: # 장애물에 닿았을 때
            break # 반복문을 빠져나옴
        
    while True:
        if a <= -250: # a가 -250보다 작을 때
            ang = t.heading() # 현재 거북이의 각도 기억
            t.setheading(180-ang) # 반사각 구하기. 반사각: 180-현재 보고 있는각도
        if a >= 250:  # a가 250보다 클 때
            ang = t.heading() # 현재 거북이의 각도 기억
            t.setheading(180-ang) # 반사각 구하기. 반사각: 180-현재 보고 있는각도
        if -200 <= a <=-100 and 100 <= b <=200: # 장애물에 닿았을 때
            ang = t.heading() # 현재 거북이의 각도 기억
            t.setheading(180-ang) # 반사각 구하기. 반사각: 180-현재 보고 있는각도

        t.fd(2) # 앞으로 2만큼 이동
        a = t.xcor() # a에 현재 x좌표 대입
        b = t.ycor() # b에 현재 y좌표 대입
        t.goto(a,b)
        
        if a <= -250: # a가 -250보다 작을 때
            break # 반복문을 빠져나옴
        if a >= 250: # a가 250보다 클 때
            break  # 반복문을 빠져나옴
        if b <= -250: # b가 -250보다 작을 때
            break # 반복문을 빠져나옴
        if b >= 250: # b가 250보다 클 때
            break # 반복문을 빠져나옴
        if -200 <= a <=-100 and 100 <= b <=200: # 장애물에 닿았을 때
            break # 반복문을 빠져나옴
        
    while True:  
        if b <= -250: # b가 -250보다 작을 때
            ang = t.heading() # 현재 거북이의 각도 기억
            t.setheading(-ang) # 반사각 구하기. 반사각: -현재 보고 있는각도
        if b >= 250: # b가 250보다 클 때
            ang = t.heading() # 현재 거북이의 각도 기억
            t.setheading(-ang) # 반사각 구하기. 반사각: -현재 보고 있는각도
        if -200 <= a <=-100 and 100 <= b <=200: # 장애물에 닿았을 때
            ang = t.heading() # 현재 거북이의 각도 기억
            t.setheading(-ang)  # 반사각 구하기. 반사각: -현재 보고 있는각도
        
                    
        t.fd(2) # 앞으로 2만큼 이동
        a = t.xcor() # a에 현재 x좌표 대입
        b = t.ycor() # b에 현재 y좌표 대입
        t.goto(a,b) 
        
        if a <= -250: # a가 -250보다 작을 때
            break # 반복문을 빠져나옴
        if a >= 250: # a가 250보다 클 때
            break  # 반복문을 빠져나옴
        if b <= -250: # b가 -250보다 작을 때
            break # 반복문을 빠져나옴
        if b >= 250: # b가 250보다 클 때
            break # 반복문을 빠져나옴
        if -200 <= a <=-100 and 100 <= b <=200: # 장애물에 닿았을 때
            break # 반복문을 빠져나옴
            
