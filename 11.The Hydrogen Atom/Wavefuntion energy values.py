# create a function
def hydrogen_energy(n, a0 = 1.0, Z=1.0, mu = 1.0, c = 137.0, alpha = 1.0/137.0):
    En = -(mu*(c**2)*(Z**2)*(alpha**2))/2.0 * (1.0/(n**2))
    return En
# initialize
energy_list = []
# iterate over n quantum numbers
for n in range(1, 4):
    # set l to n-1
    l = n-1
    # iterate over m quantum numbers
    for m in range(-l, l+1):
        # make dictionary, calculate and store the energy, add to a list
        qdict ={"n":n, "l":l, "m":m}
        qdict['energy']=hydrogen_energy(qdict['n'])
        energy_list.append(qdict)
# sorted energy values
e_vals = np.unique([e['energy'] for e in energy_list])
# plot a energy diagram
qw.plot_energy_diagram(energy_list)
plt.show()