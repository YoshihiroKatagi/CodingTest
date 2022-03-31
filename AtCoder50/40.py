N = int(input())
x0, y0 = map(int, input().split())
xn2, yn2 = map(int, input().split())

center_x = (x0 + xn2)/2
center_y = (y0 + yn2)/2

x0-=center_x
y0-=center_y

from math import sin, cos, pi
x1 = cos(2*pi/N)*x0-sin(2*pi/N)*y0
y1 = sin(2*pi/N)*x0+cos(2*pi/N)*y0

x1 += center_x
y1 += center_y
print(x1, y1)