import math
from tkinter import *
root=Tk()
root.title("Area Calculator")
root.state('zoomed')

def circle():
    top=Toplevel()
    top.title("Circle")
    top.state('zoomed')
    Label(top,text="Chose your parameter:",font=("Comic Sans MS",16)).grid()
    def radius():
        Label(top,text="ENTER RADIUS",font=16).grid()
        e=Entry(top,width = 35, borderwidth = 5)
        e.grid()
        def f():
            r=float(e.get())
            Label(top,text="area= "+str(math.pi*r*r),font=16).grid()
        Button(top,text="Enter",font=16,command=f).grid()
    def diameter():
        Label(top,text="ENTER DIAMETER",font=16).grid()
        e=Entry(top,width = 35, borderwidth = 5)
        e.grid()
        def f():
            d=float(e.get())
            Label(top,text="area= "+str(math.pi*d*d/4),font=16).grid()
        Button(top,text="Enter",font=16,command=f).grid()
    def circum():
        Label(top,text="ENTER LENGTH OF CIRCUMFERENCE",font=16).grid()
        e=Entry(top,width = 35, borderwidth = 5)
        e.grid()
        def f():
            c=float(e.get())
            Label(top,text="area= "+str(math.pi*((c/ (2*math.pi) )**2)),font=16).grid()
        Button(top,text="Enter",font=16,command=f).grid()
    Button(top,text="Radius",font=16,command=radius).grid()
    Button(top,text="Diameter",font=16,command=diameter).grid()
    Button(top,text="Circumference",font=16,command=circum).grid()

def square():
    top=Toplevel()
    top.title("Square")
    top.state('zoomed')
    Label(top,text="Chose your parameter:",font=("Comic Sans MS",16)).grid()
    def Side():
        Label(top,text="Enter Length of side: ",font=16).grid()
        e=Entry(top,width = 35, borderwidth = 5)
        e.grid()
        def f():
            s=float(e.get())
            Label(top,text="area= "+str(s**2),font=16).grid()
        Button(top,text="Enter",font=16,command=f).grid()
    def Diagonal():
        Label(top,text="Enter Length of diagonal: ",font=16).grid()
        e=Entry(top,width = 35, borderwidth = 5)
        e.grid()
        def f():
            d=float(e.get())
            Label(top,text="area= "+str(d*d/2),font=16).grid()
        Button(top,text="Enter",font=16,command=f).grid()
    def Perimeter():
        Label(top,text="Enter Length of perimeter: ",font=16).grid()
        e=Entry(top,width = 35, borderwidth = 5)
        e.grid()
        def f():
            p=float(e.get())
            Label(top,text="area= "+str((p/4)**2),font=16).grid()
        Button(top,text="Enter",font=16,command=f).grid()
    Button(top,text="Side",font=16,command=Side).grid()
    Button(top,text="Diagonal",font=16,command=Diagonal).grid()
    Button(top,text="Perimeter",font=16,command=Perimeter).grid()

def rectangle():
    top=Toplevel()
    top.title("Rectangle")
    top.state('zoomed')
    Label(top,text="Chose your parameter:",font=("Comic Sans MS",16)).grid()
    def Side():
        Label(top,text="Enter Length of sides: ",font=16).grid()
        e1=Entry(top,width = 35, borderwidth = 5)
        e1.grid()
        e2=Entry(top,width = 35, borderwidth = 5)
        e2.grid()
        def f():
            s1=float(e1.get())
            s2=float(e2.get())
            Label(top,text="area= "+str(s1*s2),font=16).grid()
        Button(top,text="Enter",font=16,command=f).grid()
    def Diagonal():
        Label(top,text="Enter Length of diagonal: ",font=16).grid()
        e1=Entry(top,width = 35, borderwidth = 5)
        e1.grid()
        Label(top,text="Enter length of any side ",font=16).grid()
        e2=Entry(top,width = 35, borderwidth = 5)
        e2.grid()
        def f():
            d=float(e1.get())
            s=float(e2.get())
            Label(top,text="area= "+str(s*(math.sqrt((d**2)-(s**2)))),font=16).grid()
        Button(top,text="Enter",font=16,command=f).grid()
    def Perimeter():
        Label(top,text="Enter Length of perimeter: ",font=16).grid()
        e1=Entry(top,width = 35, borderwidth = 5)
        e1.grid()
        Label(top,text="Enter length of any side: ",font=16).grid()
        e2=Entry(top,width = 35, borderwidth = 5)
        e2.grid()
        def f():
            p=float(e1.get())
            s=float(e2.get())
            Label(top,text="area= "+str((p*s/2)-(s**2)),font=16).grid()
        Button(top,text="Enter",font=16,command=f).grid()
    Button(top,text="Side",font=16,command=Side).grid()
    Button(top,text="Diagonal",font=16,command=Diagonal).grid()
    Button(top,text="Perimeter",font=16,command=Perimeter).grid()

def triangle():
    top=Toplevel()
    top.title("Triangle")
    top.state('zoomed')
    Label(top,text="Chose your parameter:",font=("Comic Sans MS",16)).grid()
    def base_and_height():
        Label(top,text="ENTER BASE:",font=16).grid()
        e1=Entry(top,width = 35, borderwidth = 5)
        e1.grid()
        Label(top,text="ENTER HEIGHT:",font=16).grid()
        e2=Entry(top,width = 35, borderwidth = 5)
        e2.grid()
        
        def f():
            b=float(e1.get())
            h=float(e2.get())
            Label(top,text="area= "+str(0.5*b*h),font=16).grid()
        Button(top,text="Enter",font=16,command=f).grid()
    def three_sides():
        Label(top,text="ENTER THE FIRST SIDE:",font=16).grid()
        e1=Entry(top,width = 35, borderwidth = 5)
        e1.grid()
        Label(top,text="ENTER THE SECOND SIDE:",font=16).grid()
        e2=Entry(top,width = 35, borderwidth = 5)
        e2.grid()
        Label(top,text="ENTER THE THIRD SDIE:",font=16).grid()
        e3=Entry(top,width = 35, borderwidth = 5)
        e3.grid()
        def f():
            a=float(e1.get())
            b=float(e2.get())
            c=float(e3.get())
            s=(a+b+c)/2
            Label(top,text="area= "+str(math.sqrt(s*(s-a)*(s-b)*(s-c))),font=16).grid()
        Button(top,text="Enter",font=16,command=f).grid()
    def side_and_angle():
        Label(top,text="ENTER FIRST SIDE:",font=16).grid()
        e1=Entry(top,width = 35, borderwidth = 5)
        e1.grid()
        Label(top,text="ENTER SECOND SIDE:",font=16).grid()
        e2=Entry(top,width = 35, borderwidth = 5)
        e2.grid()
        Label(top,text="ENTER ANGLE B/W THE SIDES:",font=16).grid()
        e3=Entry(top,width = 35, borderwidth = 5)
        e3.grid()
        def f():
            a=float(e1.get())
            b=float(e2.get())
            c=float(e3.get())
            Label(top,text="area= "+str( abs(0.5*a*b*(math.sin(c*math.pi/180)))),font=16).grid()
        Button(top,text="Enter",font=16,command=f).grid()
    Button(top,text="Base And Height",font=16,command=base_and_height).grid()
    Button(top,text="Three Sides",font=16,command=three_sides).grid()
    Button(top,text="2 Sides And Angle b/w Them",font=16,command=side_and_angle).grid()

def trapezium():
    top=Toplevel()
    top.title("Trapezium")
    top.state('zoomed')
    Label(top,text="enter the following details",font=("Comic Sans MS",16)).grid()
    def parallel():
        Label(top,text="Enter Length of first parallel side: ",font=16).grid()
        e1=Entry(top,width = 35, borderwidth = 5)
        e1.grid()
        Label(top,text="Enter Length of second parallel side: ",font=16).grid()
        e2=Entry(top,width = 35, borderwidth = 5)
        e2.grid()
        Label(top,text="Enter distance b/w parallel sides: ",font=16).grid()
        e3=Entry(top,width = 35, borderwidth = 5)
        e3.grid()
        def f():
            a=float(e1.get())
            b=float(e2.get())
            c=float(e3.get())
            Label(top,text="area= "+str(0.5*(a+b)*c),font=16).grid()
        Button(top,text="Enter",font=16,command=f).grid()

    Button(top,text="Side And Parallel Sides",font=16,command=parallel).grid()

def rhombus():
    top=Toplevel()
    top.title("Rhombus")
    top.state('zoomed')
    Label(top,text="Chose your parameter:",font=("Comic Sans MS",16)).grid()
    def base_and_height():
        Label(top,text="ENTER BASE:",font=16).grid()
        e1=Entry(top,width = 35, borderwidth = 5)
        e1.grid()
        Label(top,text="ENTER HEIGHT:",font=16).grid()
        e2=Entry(top,width = 35, borderwidth = 5)
        e2.grid()
        def f():
            s1=float(e1.get())
            s2=float(e2.get())
            Label(top,text="area= "+str(s1*s2),font=16).grid()
        Button(top,text="Enter",font=16,command=f).grid()
    def Diagonal():
        Label(top,text="Enter Length of diagonal 1: ",font=16).grid()
        e1=Entry(top,width = 35, borderwidth = 5)
        e1.grid()
        Label(top,text="Enter length of diagonal 2: ",font=16).grid()
        e2=Entry(top,width = 35, borderwidth = 5)
        e2.grid()
        def f():
            d=float(e1.get())
            s=float(e2.get())
            Label(top,text="area= "+str(0.5*d*s),font=16).grid()
        Button(top,text="Enter",font=16,command=f).grid()
    def side_interior_angle():
        Label(top,text="Enter Length of one side: ",font=16).grid()
        e1=Entry(top,width = 35, borderwidth = 5)
        e1.grid()
        Label(top,text="Enter one interior angle: ",font=16).grid()
        e2=Entry(top,width = 35, borderwidth = 5)
        e2.grid()
        def f():
            p=float(e1.get())
            s=float(e2.get())
            Label(top,text="area= "+str( abs(p*p*math.sin(s*math.pi/180))),font=16).grid()
        Button(top,text="Enter",font=16,command=f).grid()
    Button(top,text="Base and Height",font=16,command=base_and_height).grid()
    Button(top,text="Diagonals",font=16,command=Diagonal).grid()
    Button(top,text="One Side and One Interior Angle",font=16,command=side_interior_angle).grid()
    
def kite():
    top=Toplevel()
    top.title("Kite")
    top.state('zoomed')
    Label(top,text="Chose your parameter:",font=("Comic Sans MS",16)).grid()
    def diagonal():
        Label(top,text="ENTER FIRST DIAGONAL:",font=16).grid()
        e1=Entry(top,width = 35, borderwidth = 5)
        e1.grid()
        Label(top,text="ENTER SECOND DIAGONAL:",font=16).grid()
        e2=Entry(top,width = 35, borderwidth = 5)
        e2.grid()
        def f():
            s1=float(e1.get())
            s2=float(e2.get())
            Label(top,text="area= "+str((s1*s2)/2),font=16).grid()
        Button(top,text="Enter",font=16,command=f).grid()
    def side_angle():
        Label(top,text="Enter Length of side 1: ",font=16).grid()
        e1=Entry(top,width = 35, borderwidth = 5)
        e1.grid()
        Label(top,text="Enter length of side 2: ",font=16).grid()
        e2=Entry(top,width = 35, borderwidth = 5)
        e2.grid()
        Label(top,text="Enter angle b/w two given sides: ",font=16).grid()
        e3=Entry(top,width = 35, borderwidth = 5)
        e3.grid()
        def f():
            a=float(e1.get())
            b=float(e2.get())
            c=float(e3.get())
            Label(top,text="area= "+str( abs(a*b*math.sin(c*math.pi/180))),font=16).grid()
        Button(top,text="Enter",font=16,command=f).grid()
    
    Button(top,text="Diagonals",font=16,command=diagonal).grid()
    Button(top,text="2 Sides and Angle b/w them",font=16,command=side_angle).grid()
    
def pyramid():
    top=Toplevel()
    top.title("Pyramid")
    top.state('zoomed')
    Label(top,text="enter the following details",font=("Comic Sans MS",16)).grid()
    def side():
        Label(top,text="Enter Length of side:",font=16).grid()
        e1=Entry(top,width = 35, borderwidth = 5)
        e1.grid()
        Label(top,text="Enter Length of slant height: ",font=16).grid()
        e2=Entry(top,width = 35, borderwidth = 5)
        e2.grid()
        
        def f():
            a=float(e1.get())
            b=float(e2.get())
                
            Label(top,text="area= "+str((2*a*b)+(b*b)),font=16).grid()
        Button(top,text="Enter",font=16,command=f).grid()

    Button(top,text="Side And Slant Height",font=16,command=side).grid()

def ellipse():
    top=Toplevel()
    top.title("Ellipse")
    top.state('zoomed')
    Label(top,text="Choose your parameter : ",font=("Comic Sans MS",16)).grid()
    def semimajor_semiminor():
        Label(top,text="ENTER LENGTH OF SEMI MAJOR AXIS :",font=16).grid()
        e1=Entry(top,width = 35, borderwidth = 5)
        e1.grid()
        Label(top,text="ENTER LENGTH OF SEMI MINOR AXIS :",font=16).grid()
        e2=Entry(top,width = 35, borderwidth = 5)
        e2.grid()
        def f():
            a=float(e1.get())
            b=float(e2.get())
            Label(top,text="Area = "+str(math.pi*a*b),font=16).grid()
        Button(top,text="Enter",font=16,command=f).grid()
    def semimajor_eccentricity():
        Label(top,text="ENTER LENGTH OF SEMI MAJOR AXIS :",font=16).grid()
        e1=Entry(top,width = 35, borderwidth = 5)
        e1.grid()
        Label(top,text="ENTER ECCENTRICITY OF ELLIPSE :",font=16).grid()
        e2=Entry(top,width = 35, borderwidth = 5)
        e2.grid()

        def f():
            a=float(e1.get())
            e=float(e2.get())
            Label(top,text="Area = "+str(math.pi*a*math.sqrt((a**2)*(1-e**2))),font=16).grid()
        Button(top,text="Enter",font=16,command=f).grid()
    def semiminor_eccentricity():
        Label(top,text="ENTER LENGTH OF SEMI MINOR AXIS :",font=16).grid()
        e1=Entry(top,width = 35, borderwidth = 5)
        e1.grid()
        Label(top,text="ENTER ECCENTRICITY OF ELLIPSE :",font=16).grid()
        e2=Entry(top,width = 35, borderwidth = 5)
        e2.grid()

        def f():
            b=float(e1.get())
            e=float(e2.get())
            Label(top,text="Area = "+str((math.pi*b**2)/(math.sqrt(1-e**2))),font=16).grid()
        Button(top,text="Enter",font=16,command=f).grid()

    Button(top,text="Semimajor & Semiminor",font=16,command=semimajor_semiminor).grid()
    Button(top,text="Semimajor & Eccentricity",font=16,command=semimajor_eccentricity).grid()
    Button(top,text="Semiminor & Eccentricity",font=16,command=semiminor_eccentricity).grid()

def cube():
    top=Toplevel()
    top.title("Cube")
    top.state('zoomed')
    Label(top,text="Choose your parameter:",font=("Comic Sans MS",16)).grid()
    def sidelength():
        Label(top,text="ENTER SIDE LENGTH :",font=16).grid()
        e1=Entry(top,width = 35, borderwidth = 5)
        e1.grid()
        
        def f():
            a=float(e1.get())
            Label(top,text="Surface Area = "+str(6*a**2),font=16).grid()
        Button(top,text="Enter",font=16,command=f).grid()
    def volume():
        Label(top,text="ENTER THE VOLUME OF THE CUBE :",font=16).grid()
        e1=Entry(top,width = 35, borderwidth = 5)
        e1.grid()
        
        def f():
            v=float(e1.get())
            Label(top,text="Surface Area = "+str(6*v**(2/3)),font=16).grid()
        Button(top,text="Enter",font=16,command=f).grid()
    def facediagonal():
        Label(top,text="ENTER LENGTH OF FACE DIAGONAL :",font=16).grid()
        e1=Entry(top,width = 35, borderwidth = 5)
        e1.grid()

        def f():
            f=float(e1.get())
            Label(top,text="Surface Area = "+str(3*f**2),font=16).grid()
        Button(top,text="Enter",font=16,command=f).grid()
    def bodydiagonal():
        Label(top,text="ENTER LENGTH OF BODY DIAGONAL :",font=16).grid()
        e1=Entry(top,width = 35, borderwidth = 5)
        e1.grid()
        
        def f():
            b=float(e1.get())
            Label(top,text="Surface Area = "+str(2*b**2),font=16).grid()
        Button(top,text="Enter",font=16,command=f).grid()

    Button(top,text="Side length",font=16,command=sidelength).grid()
    Button(top,text="Volume",font=16,command=volume).grid()
    Button(top,text="Face diagonal",font=16,command=facediagonal).grid()
    Button(top,text="Body diagonal",font=16,command=bodydiagonal).grid()

def cuboid():
    top=Toplevel()
    top.title("Cuboid")
    top.state('zoomed')
    Label(top,text="Choose your parameter:",font=("Comic Sans MS",16)).grid()
    def length_breadth_height():
        Label(top,text="ENTER THE LENGTH :",font=16).grid()
        e1=Entry(top,width = 35, borderwidth = 5)
        e1.grid()
        Label(top,text="ENTER THE BREADTH :",font=16).grid()
        e2=Entry(top,width = 35, borderwidth = 5)
        e2.grid()
        Label(top,text="ENTER THE HEIGHT :",font=16).grid()
        e3=Entry(top,width = 35, borderwidth = 5)
        e3.grid()

        def f():
            l=float(e1.get())
            b=float(e2.get())
            h=float(e3.get())
            Label(top,text="Surface Area = "+str(2*(l*b+b*h+h*l)),font=16).grid()
        Button(top,text="Enter",font=16,command=f).grid()
    def volume_length_breadth():
        Label(top,text="ENTER THE VOLUME OF THE CUBOID :",font=16).grid()
        e1=Entry(top,width = 35, borderwidth = 5)
        e1.grid()
        Label(top,text="ENTER THE LENGTH :",font=16).grid()
        e2=Entry(top,width = 35, borderwidth = 5)
        e2.grid()
        Label(top,text="ENTER THE BREADTH :",font=16).grid()
        e3=Entry(top,width = 35, borderwidth = 5)
        e3.grid()

        def f():
            v=float(e1.get())
            l=float(e2.get())
            b=float(e3.get())
            Label(top,text="Surface Area = "+str(2*(l*b+(v/l)+(v/b))),font=16).grid()
        Button(top,text="Enter",font=16,command=f).grid()
    def volume_length_height():
        Label(top,text="ENTER THE VOLUME OF THE CUBOID :",font=16).grid()
        e1=Entry(top,width = 35, borderwidth = 5)
        e1.grid()
        Label(top,text="ENTER THE LENGTH :",font=16).grid()
        e2=Entry(top,width = 35, borderwidth = 5)
        e2.grid()
        Label(top,text="ENTER THE HEIGHT :",font=16).grid()
        e3=Entry(top,width = 35, borderwidth = 5)
        e3.grid()

        def f():
            v=float(e1.get())
            l=float(e2.get())
            h=float(e3.get())
            Label(top,text="Surface Area = "+str(2*(l*h+(v/l)+(v/h))),font=16).grid()
        Button(top,text="Enter",font=16,command=f).grid()
    def volume_breadth_height():
        Label(top,text="ENTER THE VOLUME OF THE CUBOID :",font=16).grid()
        e1=Entry(top,width = 35, borderwidth = 5)
        e1.grid()
        Label(top,text="ENTER THE BREADTH :",font=16).grid()
        e2=Entry(top,width = 35, borderwidth = 5)
        e2.grid()
        Label(top,text="ENTER THE HEIGHT :",font=16).grid()
        e3=Entry(top,width = 35, borderwidth = 5)
        e3.grid()

        def f():
            v=float(e1.get())
            b=float(e2.get())
            h=float(e3.get())
            Label(top,text="Surface Area = "+str(2*(b*h+(v/b)+(v/h))),font=16).grid()
        Button(top,text="Enter",font=16,command=f).grid()

    Button(top,text="Length,Breadth & Height",font=16,command=length_breadth_height).grid()
    Button(top,text="Volume,Length & Breadth",font=16,command=volume_length_breadth).grid()
    Button(top,text="Volume,Length & Height",font=16,command=volume_length_height).grid()
    Button(top,text="Volume,Breadth & Height",font=16,command=volume_breadth_height).grid()

def sector():
    top=Toplevel()
    top.title("Sector")
    top.state('zoomed')
    Label(top,text="Choose your parameter:",font=("Comic Sans MS",16)).grid()
    def radius_angle():
        Label(top,text="ENTER THE RADIUS :",font=16).grid()
        e1=Entry(top,width = 35, borderwidth = 5)
        e1.grid()
        Label(top,text="ENTER THE ANGLE SUBTENDED IN DEGREES :",font=16).grid()
        e2=Entry(top,width = 35, borderwidth = 5)
        e2.grid()

        def f():
            r=float(e1.get())
            t=float(e2.get())
            Label(top,text="Area of sector = "+str((t/360)*math.pi*r**2),font=16).grid()
        Button(top,text="Enter",font=16,command=f).grid()

    Button(top,text="Radius & Angle",font=16,command=radius_angle).grid()

def cone():
    top=Toplevel()
    top.title("Cone")
    top.state('zoomed')
    Label(top,text="Choose your parameter:",font=("Comic Sans MS",16)).grid()
    def radius_and_height():
        Label(top,text="ENTER RADIUS:",font=16).grid()
        e1=Entry(top,width = 35, borderwidth = 5)
        e1.grid()
        Label(top,text="ENTER HEIGHT:",font=16).grid()
        e2=Entry(top,width = 35, borderwidth = 5)
        e2.grid()
        
        def f():
            r=float(e1.get())
            h=float(e2.get())
            Label(top,text="area= "+str((math.pi*r**2)+(math.pi*r*math.sqrt(h**2+r**2))),font=16).grid()
        Button(top,text="Enter",font=16,command=f).grid()
    def d_h():
        Label(top,text="ENTER THE DIAMETER:",font=16).grid()
        e1=Entry(top,width = 35, borderwidth = 5)
        e1.grid()
        Label(top,text="ENTER THE HEIGHT:",font=16).grid()
        e2=Entry(top,width = 35, borderwidth = 5)
        e2.grid()
        
        def f():
            d=float(e1.get())
            h=float(e2.get())           
            Label(top,text="area= "+str((math.pi*d**2/4)+(math.pi*d*math.sqrt(4*h**2+d**2)/4)),font=16).grid()
        Button(top,text="Enter",font=16,command=f).grid()
    def r_l():
        Label(top,text="ENTER RADIUS:",font=16).grid()
        e1=Entry(top,width = 35, borderwidth = 5)
        e1.grid()
        Label(top,text="ENTER SLANT HEIGHT:",font=16).grid()
        e2=Entry(top,width = 35, borderwidth = 5)
        e2.grid()
        
        def f():
            r=float(e1.get())
            l=float(e2.get())            
            Label(top,text="area= "+str((math.pi*r**2)+(math.pi*r*l)),font=16).grid()
        Button(top,text="Enter",font=16,command=f).grid()
    def d_l():
        Label(top,text="ENTER THE DIAMETER:",font=16).grid()
        e1=Entry(top,width = 35, borderwidth = 5)
        e1.grid()
        Label(top,text="ENTER THE SLANT HEIGHT:",font=16).grid()
        e2=Entry(top,width = 35, borderwidth = 5)
        e2.grid()
        def f():
            d=float(e1.get())
            l=float(e2.get())            
            Label(top,text="area= "+str((math.pi*d**2/4)+(math.pi*d*math.sqrt(4*(l**2-d**2/4)+d**2)/4)),font=16).grid()
        Button(top,text="Enter",font=16,command=f).grid()
    Button(top,text="Radius and Height",font=16,command=radius_and_height).grid()
    Button(top,text="Diameter and Height",font=16,command=d_h).grid()
    Button(top,text="Radius and Slant Height",font=16,command=r_l).grid()
    Button(top,text="Diameter and Slant Height",font=16,command=d_l).grid()




def sphere():
    top=Toplevel()
    top.title("Sphere")
    top.state('zoomed')
    Label(top,text="enter the following details",font=("Comic Sans MS",16)).grid()
    def radius():
        Label(top,text="Enter Radius of the sphere: ",font=16).grid()
        e1=Entry(top,width = 35, borderwidth = 5)
        e1.grid()
        
        def f():
            r=float(e1.get())            
            Label(top,text="area= "+str(4*math.pi*r**2),font=16).grid()
        Button(top,text="Enter",font=16,command=f).grid()
    Button(top,text="Radius",font=16,command=radius).grid()
    def diameter():
        Label(top,text="Enter Diameter of the sphere: ",font=16).grid()
        e1=Entry(top,width = 35, borderwidth = 5)
        e1.grid()
        
        def f():
            d=float(e1.get())            
            Label(top,text="area= "+str(math.pi*d**2),font=16).grid()
        Button(top,text="Enter",font=16,command=f).grid()
    Button(top,text="Diameter",font=16,command=diameter).grid()

def hemisphere():
    top=Toplevel()
    top.title(" HemiSphere")
    top.state('zoomed')
    Label(top,text="Choose your Parameter",font=("Comic Sans MS",16)).grid()
    def radius1():
        Label(top,text="Enter Radius of the hemisphere: ",font=16).grid()
        e1=Entry(top,width = 35, borderwidth = 5)
        e1.grid()
        
        def f():
            r=float(e1.get())            
            Label(top,text="area= "+str(3*math.pi*r**2),font=16).grid()
        Button(top,text="Enter",font=16,command=f).grid()
    Button(top,text="Radius",font=16,command=radius1).grid()
    def diameter1():
        Label(top,text="Enter Diameter of the Hemisphere: ",font=16).grid()
        e1=Entry(top,width = 35, borderwidth = 5)
        e1.grid()
        
        def f():
            d=float(e1.get())            
            Label(top,text="area= "+str((3*math.pi*d**2)/2),font=16).grid()
        Button(top,text="Enter",font=16,command=f).grid()
    Button(top,text="Diameter",font=16,command=diameter1).grid()
    
    
    
    
def parallelogram():
    top=Toplevel()
    top.title("Parallelogram")
    top.state('zoomed')
    Label(top,text="Chose your parameter:",font=("Comic Sans MS",16)).grid()
    def b_h():
        Label(top,text="ENTER BASE :",font=16).grid()
        e1=Entry(top,width = 35, borderwidth = 5)
        e1.grid()
        Label(top,text="ENTER HEIGHT :",font=16).grid()
        e2=Entry(top,width = 35, borderwidth = 5)
        e2.grid()
        def f():
            b=float(e1.get())
            h=float(e2.get())
            Label(top,text="area= "+str(b*h),font=16).grid()
        Button(top,text="Enter",font=16,command=f).grid()
    def side_angle():
        Label(top,text="Enter Length of side 1: ",font=16).grid()
        e1=Entry(top,width = 35, borderwidth = 5)
        e1.grid()
        Label(top,text="Enter length of side 2: ",font=16).grid()
        e2=Entry(top,width = 35, borderwidth = 5)
        e2.grid()
        Label(top,text="Enter angle b/w two given sides: ",font=16).grid()
        e3=Entry(top,width = 35, borderwidth = 5)
        e3.grid()
        def f():
            l1=float(e1.get())
            l2=float(e2.get())
            x=float(e3.get())
            Label(top,text="area= "+str(l1*l2*math.sin(x*math.pi/180)),font=16).grid()
        Button(top,text="Enter",font=16,command=f).grid()
    def diagnol_angle():
        Label(top,text="Enter Length of diagnol 1: ",font=16).grid()
        e1=Entry(top,width = 35, borderwidth = 5)
        e1.grid()
        Label(top,text="Enter length of diagnol 2: ",font=16).grid()
        e2=Entry(top,width = 35, borderwidth = 5)
        e2.grid()
        Label(top,text="Enter angle b/w two given diagnol: ",font=16).grid()
        e3=Entry(top,width = 35, borderwidth = 5)
        e3.grid()
        def f():
            d1=float(e1.get())
            d2=float(e2.get())
            x=float(e3.get())
            Label(top,text="area= "+str(d1*d2*math.sin(x*math.pi/180)/2),font=16).grid()
        Button(top,text="Enter",font=16,command=f).grid()
    
    Button(top,text="Base and Height",font=16,command=b_h).grid()
    Button(top,text="2 Sides and Angle b/w them",font=16,command=side_angle).grid()
    Button(top,text="2 diagnols and angle between them",font=16,command=diagnol_angle).grid()
    


Label(root,text="Welcome to Area Calculator",fg="purple",font=("Algerian",20)).grid(row=0,column=10)
Label(root,text="Choose your Shape: ",font=("Comic Sans MS",16)).grid(row=1,column=0)

Label(root,text="\U0001F449" ).grid(row=2,column=0)
Button(root,text="Circle" ,command=circle).grid(row=2,column=1)

Label(root,text="\U0001F449" ).grid(row=3,column=0)
Button(root,text="Square" ,command=square).grid(row=3,column=1)

Label(root,text="\U0001F449" ).grid(row=4,column=0)
Button(root,text="Rectangle" ,command=rectangle).grid(row=4,column=1)

Label(root,text="\U0001F449" ).grid(row=5,column=0)
Button(root,text="Triangle" ,command=triangle).grid(row=5,column=1)

Label(root,text="\U0001F449" ).grid(row=6,column=0)
Button(root,text="Trapezium" ,command=trapezium).grid(row=6,column=1)

Label(root,text="\U0001F449" ).grid(row=7,column=0)
Button(root,text="Rhombus" ,command=rhombus).grid(row=7,column=1)

Label(root,text="\U0001F449" ).grid(row=8,column=0)
Button(root,text="Kite" ,command=kite).grid(row=8,column=1)

Label(root,text="\U0001F449" ).grid(row=9,column=0)
Button(root,text="Pyramid" ,command=pyramid).grid(row=9,column=1)

Label(root,text="\U0001F449" ).grid(row=10,column=0)
Button(root,text="Ellipse" ,command=ellipse).grid(row=10,column=1)

Label(root,text="\U0001F449" ).grid(row=11,column=0)
Button(root,text="Cube" ,command=cube).grid(row=11,column=1)

Label(root,text="\U0001F449" ).grid(row=12,column=0)
Button(root,text="Cuboid" ,command=cuboid).grid(row=12,column=1)

Label(root,text="\U0001F449" ).grid(row=13,column=0)
Button(root,text="Sector" ,command=sector).grid(row=13,column=1)

Label(root,text="\U0001F449" ).grid(row=14,column=0)
Button(root,text="Cone" ,command=cone).grid(row=14,column=1)

Label(root,text="\U0001F449" ).grid(row=15,column=0)
Button(root,text="Sphere" ,command=sphere).grid(row=15,column=1)

Label(root,text="\U0001F449" ).grid(row=16,column=0)
Button(root,text="HemiSphere" ,command=hemisphere).grid(row=16,column=1)

Label(root,text="\U0001F449" ).grid(row=17,column=0)
Button(root,text="Parallelogram" ,command=parallelogram).grid(row=17,column=1)

mainloop()

















