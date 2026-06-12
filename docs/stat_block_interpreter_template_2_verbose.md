# Verbose Template Monster 2, Overexplained Parser Trial

This first paragraph is intentionally outside a known section.
The interpreter ignores it.

# metadata

name: Verbose Template Monster 2, Overexplained Parser Trial
cr: ????
url: [Verbose Example Stat Block](https://example.com/verbose-stat-block)
font: DND_5E_CR_versus_player_calculuator
author: Codex
additional: Interpreted from markdown with inferred CR helper values.

# core stats

size: medium
type: humanoid
alignment: neutral evil
hp: 45
ac: 15
speed: 30, fly 40

# ability scores

str_numeric_stat: 8
str_modifier: -1
dex_numeric_stat: 16
dex_modifier: 3
con_numeric_stat: 14
con_modifier: 2
int_numeric_stat: 10
int_modifier: 0
wis_numeric_stat: 12
wis_modifier: 1
cha_numeric_stat: 6
cha_modifier: -2

# saving throws

dex: 5
wis: 3

# skills

acrobatics: 5
stealth: 7
history: -1

# WRI

weak: radiant
resistant: fire, necrotic
immune: poison

# Senses

senses: darkvision 60
passive_perception: 11

# languages

* common
* thieves cant

## cr inputs

These can be omitted or set to 0 when you want the generated Python file to infer them from actions, WRI, and speed.

average_damage: 0
attack_modifier: 0
has_legendary_action: false
legendary_action_damage: 0
has_flight: false
resistance_count: 0
immunity_count: 0
weakness_count: 0
save_dc: 0
is_spellcaster: false
regeneration_per_round: 0
multiattack_count: 0
ability_count: 0
ability_cr_weight: 2
recharge_damage: 0
limited_use_damage: 0
bonus_action_damage: 0

# actions

## action - reliable sword strike

action_type: action
attack_type: melee_attack
hit_modifier: 5
damage: 2d8 + 3
damage_type: slashing
range: 5
notes: This should be considered for average_damage.

## action - weaker thrown dagger

action_type: action
attack_type: ranged_attack
hit_modifier: 5
damage: 1d4 + 3
damage_type: piercing
range: 20
notes: The interpreter should prefer the stronger normal action above.

## bonus action - wing clip

action_type: bonus action
attack_type: melee_attack
hit_modifier: 5
damage: 1d6 + 3
damage_type: slashing
range: 5
notes: This should become bonus_action_damage.

## rechargeable action - acid burst

action_type: rechargeable action
attack_type: saving_throw
save_dc: 13
save_stat: dex
damage: 4d6
damage_type: acid
range: 30
notes: This should become recharge_damage and save_dc.

## limited use reaction - spiteful spark

action_type: limited use reaction
attack_type: saving_throw
save_dc: 13
save_stat: wis
damage: 2d6
damage_type: lightning
range: 30
notes: This should become limited_use_damage.

## passive - mean aura

action_type: passive
attack_type: utility
range: 10
notes: This has no damage, so it can count as a utility ability.

# jokes i refuse to delete

parser_mood: deeply suspicious
This section is intentionally ignored.

# lore

Put freeform monster description here. The interpreter should not try to understand this section.

# math description

Use this section for your calculus creature explanations, puzzle notes, or DM-only context.
