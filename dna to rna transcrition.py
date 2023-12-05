##TRANSCRIPTION
##input => dna => ATCG
##output => rna => AUCG => complementary to dna => for A its U instead of T 




def transcription (dna_to_rna):
    
    bases_dict = {
        'A': 'U', 'T': 'A', 'C': 'G', 'G': 'C'
        }

    rna = "".join(bases_dict[base] for base in dna_to_rna)

        

    return (rna)


input_dna = str(input("ernter your DNA seq here: "))

result_rna = transcription(input_dna)
print(f"DNA: {input_dna}")
print(f"RNA: {result_rna}")
