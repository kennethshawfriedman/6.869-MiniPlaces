f = open("logResults.txt","r") #opens file with name of "test.txt"

iters = []

trainingLoss = []
trainingTop1 = []
trainingTop5 = []

validateLoss = []
validateTop1 = []
validateTop5 = []

i = 0
for line in f:
	i += 1
	parts = line.split(',')
	if "Training" in parts[1]:
		iterCount = parts[0].split('r')[1].strip()
		iters.append(str(iterCount))
		temptl = parts[1].split('=')[1].strip()
		trainingLoss.append(temptl)
		temptop1 = parts[2].split('=')[1].strip()
		trainingTop1.append(temptop1)
		temptop5 = parts[3].split('=')[1].strip()
		trainingTop5.append(temptop5)
	else:
		temptl = parts[1].split('=')[1].strip()
		validateLoss.append(temptl)
		temptop1 = parts[2].split('=')[1].strip()
		validateTop1.append(temptop1)
		temptop5 = parts[3].split('=')[1].strip()
		validateTop5.append(temptop5)

result = "Iterations, TrainLoss, TrainTop1, TrainTop5, ValidLoss, ValidTop1, ValidTop5\n"

for i in range(len(iters)):
	result += iters[i] + ", "
	result += trainingLoss[i] + ", "
	result += trainingTop1[i] + ", "
	result += trainingTop5[i] + ", "
	result += validateLoss[i] + ", "
	result += validateTop1[i] + ", "
	result += validateTop5[i] + ", "
	result += "\n"

print(result)