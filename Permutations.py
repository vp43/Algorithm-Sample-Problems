
def perms(permuteList):
	if len(permuteList) <= 1:
		return [permuteList]
	else:
		finalList = []
		for index in range(len(permuteList)):
			key = permuteList[index]	
			tempList = permuteList[:index] + permuteList[index+1:]
			for items in perms(tempList):
				finalList.append([key] + items)
		return finalList
			


