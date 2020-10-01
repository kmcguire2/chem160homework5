def molemass(sequence):
    symbols = ["H", "C", "N", "O", "P", "S", "K", "F"]
    masses = [1.0079, 12.0107, 14.0067, 15.9994, 30.9738, 32.0660, 39.0983, 18.9984]
    atoms_dict = dict(zip(symbols, masses))
    total_mass = 0
    for i in range(len(sequence)):
        total_mass += atoms_dict[sequence[i]]
    return total_mass