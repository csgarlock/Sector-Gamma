def gen(min, max, scan1, scan2, scan3):
	for i in range(min, max+1):
		print(scan1+str(i)+scan2+str(i*5)+scan3)

if __name__ == '__main__':
	scan1 = "{\n\"Index\": "
	scan2 = ",\n\"ConcurrentCluster\": false,\n\"HideSpline\": true,\n\"Position\": {\n\"x\": 50.000,\n\"y\": 0,\n\"z\":"
	scan3 = "\n},\n\"Rotation\": {\n\"x\": 0,\n\"y\": 0,\n\"z\": 0\n},\n\"EventsOnPuzzleSolved\": [],\n\"RequiredItemsIndices\": []\n},"
	gen(1, 200, scan1, scan2, scan3)
