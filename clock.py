import turtle
import datetime
import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    label.after(1000, update_time)

def draw_clock(hour, minute, second):
    pen.goto(0, 210)
    pen.setheading(180)
    pen.color("white")
    pen.pensize(5)
    pen.pendown()
    pen.circle(210)
    pen.penup()
    
    pen.goto(0, 0)
    pen.setheading(90)
    angle = (hour / 12) * 360
    pen.rt(angle)
    pen.pendown()
    pen.pensize(7)
    pen.fd(80)
    pen.penup()
    
    pen.goto(0, 0)
    pen.setheading(90)
    angle = (minute / 60) * 360
    pen.rt(angle)
    pen.pendown()
    pen.pensize(5)
    pen.fd(120)
    pen.penup()
    
    pen.goto(0, 0)
    pen.color("red")
    pen.setheading(90)
    angle = (second / 60) * 360
    pen.rt(angle)
    pen.pendown()
    pen.pensize(3)
    pen.fd(150)
    pen.penup()

def update_clock():
    current_time = datetime.datetime.now()
    hour = current_time.hour % 12
    minute = current_time.minute
    second = current_time.second
    draw_clock(hour, minute, second)
    turtle.ontimer(update_clock, 1000)

window = tk.Tk()
window.title("Digital Clock")

label = tk.Label(window, font=("Arial", 80), fg="white", bg="black")
label.pack(pady=50)

pen = turtle.Turtle()
pen.shape("square")
pen.color("white")
pen.penup()
pen.speed(0)
pen.hideturtle()

update_time()
update_clock()

turtle.done()
