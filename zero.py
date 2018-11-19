from particlesim import *
root = Tk()
canvas = Simulation(root, bg='white', width=1000, height=1000)
p = Particle(x=500, y=250, xVel=.04, color='black')
p2 = Particle(x=500, y=400, size=20, color='white', stationary=True)
p3 = Particle(x=500, y=600, size=20, color='white', stationary=True)
canvas.add(p, fill='black')
canvas.add(p2, fill='white')
canvas.add(p3, fill='white')
canvas.pack()

def update():
    for i in range(30):
        canvas.step(3)
    canvas.make_lines()
    root.after(100, update)

print(canvas.particles)

canvas.pack()
root.wm_title('Particle Simulation')
root.after(100, update)
root.mainloop()
