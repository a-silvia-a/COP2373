#User is prompted to enter email message
#The application will scan the message for 30 spam keywords or phrases.
#For each occurrence of one of these within the message, a point will be added to the message's "spam score".
#A rate of the likelihood that the message is spam will be based on the number of points received.
#Application will display the user's spam score, the likelihood message that it is spam,
#and the words/phrases which caused it to be spam.

#Function that reads and totals spam score.
def calculate_spam_score(email_text, keywords):
    #Normalize text for case-insensitive matching.
    clean_text = email_text.casefold()
    #Initialzie score and match trackers
    spam_score = 0
    triggered_words = []

    #Scan email for target words.
    for keyword in keywords:
        if keyword in clean_text:
            spam_score = spam_score + 1
            triggered_words.append(keyword)

    return spam_score, triggered_words

#Main Function, Controls workflow, handles user input, evaluates spam score, and displays final report.
def main():
    #Master list of spam keywords. (Constant)
    SPAM_KEYWORDS = [
        "free", "urgent", "winner", "offer", "discount",
        "exclusive", "guaranteed", "earn", "cash", "bonus",
        "deal", "credit", "loan", "prize", "claim",
        "buy", "save", "download", "cost", "attachment",
        "confidential", "finances", "act now", "budget",
        "limited offer", "special offer", "buy now", "money back",
        "high interest", "you have been chosen"
    ]

    #Get input and calculate results.
    user_email = input("Please enter the email message: ")
    final_score, words_found = calculate_spam_score(user_email, SPAM_KEYWORDS)

    #Loop to determine spam likelihood category.
    if final_score <= 4:
        spam_likelihood = "Low"
    elif final_score <= 12:
        spam_likelihood = "Moderate"
    else:
        spam_likelihood = "High"

    #Display final results.
    print ("\n --- Spam Detection Report ---")
    print (f"Your score of {final_score} puts you in the '{spam_likelihood}' likelihood category of being spam.")
    print (f"Keywords triggered: {words_found}")

if __name__ == "__main__":
    main()