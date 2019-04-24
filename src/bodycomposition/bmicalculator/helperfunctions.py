
def inchesToCentimeters(feet, inches):
	totalInches = feet*12 + inches
	centimeters_per_inch = 2.54
	return totalInches*centimeters_per_inch


def feetsFromCentimeters(centimeters):
	inches = centimeters / 2.54
	return inches // 12


def inchesFromCentimeters(centimeters):
	inches = centimeters / 2.54
	feets = feetsFromCentimeters(centimeters)
	return feets - (inches / 12)


def ComputeBMI(weight, height):
	return (weight/height*height)


def ComputeJP3Point(gender, first, second, third, age):
	if(gender == "male"):
		x = first + second + third
		return 1.10938 - (0.0008267*x) + (0.0000016*x*x) - (0.0002574*age)
	else:
		return 1.0994921 - (0.0009929*x) + (0.0000023*x*x) - (0.0001392*age)


def ComputeJP7Point(gender, first, second, third, fourth, fifth, sixth, seventh, age):
	if(gender == "male"):
		x = first + second + third + fourth + fifth + sixth + seventh
		return 1.112 - (0.00043499*x) + (0.00000055*x*x) - (0.00028826*age)
	else:
		return 1.097 - (0.00046971*x) + (0.00000056*x*x) - (0.00012828*age)


def ComputeBodyFatPercentage(bodyDensity):
	return (4.95/bodyDensity) - 4.50


def ComputeFatMass(fatPercentage, weight):
	return fatPercentage*weight


def ComputeLeanMass(fatMass, weight):
	return weight - fatMass


# Once you calculate your BMR factor in activity to account for calories burned during exercise.

# BMR x 1.2 for low intensity activities and leisure activities (primarily sedentary)

# BMR x 1.375 for light exercise (leisurely walking for 30-50 minutes 3-4 days/week, golfing, house chores)

# BMR x 1.55 for moderate exercise 3-5 days per week (60-70% MHR for 30-60 minutes/session)

# BMR x 1.725 for active individuals (exercising 6-7 days/week at moderate to high intensity (70-85% MHR) for 45-60 minutes/session)

# BMR x 1.9 for the extremely active individuals (engaged in heavy/intense exercise like heavy manual labor, heavy lifting, endurance athletes, and competitive team sports athletes 6-7 days/week for 90 + minutes/session)

def ComputeCalorieRequirement(activityLevel, leanMass):
	activityLevelCoefficients = { 0: 1.2, 1: 1.375, 2: 1.55, 3: 1.725, 4: 1.9 }
	c = choices.get(key, activityLevel)
	return 13.8*leanMass*c