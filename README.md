# calculate-pi-archimedes
Quick python script to calculate Pi as Archimedes did it manually


# What is Pi?
The constant ratio between the circumference and diameter of every circle in this universe

# how did Archimedes calculate this ratio in 200 BC?
By approximation, starting with a hexagon (6 sides) within a circle

<img width="551" alt="Screenshot 2021-07-19 at 11 59 55 PM" src="https://user-images.githubusercontent.com/23168725/126232952-5aecc3c5-5ec3-434a-9218-149c1df5b5e8.png">


Assuming the hexagon having side length of 1

Circumference of hexagon = 1 * 6 = 6

Diamater of hexagon/circle = 1 * 2 = 2

Hence ratio π > 6/2 = 3. (why greater? as hexagon hasn't completely covered the whole area in the circle)

# Calculating value of SIDE for 12 side polygon within a circle

Note : The 12 sided polygon covers more area of the circumference and hence Pi gets more accurate as we keep increasing the number of sides of the polygon

We need to calculate the line segment DE to get closer to the circumference of the circle

<img width="990" alt="Screenshot 2021-08-18 at 1 56 57 AM" src="https://user-images.githubusercontent.com/23168725/129815619-24a66873-2126-42ca-8f92-101fecfcc27e.png">


Naming the FD line segment can be called as S 

Naming MN line segment as d 

Using pythagoras, we get length of d to be

<img src="https://render.githubusercontent.com/render/math?math=d=sqrt[1-(S/2)^2]">

But what we need is the length of a

which can be described as <img src="https://render.githubusercontent.com/render/math?math=a=1-d">

Finally now X can be described as <img src="https://render.githubusercontent.com/render/math?math=X=sqrt[a^2%2B(S/2)^2]">


# calculate PI ratio - 6 side

N - Number of Sides = 6

S - Length of Side = 1

d = (<img src="https://render.githubusercontent.com/render/math?math=sqrt[1-(1/2)^2]">)  =  0.87

a = <img src="https://render.githubusercontent.com/render/math?math=(1-a)"> = <img src="https://render.githubusercontent.com/render/math?math=(1-0.87)"> = 0.13 

New S (which is X basically) = <img src="https://render.githubusercontent.com/render/math?math=sqrt((0.13)^2-(1/2)^2)"> = 0.52

New length of side when polygon sides are doubled

Perimeter = 6

Diameter = <img src="https://render.githubusercontent.com/render/math?math=P/2"> = 3

# calculate PI ratio - 12 side now

N = 12

S = 0.52  (From previous calculation)

and rest values follow the same above approach

# Pythonic way to calculate PI ratio


```
import math
N = float(6)
S = float(1)

#Iterating uptil N is 96 sides 
for i in range(2,7):
    d = math.sqrt(1 - pow(S/2,2))
    a = 1 - d
    NewS = math.sqrt(pow(a,2) + pow(S/2,2))
    Perimeter = float(N * S)
    Pi = Perimeter/2
    print(Pi)
    S = NewS
    N = N*2.0
```


The results we get are as follows
```
3.0
3.10582854123
3.13262861328
3.13935020305
3.14103195089
```
