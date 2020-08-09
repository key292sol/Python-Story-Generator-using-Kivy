
def ScreensAdd(that):
	with open('aliencomp.txt','a') as fa:
		fa.write('\n' + that)
		
def ScreenBack():
	screens = GetScreens()
	if screens[-1] == 'StoryStart':
		EraseScreens()
		return 'main'
		
	st = screens[-2]
	del screens[-2:]
	with open('aliencomp.txt','w') as fw:
		fw.write('\n'.join(screens))		
	return st
		
def GetScreens():
	screens = []
	try:
		with open('aliencomp.txt','r') as fr:
			screens = fr.readlines()			
			for i in range(len(screens)):
				screens[i] = screens[i][:-2] + screens[i][-2:].replace('\n','')		
	except IOError as e:
		screens = ["StoryStart"]
	
	return screens
	
def EraseScreens():
	with open('aliencomp.txt','w') as fa:
		with open('extras.txt','w') as fe:
			pass


def SetExtra(key, val):
	keyExists = GetExtra(key)
	if keyExists:
		with open('extras.txt','r') as fr:
			lines = fr.readlines()
			lines[keyExists["FileLineIndex"]] = lines [keyExists["FileLineIndex"]] [:keyExists["ColonIndex"]] + ": " + keyExists["NodeData"]
			with open('aliencomp.txt','w') as fw:
				fw.write("".join(lines))
	else:
		with open('extras.txt','a') as fa:
			fa.write(key + ": " + val + "\n")


def GetExtra(key):
	with open('extras.txt','r') as fr:
		lines = fr.readlines()
		for li in range(len(lines)):
			colonIndex = lines[li].find(":")
			if lines[li][:colonIndex] == key:
				return {
					"NodeKey": lines[li][:colonIndex],
					"NodeData": lines[li][colonIndex + 1:],
					"FileLineIndex": li,
					"ColonIndex": colonIndex
				}

	return False

