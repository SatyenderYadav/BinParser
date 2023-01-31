import struct
import argparse
import datetime

def convert_filetime(file_time):
	return((datetime.datetime (1601, 1, 1) + datetime.timedelta(seconds=file_time/10000000)).strftime('%Y-%m-%d %H:%M:%S:%f'))

def showResult(fileSize,fileDeleteTime,fileNameLength,DeletedfileName):
	print("\t\t\u001b[1m\u001b[38;5;8m  =============================================\u001b[37;1m")	
	print("\t\t▒█▀▀█ ▄█  █▀▀▄ 　  █▀▀█  █▀█  █▀▀█ █▀▀ █▀▀█ █▀▀█ ")
	print("\t\t▒█▀▀▄  █  █  █ 　  █▄▄█ █▄▄█▄ █▄▄▀ ▀▀█   ▀▄ █▄▄▀ ")
	print("\t\t▒█▄▄█ ▄█▄ ▀  ▀ 　  █       █  ▀ ▀▀ ▀▀▀ █▄▄█ ▀ ▀▀")
	print("\t\t\u001b[1m\u001b[38;5;8m  =============================================\u001b[37;1m")
	print("\033[0m")
	print("\033[93mDeleted FileName: \033[0m",DeletedfileName.split("\\")[-1])
	print("\033[93mFile Size [ KB ]: \033[0m",fileSize)
	print("\033[93mFile Name Length: \033[0m",fileNameLength - 1)
	print("\033[93mFile Delete Time [UTC]: \033[0m", fileDeleteTime)
	print("\033[93mOrginal Path: \033[0m",DeletedfileName)

def main(fileName):
	with open(fileName, mode="rb") as RecycleMetaFile:
		headersInfo = (struct.unpack("q",RecycleMetaFile.read(8)))[0]
		fileSize = (struct.unpack("q",RecycleMetaFile.read(8)))[0] / 1000
		fileDeleteTimeEpoch = (struct.unpack("q",RecycleMetaFile.read(8)))[0]
		fileDeleteTime = convert_filetime(fileDeleteTimeEpoch)
		fileNameLength = (struct.unpack("I",RecycleMetaFile.read(4)))[0]
		RecycleMetaFile.seek(28)
		DeletedfileName = (RecycleMetaFile.read().decode("ascii"))
		showResult(fileSize,fileDeleteTime,fileNameLength,DeletedfileName)

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-f","--file", type=str, required=True ,help="The $I file from the $Recycle.Bin")
	args = parser.parse_args()
	main(args.file)


