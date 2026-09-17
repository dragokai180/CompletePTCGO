from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bed91645-0fba-5e32-a887-8f2faff9ef05',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MowRotom.Name',
    display_name='Mow Rotom',
    searchable_by=['Mow Rotom', 'Basic', 'MowRotom'],
    subtypes=['Basic'],
    collector_number=14,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=479,
    abilities=[
        Ability(
            title='Roto Motor',
            game_text="If you have 9 or more Pokémon Tool cards in your discard pile, ignore all Energy in the attack cost of each of this Pokémon's attacks.",
            effect=standard_ability,
        ),
        Attack(
            title='Special Mow',
            game_text="Discard a Special Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
