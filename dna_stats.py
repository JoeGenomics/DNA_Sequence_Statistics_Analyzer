from Bio import SeqIO

fasta_file = "example.fasta"

for record in SeqIO.parse(fasta_file, "fasta"):
    seq = record.seq
    a = seq.count("A")
    t = seq.count("T")
    g = seq.count("G")
    c = seq.count("C")
    length = len(seq)
    gc = (g + c) / length * 100
    at = (a + t) / length * 100

    print("Sequence ID:", record.id)
    print("Length:", length)
    print("A:", a)
    print("T:", t)
    print("G:", g)
    print("C:", c)
    print("GC Content:", round(gc, 2), "%")
    print("AT Content:", round(at, 2), "%")
