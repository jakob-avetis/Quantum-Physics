# define your function
def wave_solution(x,t,c,n,l):
    solution = harmonic_time_dependent(t,c,n,l)*harmonic_time_independent(x,n,l)
    return solution
# initialize variables
t = np.arange(0, 100, 0.1)
l = 10
c = 0.5
x = l/3
# sum both waves
wave = wave_solution(x,t,c,1,l) + wave_solution(x,t,c,2,l)
# plot
plt.plot(t, wave)
plt.show()