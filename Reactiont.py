def reaction_stoichiometry(reaction):
    reactants, products = reaction.split('->')
    reactant_atoms = count_atoms(reactants.strip())
    product_atoms = count_atoms(products.strip())
    ratios = {atom: product_atoms[atom] / reactant_atoms.get(atom, 1) for atom in product_atoms}
    return ratios

reaction = "2H2 + O2 -> 2H2O"
print("Reaction:", reaction)
print("Stoichiometry ratios:", reaction_stoichiometry(reaction))
