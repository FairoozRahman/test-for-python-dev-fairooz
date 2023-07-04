from setfit import SetFitModel


# Analyses the text submitted in the form
def AnalyzeText(text):
    # It takes some time for the first text to analyze as it downloads the weights
    model = SetFitModel.from_pretrained("StatsGary/setfit-ft-sentinent-eval") 

    preds = model([text])

    if preds[0] == 0:
        return("Negative")
    else:
        return("Positive")