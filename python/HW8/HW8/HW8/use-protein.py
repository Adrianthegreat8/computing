#aibanez1:03/25/2024:use-protein.py

D={'Q96524': 'MKMDKKTIVWFRRDLRIEDNPALAAAAHEGSVFPVFIWCPEEEGQFYPGRASRWWMKQSLAHLSQSLKALGSDLTLIKTHNTISAILDCIRVTGATKVVFNHLYDPVSLVRDHTVKEKLV',
   'P97784': 'MGVNAVHWFRKGLRLHDNPALKECIQGADTIRCVYILDPWFAGSSNVGINRWRFLLQCLEDLDANLRKLNSRLFVIRGQPADVFPRLFKEWNITKLSIEYDSEPFGKERDAAIKKLATEA',
   'Q9R194': 'MAAAAVVAATVPAQSMGADGASSVHWFRKGLRLHDNPALLAAVRGARCVRCVYILDPWFAASSSVGINRWRFLLQSLEDLDTSLRKLNSRLFVVRGQPADVFPRLFKEWGVTRLTFEYDS',
   'O77059': 'MATRGANVIWFRHGLRLHDNPALLAALADKDQGIALIPVFIFDGESAGTKNVGYNRMRFLLDSLQDIDDQLQAATDGRGRLLVFEGEPAYIFRRLHEQVRLHRICIEQDCEPIWNERDES',
   'Q49AN0': 'LPKKPVGLVTSQQMESCRAEIQENHDETYGVPSLEELGFPTEGLGPAVWQGGETEALARLDKHLERKAWVANYERPRMNANSLLASPTGLSPYLRFGCLSCRLFYYRLWDLYKKVKRNST'}

#Q1
import proteins as pr

#Q2
ID = list(D.keys())

#Q3
aromaticities = [pr.aromaticity(D[i]) for i in ID]

#Q4
weights = [pr.weight(D[i]) for i in ID]

#Q5
for i in range(len(D)):
   print('%s %.2f %.2f' % (ID[i], aromaticities[i], weights[i]))

#Q6
index = weights.index(max(weights))
print('%s %.1e g/mol' % (ID[index], weights[index]))



