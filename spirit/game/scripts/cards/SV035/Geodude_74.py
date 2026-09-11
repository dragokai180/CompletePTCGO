from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bc169af7-c7b2-50c2-98cb-b02e4ab1427c',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Geodude.Name',
    display_name='Geodude',
    searchable_by=['Geodude', 'Basic', 'Geodude'],
    subtypes=['Basic'],
    collector_number=74,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=74,
    abilities=[
        Attack(
            title='Stiffen',
            game_text="During your opponent's next turn, this Pokémon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.FIGHTING: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Knuckle Punch',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
