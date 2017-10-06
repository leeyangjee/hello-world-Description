import turtle as t
t.shape("turtle")

t.bgcolor("black")
t.speed(0) # 속도 빠르게

t.up()
t.left(180)
t.forward(340)
t.right(90)
t.forward(280)
t.right(90)
t.down() # 상단으로 이동

for x in range(15): # 15번 반복
    for x in range(6):
        if x % 7 == 0:
            t.color("red")
        if x % 7 == 1:
            t.color("orange")
        if x % 7 == 2:
            t.color("yellow")
        if x % 7 == 3:
            t.color("green")
        if x % 7 == 4:
            t.color("skyblue")
        if x % 7 == 5:
            t.color("blue")
        if x % 7 == 6:
            t.color("purple") # 7의 배수로 색 바꾸기
        t.forward(50)
        t.right(90)
        t.forward(50)
        t.right(90)
        t.forward(50)
        t.left(90)
        t.forward(50)
        t.left(90) # 네모만들기
    
    t.up()
    t.forward(50)
    t.left(90)
    t.forward(600)
    t.right(90)
    t.down() # 처음 상단으로 이동


