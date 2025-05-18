# hiv_data_loader.py
# Description: Load and validate sequence

def load_hiv_genome(sequence):
    sequence = sequence.upper().replace("\n", "")
    valid_nucleotides = {"A", "T", "G", "C"}
    cleaned = ''.join([c for c in sequence if c in valid_nucleotides])
    if len(cleaned) < 100:
        raise ValueError("Input sequence too short or contains invalid characters.")
    return cleaned