# Template Monster, Parser Trial

# metadata

name: Template Monster, Parser Trial
cr: 0.5
url: [Example Stat Block](https://example.com/stat-block)
font: Virasco 2000
author: Shwifty_meme_lord

# core stats

size: small
type: construct
alignment: almost chaos
hp: 13
ac: 12
speed: 30, climb 20

# ability scores

str_numeric_stat: 8
str_modifier: -1

dex_numeric_stat: 14
dex_modifier: 2

con_numeric_stat: 10
con_modifier: 0

int_numeric_stat: 6
int_modifier: -2

wis_numeric_stat: 9
wis_modifier: -1

cha_numeric_stat: 4
cha_modifier: -3

# saving throws

str: -1
dex: 4

# skills

stealth: 4
history: -2

# WRI

weak: radiant
resistant: fire, necrotic
immune: poison

# Senses

passive_perception: 9
senses: darkvision 60

# languages

- common
- thieves cant

## cr inputs

average_damage: 5.5
attack_modifier: 4
has_legendary_action: false
legendary_action_damage: 0
has_flight: false
resistance_count: 2
immunity_count: 1
weakness_count: 1
save_dc: 11
is_spellcaster: false
regeneration_per_round: 0
multiattack_count: 0
ability_count: 1
ability_cr_weight: 2
recharge_damage: 0
limited_use_damage: 6
bonus_action_damage: 1

# actions

## action - test [spark](https://example.com/spark)

action_type: action
attack_type: ranged_spell_attack
hit_modifier: 4
damage: 1d6 + 2
damage_type: fire
range: 60
notes: Link in the action name should become plain text.

## action - bad math shove

action_type: bonus_action
attack_type: saving_throw
save_dc: 11
save_stat: str
damage: 1d4 - 1
damage_type: bludgeoning
range: 5
notes: Negative constants should not scare the parser.

# jokes i refuse to delete

This section is deliberately weird and should be ignored by the interpreter.

chaos_value: bananas

# lore

This monster exists to make sure the parser can ignore creative prose while still reading structured stat data.

# math description

Parser Trial (Definition)
Purpose: Make future stat block parsing less fragile.
