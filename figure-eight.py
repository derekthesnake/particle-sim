from particlesim import *
vel = .01
frac = 2
root = Tk()
canvas = Simulation(root, bg='white', width=1000, height=1000)
p = Particle(x=500, y=500, xVel=frac*vel, yVel=-.05*vel, color='blue')
p2 = Particle(x=600, y=300, xVel=-vel, color='red')
p3 = Particle(x=400, y=700, xVel=-vel, color='green')
canvas.add(p, fill='blue')
canvas.add(p2, fill='red')
canvas.add(p3, fill='green')
canvas.pack()

def update():
    for i in range(50):
        canvas.step(3)
    canvas.make_lines()
    root.after(100, update)

print(canvas.particles)

canvas.pack()
root.wm_title('Particle Simulation')
root.after(100, update)
root.mainloop()
