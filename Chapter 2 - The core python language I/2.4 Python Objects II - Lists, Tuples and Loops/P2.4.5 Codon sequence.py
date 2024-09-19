"""
A DNA sequence encodes each amino acid making up a protein as a threenucleotide
sequence called a codon. For example, the sequence fragment AGTCTTATATCT
contains the codons (AGT, CTT, ATA, TCT) if read from the first position
(“frame”). If read in the second frame it yields the codons (GTC, TTA, TAT) and in the
third (TCT, TAT, ATC).
Write some Python code to extract the codons into a list of three-letter strings given
a sequence and frame as an integer value (0, 1 or 2).
"""

def extract_codon(sequence, frame):
    output_list =[]
    for i in range(frame, len(sequence), 3):
        if i+3 <= len(sequence):
            output_list.append(sequence[i:i+3])
    return output_list

sequence_A = 'AGTCTTATATCT'
print(extract_codon(sequence_A, 0))
print(extract_codon(sequence_A, 1))
print(extract_codon(sequence_A, 2))