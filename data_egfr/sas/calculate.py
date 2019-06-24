from rdkit import Chem
from rdkit.Contrib.SA_Score.sascorer import calculateScore

with open('../id_smiles.txt') as f, open('data.txt', 'w') as w:
    for l in f:
        m_id, s1, s2 = l.split()
        m1, m2 = Chem.MolFromSmiles(s1), Chem.MolFromSmiles(s2)
        if m1 is None or m2 is None : continue
        c1,c2 = calculateScore(m1), calculateScore(m2)
        w.write(m_id+'\t'+str(c1)+'\t'+str(c2)+'\n')
