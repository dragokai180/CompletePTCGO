from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b85c96f2-ea13-5402-a54f-ce50edba3303',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Diglett.Name',
    display_name='Diglett',
    searchable_by=['Diglett', 'Basic', 'Diglett'],
    subtypes=['Basic'],
    collector_number=103,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=50,
    abilities=[
        Attack(
            title="Hole-Diggin' Noggin",
            game_text='Discard the top card of your deck.',
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
