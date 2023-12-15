'''Write lambda functions, each to find area of square, rectangle and triangle.'''

square=lambda n:n*n
rec=lambda l,b:l*b
tri=lambda base,h:1/2*base*h

n=int(input('enter the side of square'))
print('area of square=',square(n))

l=int(input('enter the length of rectangle'))
b=int(input('enter the breadth of rectangle'))
print('area of rectangle=',rec(l,b))

base=int(input('enter the base of triangle'))
h=int(input('enter the height of triangle'))
print('area of triangle=',tri(base,h))
