# crispr_engine.py
# Description: gRNA design module with PAM site detection

def design_gRNAs(dna_sequence, pam_sequence="NGG"):
    dna_sequence = dna_sequence.upper()
    grnas = []
    for i in range(len(dna_sequence) - 23):
        candidate = dna_sequence[i:i+23]  # 20-nt gRNA + 3-nt PAM
        guide = candidate[:20]
        pam = candidate[20:23]

        if pam[1:] == "GG":  # Simplified PAM detection (NGG)
            grnas.append(guide)
    return grnas