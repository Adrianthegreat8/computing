# write class header here

# variables

codons=['GAG', 'TGC', 'GCA', 'AGT', 'TTA', 'GGA', 'CAT', 'CAC', 'GGC', 'CCC',
        'ACA', 'ACT', 'GAT', 'CTA', 'TTC', 'GCT', 'GAC', 'CCT', 'CGC', 'GCC',
        'AAA', 'GGT', 'CTT', 'AGC', 'GTA', 'ATT', 'GAA',
        'CAA', 'CCG', 'GCG', 'ATC', 'TTG', 'CAG', 'AAT', 'AAC', 'CGT', 'ATA',
        'TAT', 'TAC', 'AGG', 'ACG', 'TGT', 'AGA', 'CTC', 'TCC', 'TGG', 'CCA',
        'TCG', 'TCA', 'GGG', 'CGA', 'ATG', 'AAG', 'CTG', 'CGG', 'GTG', 'GTC',
        'TCT', 'ACC', 'TTT', 'GTT']


amino=['E', 'C', 'A', 'S', 'L', 'G', 'H', 'H', 'G', 'P', 'T', 'T', 'D',
       'L', 'F', 'A', 'D', 'P', 'R', 'A', 'K', 'G', 'L', 'S', 'V',
       'I', 'E', 'Q', 'P', 'A', 'I', 'L', 'Q', 'N', 'N', 'R', 'I', 'Y', 'Y',
       'R', 'T', 'C', 'R', 'L', 'S', 'W', 'P', 'S', 'S', 'G', 'R', 'M', 'K',
       'L', 'R', 'V', 'V', 'S', 'T', 'F', 'V']


Dwh={'A': [1.8, 89.09], 'C': [2.5, 121.15], 'D': [-3.5, 133.1],
     'E': [-3.5, 147.13], 'F': [2.8, 165.19], 'G': [-0.4, 75.07],
     'H': [-3.2, 155.16], 'I': [4.5, 131.17], 'K': [-3.9, 146.19],
     'L': [3.8, 131.17], 'M': [1.9, 149.21], 'N': [-3.5, 132.12],
     'P': [-1.6, 115.13], 'Q': [-3.5, 146.15], 'R': [-4.5, 174.2],
     'S': [-0.8, 105.09], 'T': [-0.7, 119.12], 'V': [4.2, 117.15],
     'W': [-0.9, 204.23], 'Y': [-1.3, 181.19]}


Ldna=['AAG','ATG','TTC', 'CCG', 'TCC', 'GCA', 'CTA', 'GTG', 'AAC', 'GCC','CTA', 'TCC', 'TTG', 'TCG']

#Q1
gencode = dict(zip(codons,amino))
print(gencode)

#Q2
seq=''
for codon in Ldna:
    seq += gencode[codon]


print(seq)

#Q3
tweight=0
for AA in seq:
    tweight += Dwh[AA][1]

print('The total weight is %.2f g/mol' %tweight)