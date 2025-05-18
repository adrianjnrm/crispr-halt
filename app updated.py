
# app.py
# CRISPR-HALT: HIV Latency Eradication Simulator (Streamlit App)

import streamlit as st
from crispr_engine import design_gRNAs
from hiv_data_loader import load_hiv_genome
from off_target_predictor import score_gRNAs
from simulation import run_simulation
from visualization import plot_hiv_clearance

st.set_page_config(page_title="CRISPR-HALT", layout="centered")
st.title("🧬 CRISPR-HALT: HIV Latency Eradication Simulator")
st.markdown("""
Welcome to the CRISPR-HALT project — an interactive tool to simulate the eradication of latent HIV proviral DNA using CRISPR/Cas9 technology.
""")

# Input: Paste HIV Proviral DNA Sequence
hiv_sequence = st.text_area("🔬 Paste the HIV Proviral DNA Sequence (FASTA or Raw Format):", height=200)

# Run Simulation
if st.button("🚀 Design gRNAs and Simulate Editing"):
    if not hiv_sequence.strip():
        st.warning("Please input a valid DNA sequence.")
    else:
        st.subheader("Step 1: Processing Input DNA")
        genome = load_hiv_genome(hiv_sequence)
        st.success("✅ Genome loaded and validated successfully.")

        st.subheader("Step 2: Designing gRNAs with PAM site detection")
        gRNAs = design_gRNAs(genome)
        st.write(f"🧬 {len(gRNAs)} candidate gRNAs generated.")
        st.code(gRNAs)

        st.subheader("Step 3: Scoring Off-Target Risks")
        scored = score_gRNAs(gRNAs)
        for g, score in scored:
            st.write(f"gRNA: `{g}` | Off-Target Risk Score: `{score}`")

        st.subheader("Step 4: Running Simulation")
        result = run_simulation(scored, genome)
        st.write(f"📉 Predicted HIV Remaining: `{round(result * 100, 2)}%`")

        st.subheader("Step 5: Visualizing Results")
        plot = plot_hiv_clearance(result)
        st.pyplot(plot)

st.markdown("---")
st.caption("Created by Adrian Mahachi • African Science Buskas • Field: Bioengineering + CRISPR Simulation")
