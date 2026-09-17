from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a4e360d8-bae8-5574-99d3-4f28cf5e8133',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.FrostRotom.Name',
    display_name='Frost Rotom',
    searchable_by=['Frost Rotom', 'Basic', 'FrostRotom'],
    subtypes=['Basic'],
    collector_number=41,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=479,
    abilities=[
        Ability(
            title='Roto Motor',
            game_text="If you have 9 or more Pokémon Tool cards in your discard pile, ignore all Energy in the attack cost of each of this Pokémon's attacks.",
            effect=standard_ability,
        ),
        Attack(
            title='Frost Crush',
            game_text="This attack does 20 more damage times the amount of Energy attached to all of your opponent's Pokémon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
