def print_encounter_difficulty_concisely(dict_in_question,
                                         tab_amount="\t"):
    print(tab_amount,"print_encounter_difficulty_concisely")
    tab_amount += "\t"
    print(tab_amount,"encounter_name :",dict_in_question["encounter_name"])
    print(tab_amount,"predicted_difficulty :",dict_in_question["predicted_difficulty"])
    print(tab_amount,"monster_count :",dict_in_question["monster_count"])
    print(tab_amount,"adjusted_xp :",dict_in_question["adjusted_xp"])
    print(tab_amount,"party_thresholds :",dict_in_question["party_thresholds"])