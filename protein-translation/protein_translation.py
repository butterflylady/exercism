def proteins(strand):
    output=[]
    codons_list=[strand[i:i+3] for i in range(0,len(strand),3)]
    protein_dict={
        "Methionine":("AUG"),
        "Phenylalanine":("UUU", "UUC"),
        "Leucine":("UUA", "UUG"),
        "Serine":("UCU", "UCC", "UCA", "UCG"),
        "Tyrosine":("UAU", "UAC"),
        "Cysteine":("UGU", "UGC"),
        "Tryptophan":("UGG"),
        "STOP":("UAA", "UAG", "UGA")
    }
    for codon in codons_list:
        for protein, codon_val in protein_dict.items():
            if codon in codon_val:
                if protein!="STOP":
                    output.append(protein)
                else:
                    return output
    return output



