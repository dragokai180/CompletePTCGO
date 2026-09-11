from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3622cb19-ccbd-52da-a2e9-4a0de845d097',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bergmite.Name',
    display_name='Bergmite',
    searchable_by=['Bergmite', 'Basic', 'Bergmite'],
    subtypes=['Basic'],
    collector_number=29,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=712,
    abilities=[
        Attack(
            title='Break Open',
            game_text="If your opponent has a Stadium card in play, discard it. If you do, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
