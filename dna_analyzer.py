# DNA ANALYZER

def read_fasta(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    header = lines[0].strip()
    sequence = ""

    for line in lines[1:]:
        sequence += line.strip()

    return header, sequence


def analyze_sequence(sequence):
    sequence = sequence.upper()

    length = len(sequence)
    A = sequence.count("A")
    T = sequence.count("T")
    G = sequence.count("G")
    C = sequence.count("C")

    gc_content = (G + C) / length * 100

    return length, A, T, G, C, gc_content


def find_start_codon(sequence):
    for i in range(len(sequence)):
        if sequence[i:i+3] == "ATG":
            return i
    return -1


def find_stop_codon(sequence):
    stop_codons = ["TAA", "TAG", "TGA"]

    for i in range(len(sequence)):
        codon = sequence[i:i+3]
        if codon in stop_codons:
            return i, codon
    return -1, None


def extract_gene(sequence):
    stop_codons = ["TAA", "TAG", "TGA"]

    for i in range(len(sequence)):
        if sequence[i:i+3] == "ATG":
            for j in range(i, len(sequence), 3):
                codon = sequence[j:j+3]
                if codon in stop_codons:
                    return sequence[i:j+3]
    return None


codon_table = {
    "ATA":"I","ATC":"I","ATT":"I","ATG":"M",
    "ACA":"T","ACC":"T","ACG":"T","ACT":"T",
    "AAC":"N","AAT":"N","AAA":"K","AAG":"K",
    "AGC":"S","AGT":"S","AGA":"R","AGG":"R",
    "CTA":"L","CTC":"L","CTG":"L","CTT":"L",
    "CCA":"P","CCC":"P","CCG":"P","CCT":"P",
    "CAC":"H","CAT":"H","CAA":"Q","CAG":"Q",
    "CGA":"R","CGC":"R","CGG":"R","CGT":"R",
    "GTA":"V","GTC":"V","GTG":"V","GTT":"V",
    "GCA":"A","GCC":"A","GCG":"A","GCT":"A",
    "GAC":"D","GAT":"D","GAA":"E","GAG":"E",
    "GGA":"G","GGC":"G","GGG":"G","GGT":"G",
    "TCA":"S","TCC":"S","TCG":"S","TCT":"S",
    "TTC":"F","TTT":"F","TTA":"L","TTG":"L",
    "TAC":"Y","TAT":"Y","TAA":"_","TAG":"_",
    "TGC":"C","TGT":"C","TGA":"_","TGG":"W",
}


def translate_dna(sequence):
    protein = ""

    for i in range(0, len(sequence), 3):
        codon = sequence[i:i+3]
        if len(codon) == 3:
            protein += codon_table.get(codon, "?")

    return protein


# MAIN PROGRAM

file_path = input("Enter FASTA file path: ")

header, sequence = read_fasta(file_path)

length, A, T, G, C, gc = analyze_sequence(sequence)

start_pos = find_start_codon(sequence)
stop_pos, stop_type = find_stop_codon(sequence)

print("\n--- DNA ANALYSIS ---")
print("Header:", header)
print("Length:", length)

print("\nBase Counts:")
print("A:", A)
print("T:", T)
print("G:", G)
print("C:", C)

print(f"\nGC Content: {gc:.2f}%")

print("\nGene Signals:")
print("Start Codon (ATG) at position:", start_pos)

if stop_pos != -1:
    print("Stop Codon (" + stop_type + ") at position:", stop_pos)
else:
    print("No stop codon found")


gene = extract_gene(sequence)

if gene:
    protein = translate_dna(gene)

    print("\nExtracted Gene:")
    print(gene[:60] + "...")

    print("\nProtein Sequence:")
    print(protein[:60] + "...")
else:
    print("\nNo valid gene found")
