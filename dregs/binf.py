def write_fasta_seq(fasta_fd, header, seq):
  fasta_fd.write('>%s\n' % header)
  # Note that for long sequences, this is ridiculously slow. I should rewrite it.

  # Don't use textwrap module included in standard library, as it's far too
  # slow for large FASTA files.
  n = len(seq)
  line_len = 80
  i = 0
  while i < n:
    fasta_fd.write(seq[i:(i + line_len)] + '\n')
    i += line_len

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

def calculate_n50(sizes, cutoff=50):
  """
  Abstract: Returns the N50 value of the passed list of numbers.
  Usage: N50(numlist)

  Based on the definition from this SEQanswers post
  http://seqanswers.com/forums/showpost.php?p=7496&postcount=4
  (modified Broad Institute's definition
  https://www.broad.harvard.edu/crd/wiki/index.php/N50)

  See SEQanswers threads for details:
  http://seqanswers.com/forums/showthread.php?t=2857
  http://seqanswers.com/forums/showthread.php?t=2332
  """
  sizes.sort(reverse = True)
  total_size = sum(sizes)
  threshold = (float(cutoff)/100) * total_size
  size_sum = 0

  for size in sizes:
    size_sum += size
    if size_sum >= threshold:
      return size

def test_calculate_n50():
  'Taken from http://en.wikipedia.org/w/index.php?title=N50_statistic&oldid=550470473'
  test_sizes =[2, 2, 2, 3, 3, 4, 8, 8]
  assert calculate_n50(test_sizes) == 8
