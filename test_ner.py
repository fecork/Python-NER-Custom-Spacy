# Perform standard imports
import spacy

nlp = spacy.load("en_core_web_sm")

# Write a function to display basic entity info:
def show_ents(doc):
    if doc.ents:
        for ent in doc.ents:
            print(
                ent.text
                + " - "
                + str(ent.start_char)
                + " - "
                + str(ent.end_char)
                + " - "
                + ent.label_
                + " - "
                + str(spacy.explain(ent.label_))
            )
    else:
        print("No named entities found.")


# texto = "Apple is looking at buying U.K. startup for $1 billion"
texto = """
CANCELLATIONS:
ANY TIME
CHARGE USD 200.00 FOR CANCEL.
NOTE  TEXT BELOW NOT VALIDATED FOR AUTOPRICING.

FOR ALL JOURNEYS BEFORE or AFTER FIRST FLIGHT
DEPARTURE  USD200

APPLICABLE FEES ARE TO BE CONVERTED INTO
LOCAL CURRENCY AT THE BANKERS SELLING RATE.

FEES ARE NOT APPLICABLE FOR INFANT WITHOUT A SEAT

IN CASE OF TICKET UPGRADE THE ORIGINAL
NONREFUNDABLE AMOUNT REMAINS NONREFUNDABLE.

YR IS NONREFUNDABLE FOR ALL FARES.

IN CASES OF NOSHOW CHARGE NO SHOW FEE OF USD100
AND CANCELLATION FEE OF USD200 FOR CANCEL.

FOR ANY CANCELLATIONS THE STRICTER FARE
CONDITIONS WILL APPLY TO THE ENTIRE JOURNEY.
"""
doc1 = nlp(texto)
show_ents(doc1)
