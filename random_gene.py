# this is for random for test mtDNA
import random

def generate_random_dna_sequence(length=150):
    dna_bases = ['A', 'T', 'C', 'G']  # ตัวอักษรที่เราต้องการสุ่ม
    random_sequence = ''.join(random.choice(dna_bases) for _ in range(length))
    return random_sequence

# สุ่ม DNA sequence 150 ตัวอักษร
dna_sequence = generate_random_dna_sequence(150)
print("Random DNA Sequence:", dna_sequence)
