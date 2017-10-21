# create your normalize wfn function
def normalize_wfn(x, psi_x):
    pdf = qw.prob_density(psi_x)
    integral_norm = simps(pdf, x)
    wf_normed = psi_x/np.sqrt(integral_norm)
    return wf_normed
# initialize variables
L = 10.0
x = np.arange(0,L,0.01)
psi_x = np.zeros_like(x)
# do a for loop to sum all 4 eigenfunctions
for n in range(1,5):
    psi_x = psi_x + qw.pib_eigenfunction(x,L,n)
# get pdf, normalize for psi_x
pdf = qw.prob_density(psi_x)
psi_normed = normalize_wfn(x, psi_x)
# calculate norms before and after
norm_before = simps(qw.prob_density(psi_x), x)
norm_after = simps(qw.prob_density(psi_normed), x)
print('Norm before:',norm_before)
print('Norm after:',norm_after)
#plot
plt.plot(x,psi_x,label="$\psi$")
plt.plot(x,pdf,label="pdf")
plt.legend()
plt.show()