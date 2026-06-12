# DND 5e CR versus player calculator

## description
used to calculate combat difficulty in dungeons

## important spreadsheet updater files
* ```interpret_markdown_stat_block.py```
  * this makes python files that are dictionaries which can then be modified further or updated into the spreadsheet database. which is both a .csv and .tsv file
* ```spreadsheet_enums.py```
  * these are enums for both the spreadsheet's keys, as well as certain close ended values a key can have. Like monster type or font
* ```convert_csv_file_into_tsv_file.py```
* ```update_encoutner_feedback_spreadsheet.py```
* ```update_homebrew_monster_spreadsehet.py```
* ```get_encounter_difficulty_from_cr_values.py```
  * this ia a derivative of the "get_enouncter_difficulty_from_xp_values" because xp values are necessary, but i call CR much mor often than i do xp
* ```print_dictionary_nicely.py```
* ```print_encounter_difficulty_concisely.py```

## custom monster to cr and spreadsheet pipline
1. make stat block on google docs using the recommended template monster
2. download stat block as .md file
3. go to ```interpret_markdown_stat_block.py``` and code it to hook up and "dictionar-ify" your Markdown file
   1. this will come with it's own ```if __name__ == "__main__"``` helper function that updates it's cr and cr helper values
   2. run the file to update the CR and the CR helper values
4. run ```convert_csv_file_into_tsv_file.py```
5. open file explorer to the .tsv file
6. cntrl + A 
7. cntrl + C
8. go to your .tsv file on google sheets
9. cntrl + A
10. cntrl + V
11. the update cycle has finished. 

## major TODOS
```pycon
#TODO: make the databse be in .tsv instead of .csv
#TODO: consult a clanker on if that would be a good idea or not
```
to plug cells from pycharm into google sheets withotu making  
a whole new file you need the file to be separated by tabs, not commas.  

so that has me thinking we just have it one way. just .tsv.