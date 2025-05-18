# off_target_predictor.py
# Description: Scores each gRNA with off-target risk

def score_gRNAs(gRNAs):
    # Assign dummy off-target risk scores
    return [(g, round(0.01 + i * 0.03, 3)) for i, g in enumerate(gRNAs)]