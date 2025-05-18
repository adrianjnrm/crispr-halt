# simulation.py
# Description: Simulates HIV clearance using CRISPR

def run_simulation(scored_gRNAs, genome):
    # Simulate removal based on gRNA score
    remaining = 1.0
    for g, risk in scored_gRNAs:
        remaining -= (1 - risk) * 0.4
    return max(remaining, 0)