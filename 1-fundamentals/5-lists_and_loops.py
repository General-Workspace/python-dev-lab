acronyms = []

acronyms.append("LOL")
acronyms.append("IDK")
acronyms.append("SMH")
acronyms.append("TBH")
acronyms.append("RN")
acronyms.append("BRB")
acronyms.append("BTW")
acronyms.append("BFF")
acronyms.append("FBF")
acronyms.append("FTW")

entered_acronym = input("Enter an acronym: ")

if entered_acronym.upper() in acronyms:
    pass
else:
    acronyms.append(entered_acronym.upper())

print(acronyms)