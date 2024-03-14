#aibanez1:03/12/2024:ex7-brainwaves.py

#Q1
def func_waves(_frequency):
    '''
    Converts argument to float and print it's wave type
    ignores if argument is out of bounds
    :param _frequency:
    :return: none
    '''

    frequency = float(_frequency)

    wave_type = ''

    if frequency <= 4 and frequency >= 1:
        wave_type = 'Delta'
    elif frequency <= 8:
        wave_type = 'Theta'
    elif frequency <= 12:
        wave_type = 'Alpha'
    elif frequency < 35:
        wave_type = 'Beta'
    elif frequency <= 100:
        wave_type = 'Gamma'

    if (wave_type != ''):
        print('The frequency %-5.1f Hz is %-5s type.' %(frequency, wave_type))

#Q2
L=[99.33,30.21,10.0,5.0,2.0]

for i in L:
    func_waves(i)

