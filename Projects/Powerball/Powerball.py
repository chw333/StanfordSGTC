import random
import time
power = [random.randint(1, 69) for x in range(5)]
ball = random.randint(1, 26)

ouFile = open('MyPowerball.txt', 'a')
myballs = '\t'.join([str(x) for x in power]) + '\t' + str(ball)
print(myballs)
ouFile.write(time.ctime() + '\n')
ouFile.write(myballs + '\n')
ouFile.close()
