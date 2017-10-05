import turtle as t
t.shape("turtle")
t.pensize(2)

t.up()
t.forward(90)
t.left(110)

t.fillcolor("red")
t.begin_fill()

t.down()
t.forward(160)
t.left(140)
t.forward(300)

t.left(110)
t.forward(40)

t.left(70)
t.forward(100)

t.right(70)
t.forward(60)

t.right(70)
t.forward(100)

t.left(70)
t.forward(40)

t.left(111)
t.forward(150)
t.end_fill() # A만들기


t.fillcolor("white")
t.begin_fill()

t.up()
t.left(70)
t.forward(20)

t.down()
t.forward(65)

t.right(110)
t.forward(100)

t.right(140)
t.forward(100)

t.end_fill() # 안쪽 삼각형


t.up()
t.left(160)
t.forward(100)

t.fillcolor("red")
t.begin_fill()

t.down()
t.forward(15)
for x in range(3):
    t.right(90)
    t.forward(15)
    t.left(90)
    t.forward(15)
    t.right(90)
    t.forward(15)

t.right(90)
t.forward(15)
t.left(90)
t.forward(15)

t.end_fill() # +만들기


t.up()
t.forward(200)
t.right(90)

t.fillcolor("yellow")
t.begin_fill()

t.down()
t.forward(80)
t.left(90)
t.forward(50)
t.left(45)
t.forward(80)
t.left(90)
t.forward(30)
t.left(90)
t.forward(55)
t.right(135)
t.forward(180)
t.right(90)
t.forward(50)
t.left(90)
t.forward(30)
t.left(90)
t.forward(140)
t.left(90)
t.forward(30)
t.left(90)
t.forward(44)
t.right(90)
t.forward(180)

t.end_fill() # 1 만들기



