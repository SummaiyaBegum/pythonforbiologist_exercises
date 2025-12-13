# opening the file 
# "r" is for reading
with open("genomic_dna.txt", "r") as my_file:
    file_contents = my_file.read()
print(file_contents)

# removing the spaces
dna = "".join(file_contents.split())
print(dna)

exon1 = dna[0:62]
exon2 = dna[90:len(dna)]

# coding dna
coding_dna = exon1 + exon2
print(coding_dna)

#non coding dna
non_coding_dna = dna[62:90]
print(non_coding_dna)

#Writing the files to a new file and saving them
coding_file = open("coding_dna.txt", "w")
coding_file.write(coding_dna)
#close the file
coding_file.close()

non_coding_file = open("non_coding_dna.txt", "w")
non_coding_file.write(non_coding_dna)
non_coding_file.close()

#Reading the created new files
with open("coding_dna.txt", "r") as c_file:
    file_coding = c_file.read()
print(file_coding)

with open("non_coding_dna.txt", "r") as nc_file:
    file_non_coding = nc_file.read()
print(file_non_coding)