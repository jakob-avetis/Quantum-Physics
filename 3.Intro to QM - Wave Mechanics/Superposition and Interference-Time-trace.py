# initialize variables
c = 0.5
l= 10
x = np.linspace(0,l,100)
t = np.arange(0,30,0.1)
y = np.zeros((len(x), len(t)))
# for loop over time
for i in range(len(t)):
    for j in range(len(x)):
        y[j,i] = wave_solution(x[j],t[i],c,1,l) + wave_solution(x[j],t[i],c,2,l)

# time-plot
qw.time_plot(x,y,t,t_step=5)
plt.show()