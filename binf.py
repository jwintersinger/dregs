def parse_fasta(fd):
  on_first_sequence = True

  for line in fd:
    line = line.strip()
    if line.startswith('>'):
      if on_first_sequence:
        on_first_sequence = False
      else:
        yield seq_id, seq

      seq = ''
      seq_id = line[1:]
    else:
      seq += line

  if not on_first_sequence:
    yield seq_id, seq

def generate_codon_table():
  bases = ['T', 'C', 'A', 'G']
  codons = [a+b+c for a in bases for b in bases for c in bases]
  amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
  codon_table = dict(zip(codons, amino_acids))
  return codon_table

def reverse_complement(seq):
  complements = {
    'A': 'T',
    'C': 'G',
    'G': 'C',
    'T': 'A',
  }
  rev_comp = ''
  for c in seq[::-1]:
    rev_comp += complements[c]
  return rev_comp
