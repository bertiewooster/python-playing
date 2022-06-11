from rdkit import Chem
from rdkit.Chem import Draw

# from rdkit.Chem.Draw import IPythonConsole

m = Chem.MolFromSmiles('COc1ccc2c(c1)[nH]c(n2)[S@@](=O)Cc1ncc(c(c1C)OC)C')
m

# rdkit.Chem.Descriptors.

# from rdkit import Chem

# molecule = rdkit.Chem.MolFromSmiles("Cc1ccccc1")
# mw = rdkit.Chem.Descriptors.MolWt(molecule)
# print(mw)
