import turtle
import tkinter

self = turtle.Screen()
self.title("The Wheel of Time")
self.setup(900, 700)
self.bgcolor("black")

# Intro statements
pen = turtle.Turtle()
pen.speed(2)
pen.color("teal")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Welcome to the 'Wheel of Time' Adventure Game", align="center", font=("Helvetica", 24, "normal"))

# 
pen1 = turtle.Turtle()
pen1.speed(0)
pen1.color("gold")
pen1.penup()
pen1.hideturtle()
pen1.goto(0, 400)
pen1.write("Do you want to play?", align="center", font=("Helvetica", 24, "normal"))


def clear():
    pen.clear

self.onkeypress(clear, "enter")
