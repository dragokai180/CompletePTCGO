from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='993cfffa-fedf-54af-a823-2b01b79abb8b',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Shellder.Name',
    display_name='Shellder',
    searchable_by=['Shellder', 'Basic', 'Shellder'],
    subtypes=['Basic'],
    collector_number=23,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=90,
    abilities=[
        Attack(
            title='Clamp',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed. If tails, this attack does nothing.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
