from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7474acc6-a814-562c-af73-96de2f2aa9b8',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Carnivine.Name',
    display_name='Carnivine',
    searchable_by=['Carnivine', 'Basic', 'Carnivine'],
    subtypes=['Basic'],
    collector_number=12,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=455,
    abilities=[
        Attack(
            title='Chomp Chomp',
            game_text='Heal 20 damage from this Pokémon.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Loom Over',
            game_text='This attack does 10 less damage for each damage counter on this Pokémon.',
            cost={PokemonTypes.GRASS: 2},
            damage=90,
            damage_operator='-',
            effect=standard_attack,
        ),
    ],
)
