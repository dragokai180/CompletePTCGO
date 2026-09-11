from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1250a603-7206-5f86-aaef-0030e6f66fd2',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Purrloin.Name',
    display_name='Purrloin',
    searchable_by=['Purrloin', 'Basic', 'Purrloin'],
    subtypes=['Basic'],
    collector_number=114,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=509,
    abilities=[
        Attack(
            title='Stampede',
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
        ),
        Attack(
            title='Cat Kick',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
