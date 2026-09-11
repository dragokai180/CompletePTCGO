from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='01f31d03-afe3-52e6-bfb5-985e1d6555f5',
    key='XY6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gligar.Name',
    display_name='Gligar',
    searchable_by=['Gligar', 'Basic', 'Gligar'],
    subtypes=['Basic'],
    collector_number=36,
    set_code='XY6',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=207,
    abilities=[
        Attack(
            title='Stun Poison',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed and Poisoned.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
