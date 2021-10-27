import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image  # pillow module

image = Image.open("dna-logo.jpg")
st.image(image, use_column_width=True)  # display img

st.write("""
# DNA Nucleotide Count Web App

This app counts the nucleotide composition of query DNA!

***
""")

# input text box

st.header("Ented DNA sequence")
sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG" \
                 "\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC" \
                 "\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT "
sequence = st.text_area("Sequence input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:]  # skip the sequence name
# sequence  # show list
sequence = ''.join(sequence)  # concatenate list to string

st.write("""
***
""")

# print input DNA sequence
st.header('INPUT (DNA Query)')
sequence

# DNA nucleotide count
st.header('OUTPUT (DNA Nucleotide Count)')

##  Print dictionary
st.subheader('1. Print dictionary')
def DNA_nucleotide_count(seq):
    d = dict([
        ("A", seq.count("A")),
        ("T", seq.count("T")),
        ("G", seq.count("G")),
        ("C", seq.count("C")),
    ])
    return d

## Print text
st.subheader("2. Print text")
X = DNA_nucleotide_count(sequence)
X_label = list(X)
X_value = list(X.values())
X

## Print text
st.subheader("3. Display DataFrame")
df = pd.DataFrame.from_dict(X, orient="index")
df = df.rename({0:"count"}, axis="columns")
df.reset_index(inplace=True)
df = df.rename(columns={"index":"nucleotide"})
st.write(df)

## Display bar chart using altair
st.subheader("3. Display Bar Chart")
p = alt.Chart(df).mark_bar().encode(
    x="nucleotide",
    y="count"
)

p = p.properties(
    width=alt.Step(80)  # controls bar's width
)

st.write(p)



