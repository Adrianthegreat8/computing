#aibanez1:03/25/2024:prtoeins.py

#Q1
"""
Computes protein sequencence information
"""

d_weight={'E': 147.13, 'C': 121.15, 'T': 119.12, 'G': 75.07, 'Y':
181.19, 'R': 174.2, 'V': 117.15, 'W': 204.23, 'I': 131.17, 'K': 146.19,
'M': 149.21, 'Q': 146.15, 'F': 165.19, 'A': 89.09, 'H': 155.16, 'S':
105.09, 'N': 132.12, 'D': 133.1, 'L': 131.17, 'P': 115.13}

#Q2
def freq_am (sequence, amino_acid):
    "Returns relative frequency of an amino acid in a peptide"
    Nc = sequence.count(amino_acid)
    N = len(sequence)
    Fc = Nc/N
    return Fc

#Q3
def aromaticity (sequence):
    "Returns the aromaticity of a peptide"
    Fw = freq_am(sequence, 'W')
    Fy = freq_am(sequence, 'Y')
    Ff = freq_am(sequence, 'F')
    aromaticity = Fw + Fy + Ff
    return aromaticity

#Q4
def weight (sequence):
    "Returns the molecular wegiht of a peptide"
    Mw = 0
    for i in sequence:
        Mw += d_weight[i]
    return Mw

#Q5
if __name__ == "__main__":
    from sys import argv

    s1 = argv[1]
    s1_fa = freq_am(s1, 'W')
    print('The frequency of W is %.2f' %s1_fa)

    s1_aro = aromaticity(s1)
    print('The aromaticity is %.1f' %s1_aro)

    weight = weight(s1)
    print('Weight=%.2f g/mol' %weight)