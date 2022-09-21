coordinates  = list(map(float, input().split()))

if (coordinates[0] == 0) and (coordinates[1] == 0):
    print('Origem')

elif (coordinates[0] != 0) and (coordinates[1] == 0):
    print('Eixo X')

elif (coordinates[0] == 0) and (coordinates[1] != 0):
    print("Eixo Y")

else:
    if (coordinates[0] > 0) and (coordinates[1] > 0):
        print('Q1')

    elif (coordinates[0] < 0) and (coordinates[1] < 0):
        print('Q3')

    elif (coordinates[0] < 0) and (coordinates[1] > 0):
        print('Q2')

    elif (coordinates[0] > 0) and (coordinates[1] < 0):
        print('Q4')
