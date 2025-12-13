#assigning header and sequence
header1 = "ABC123"
seq1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"

header2 = "DEF456" 
seq2 = "actgatcgacgatcgatcgatcacgact"

header3 = "HIJ789" 
seq3 = "ACTGAC-ACTGT--ACTGTA----CATGTG"

# creating separate files for each sequence
file1 = open(header1 + ".fasta", "w")
file1.write(header1 + "\n" + seq1 + "\n")
file1.close()

file2 = open(header2 + ".fasta", "w")
file2.write(header2 + "\n" + seq2.upper() + "\n")
file2.close()

file3 = open(header3 + ".fasta", "w")
file3.write(header3 + "\n" + seq3.replace("-", "") + "\n")
file3.close()   

print("Sequences saved to " + header1 + ".fasta, " + header2 + ".fasta, " + header3 + ".fasta")

#reading the created files
with open(header1 + ".fasta", "r") as h1_file:
    file_h1 = h1_file.read()
print(file_h1)

with open(header2 + ".fasta", "r") as h2_file:
    file_h2 = h2_file.read()
print(file_h2)

with open(header3 + ".fasta", "r") as h3_file:
    file_h3 = h3_file.read()
print(file_h3)  