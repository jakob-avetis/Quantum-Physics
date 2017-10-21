# create function definition
def hydrogen_transition_energy(n1, n2, a0 = 1.0, Z=1.0, mu = 1.0, c = 137.0, alpha = 1.0/137.0):
    En = -(mu* (c**2) * (Z**2) * (alpha**2) )/2.0 * (1.0/(n1**2) - 1.0/(n2**2))
    return En
# initial variable
spectrum = []
# iterate over n1
for n1 in range(1, 11):
    # iterate over n2
    for n2 in range(1, 11):
        if n1 != n2: # Ensures that a transition actually happens
            qdict = {"n1":n1, "l1":0, "m1":0, "n2":n2, "l2":0, "m2":0}
            qdict['energy']=hydrogen_transition_energy(qdict['n1'],qdict['n2'])
            spectrum.append(qdict)
# sorted energy values
e_vals = np.unique([s['energy'] for s in spectrum])
# iterate over spectrum to plot wavelength color bands
for el in spectrum:
    wavel = qw.hartrees_to_wavelength(el['energy'])
    c = qw.wavelength_to_colour(wavel)
    plt.axvline(wavel, color=c,lw=2)
# plot options
plt.xlabel('Wavelength [nm]')
plt.xlim([390, 700])
plt.tick_params(labelleft=False)
plt.show()