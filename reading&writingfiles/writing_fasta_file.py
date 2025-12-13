#creating a fasta file
new_fasta_file = open("new_dna.fasta", "w")

#assigning header and sequence
header1 = "ABC123"
seq1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"

header2 = "DEF456" 
seq2 = "actgatcgacgatcgatcgatcacgact"

header3 = "HIJ789" 
seq3 = "ACTGAC-ACTGT--ACTGTA----CATGTG"

#writing the file
new_fasta_file.write('>'+header1 + "\n" + seq1 + "\n" +   #to have header and sequence in separate lines "\n"
                     ">"+ header2 + "\n" + seq2.upper() + "\n" +
                     ">"+header3 + "\n" + seq3.replace("-", "") + "\n")
new_fasta_file.close()

#reading the file
with open("new_dna.fasta", "r") as nf_file:
    file_new_dna = nf_file.read()
print(file_new_dna)