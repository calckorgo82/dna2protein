import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # change input to uppercase
        dna = request.form.get("DNA").upper().replace(" ","")
        # check for valid input
        error = "Please input a valid DNA sequence!"
        if len(dna) == 0:
            return render_template("error.html", error=error)
        prohibited_letters = ["B","D","E", "F", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "U", "V", "W", "X", "Y", "Z"]
        for nucleotide in prohibited_letters:
            if nucleotide in dna:
                return render_template("error.html", error=error)
        for nucleotide in dna:
            if nucleotide.isalpha() == False:
                return render_template("error.html", error=error)

        # change DNA to RNA
        dna = dna.replace("A", "U")
        dna = dna.replace("T", "A")
        dna = dna.replace("G", "Temp")
        dna = dna.replace("C", "G")
        dna = dna.replace("Temp", "C")
        rna = dna
        sample_rna = rna

        # initialize a codon dictionary
        codon_chart = {
            "UUU" : "Phe - ", "UUC" : "Phe - ", "UUA" : "Leu - ", "UUG" : "Leu - ", "CUU" : "Leu - ", "CUC" : "Leu - ",
            "CUA" : "Leu - ", "CUG" : "Leu - ", "UCU" : "Ser - ", "UCC" : "Ser - ", "UCA" : "Ser - ", "UCG" : "Ser - ",
            "AGU" : "Ser - ", "AGC" : "Ser - ", "UAU" : "Tyr - ", "UAC" : "Tyr - ", "UGU" : "Cys - ", "UGC" : "Cys - ",
            "UAA" : "STOP", "UAG" : "STOP", "UGA" : "STOP", "UGG" : "Trp - ", "CCU" : "Pro - ", "CCA" : "Pro - ",
            "CCC" : "Pro - ", "CCG" : "Pro - ", "CGU" : "Arg - ", "CGC" : "Arg - ", "CGA" : "Arg - ", "CGG" : "Arg - ",
            "AGA" : "Arg - ", "AGG" : "Arg - ", "AUU" : "Ile - ", "AUC" : "Ile - ", "AUA" : "Ile - ", "AUG" : "Met - ",
            "ACU" : "Thr - ", "ACC" : "Thr - ", "ACA" : "Thr - ", "ACG" : "Thr - ", "AAU" : "Asn - ", "AAC" : "Asn - ",
            "AAA" : "Lys - ", "AAG" : "Lys - ", "GUA" : "Val - ", "GUC" : "Val - ", "GUG" : "Val - ", "GUU" : "Val - ",
            "GCU" : "Ala - ", "GCC" : "Ala - ", "GCA" : "Ala - ", "GCG" : "Ala - ", "GAU" : "Asp - ", "GAC" : "Asp - ",
            "GAA" : "Glu - ", "GAG" : "Glu - ", "GGU" : "Gly - ", "GGC" : "Gly - ", "GGA" : "Gly - ", "GGG" : "Gly - ",
            "CAU" : "His - ", "CAC" : "His - ", "CAA": "Gln - ", "CAG": "Gln - "
        }

        protein = ""
        # find start codon
        while len(sample_rna) >= 3:
            if sample_rna[0:3] == "AUG":
                # translate mRNA to amino acid
                while len(sample_rna) >= 3:
                    codon = sample_rna[:3]
                    protein += codon_chart[codon]
                    sample_rna = sample_rna[3:]
                    if codon_chart[codon] == "STOP":
                        break
                break
            else:
                sample_rna = sample_rna[1:]
                if len(sample_rna) == 2:
                    error = "There is no indication of a start codon!"
                    return render_template("error.html", error=error)

        return render_template("result.html", rna=rna, protein=protein)
    else:
        return render_template("index.html")