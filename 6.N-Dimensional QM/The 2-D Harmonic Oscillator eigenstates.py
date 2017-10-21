# intialize variables
l=1
m=2
#exercise
x = np.linspace(-4,4,50)
y = np.linspace(-4,4,50)
xx, yy = np.meshgrid(x,y)
# evaluate function
ho = qw.harmonic_oscillator_2D(xx,yy,l,m)
#plot
qw.plot_contours(xx, yy, ho)    
plt.title('l='+str(l)+', y='+str(m))   
plt.show()
plt.clf()
# pick a random item from list and plot
import random
l_new, m_new = random.choice([(0,0),(0,1),(1,0),(0,2),(2,0),(1,1),(1,2),(2,1),(2,2)])
qw.plot_contours(xx, yy, qw.harmonic_oscillator_2D(xx,yy,l_new,m_new))    
plt.title('l='+str(l_new)+', y='+str(m_new))   
plt.show()
plt.clf()