# DND 5e CR versus player calculator

## cataclysmic TODO
```pycon
#TODO: i'm discontinuing the encounter difficulty calculator becuase of the following reasons 1. it's not accurage, things rated as deadly ahve been easy for ages now. 2. it's not sustainable. 3. fuck piss dick fuck piss dick fuck.
"""
while the encounters themselves are not going to be
 updated unless i'm neurotic enough to update them
  and their master spreadsheet anyway. i will still 
  have combat calculators and some computer minigames 
  if i have free time.
  
in this edict there's the issue that i'm gonna be updating the monster stat block haphazardly
ergo- ad-hacally. 
    fucking tech bro vocab...
so in that i'm going to have to make a decision if there's gonna be phase 1 or phase 2 calculus monsters.
and as of now, i'd rather give myself a punch in the face that make decisions

so again. haphazard updating. 
"""
```

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
#TODO: make the database be in .tsv instead of .csv
#TODO: consult a clanker on if that would be a good idea or not
```
to plug cells from pycharm into google sheets withotu making  
a whole new file you need the file to be separated by tabs, not commas.  

so that has me thinking we just have it one way. just .tsv.

```pycon
#TODO: make a more advanced combat simulator that takes in-game difficulty statistics for me so i can manually and algorithmically analyzer encounters.
```
technically i discontinued the whole prediction of difficulty encounters feature but if i were want to start it again i would need data to create the algorithm with. 
Currently the one i have was vibe coded by Codex and it says it got the idea from teh wizards of the coast algorithm from their book.
Idk if it's having a clanker moment and i don't care to find out :-/ 