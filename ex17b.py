from sys import argv

from os.path import exists

script, from_file, to_file = argv


#in_file = open(from_file)
#in_data = in_file.read() 

#length = len(open(from_file).read())

#print(length)

#in_data = open(from_file).read() 

#print(f"The input file is {len(in_data)} bytes long. ")

#print(f"Does the output file exist? {exists(to_file)}. ")

#print("Ready? Hit return to continue, CTRL-C to abort. ")
#input()

open(to_file, 'w').write(open(from_file).read())

#out_file.write(in_data)

print(f"Copyed {len(open(from_file).read())} bytes of data from {from_file} to {to_file}.")

#out_file.close()
#in_file.close()
