from pydoc import doc
import spacy

nlp_ner = spacy.load("data/07_model_output/model-best")

text = """
"CANCELLATIONS ANY TIME CHARGE USD 666.00 FOR CANCEL.
NOTE - TEXT BELOW NOT VALIDATED FOR AUTOPRICING.
FOR ALL JOURNEYS BEFORE/AFTER FIRST FLIGHT DEPARTURE - USD300
APPLICABLE FEES ARE TO BE CONVERTED INTO LOCAL CURRENCY AT THE BANKERS SELLING RATE.
FEES ARE NOT APPLICABLE FOR INFANT WITHOUT A SEAT
IN CASE OF TICKET UPGRADE THE ORIGINAL NON-REFUNDABLE AMOUNT REMAINS NON-REFUNDABLE.
YR IS NON-REFUNDABLE FOR ALL FARES.IN CASES OF NO-SHOW CHARGE NO SHOW FEE OF USD300 
AND CANCELLATION FEE OF USD300 FOR CANCEL.\
FOR ANY CANCELLATIONS THE STRICTER FARE\ CONDITIONS WILL APPLY TO THE ENTIRE JOURNEY.
"""

doc = nlp_ner(text)

colors = {
    "CANCELLATION_TIME": "#F67DE3",
    "CHARGE_CANCEL": "#7DF6D9",
    "CHARGE_NOSHOW": "#FFFFFF",
}
options = {"colors": colors}

spacy.displacy.render(doc, style="ent", options=options, jupyter=True)