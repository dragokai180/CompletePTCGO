from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='462485ff-66ed-5d8c-a4fb-8fbd8cbf0c0b',
    key='XY0',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Weedle.Name',
    display_name='Weedle',
    searchable_by=['Weedle', 'Basic', 'Weedle'],
    subtypes=['Basic'],
    collector_number=1,
    set_code='XY0',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=13,
    abilities=[
        Attack(
            title='String Shot',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
