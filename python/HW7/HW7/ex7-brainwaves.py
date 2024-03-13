#aibanez1:03/12/2024:ex7-brainwaves.py

#Q1
def func_waves(_frequency, _fmin = 1, _fmax = 100):
    '''
    Converts argument to float and print it's wave type
    ignores if argument is out of bounds
    :param _frequency:
    :param _fmin: minimum frequency
    :param _fmax: maximum frequency
    optional parameters because the assignment specifies using only one argument
    I included optional bounds so that I could loop instead of a long ifelif branch
    I know this isn't in the class materials but I thought it would be cool
    I understand if I have to explain it in class
    :return: none
    '''

    frequency = float(_frequency)

    wave_pairs = {'Delta': 4, 'Theta': 8, 'Alpha': 12, 'Beta': 35, 'Gamma': 100}
    wave_type = ''

    fmin = float(_fmin)
    fmax = float(_fmax)

    if (frequency >= fmin and frequency <= fmax):
        for type,j in wave_pairs.items():
            if frequency <= float(j):
                wave_type = type
                break
            else:
                continue
        if (wave_type != ''):
            print('The frequency %-5.1f Hz is %-5s type.' %(frequency, wave_type))

#Q2
L=[99.33,30.21,10.0,5.0,2.0]

for i in L:
    func_waves(i)

