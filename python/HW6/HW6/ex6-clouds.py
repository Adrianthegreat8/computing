#aibanez1:03/05/2024:ex6-clouds.py

#Q1
while True:
    cloud_height = int(input('Enter a positive number for the height of the cloud: \n'))
    if cloud_height > 0:
        break
    print("Number must be positive, try again. \n")


if cloud_height < 6500:
    print('This is a low cloud')
elif cloud_height <= 20000:
    print('This is a middle cloud')
else:
    print('This is a high cloud')
