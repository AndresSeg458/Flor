from turtle import *
import colorsys

# Agregar el texto en la cabecera
header_text = "Eres la más hermosa 😍"
color("white")  # Color del texto
penup()
goto(-180, 230)  # Posición del texto
pendown()
write(header_text, align="left", font=("Times new roman", 30, "normal"))

speed(0.5)
bgcolor("black")
h = 0
# Dibujar el tallo verde del girasol
penup()
goto(0, -100)
pendown()
color("limegreen")
begin_fill()
rt(90)
fd(400)
lt(90)
fd(20)
lt(90)
fd(400)
lt(90)
fd(20)
end_fill()
# Dibujar el girasol
penup()
goto(0, 0)
pendown()
for i in range(16):
    for j in range(18):
        color("gold")  # Todos los pétalos son amarillos
        h += 0.005
        rt(90)
        circle(150 - j * 6, 90)
        lt(90)
        circle(150 - j * 6, 90)
        rt(180)
    circle(40, 24)
# Colorear el centro de marrón
penup()
goto(-20, 0)
pendown()
color("peru")
begin_fill()
circle(44)  # Ajustar el radio del centro
end_fill()
done()
