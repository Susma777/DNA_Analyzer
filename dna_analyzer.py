class DNA:
    def __init__(self, sequence):
        self.sequence = sequence.upper()

    def gc_content(self):
        gc_count = 0
        for base in self.sequence:
            if base == "G" or base == "C":
                gc_count += 1
        return (gc_count / len(self.sequence)) * 100

    def length(self):
        return len(self.sequence)

    def show(self):
        print("Sequence:", self.sequence)
        print("Length:", self.length())
        print("GC Content:", self.gc_content())


Sequence = input("Enter DNA Sequence: ")
dna1 = DNA(Sequence)
dna1.show()
