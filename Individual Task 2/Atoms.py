avogadro = 6.022*10**23

def num_atoms(elementAmountInGram, atomicWeight=196.97):
    sth = avogadro/atomicWeight
    print(sth*elementAmountInGram)

num_atoms(10)
num_atoms(10, 12.001)
num_atoms(10, 1.008)
