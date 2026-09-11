from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2f9e240f-bce6-5374-8735-78a6832d3e91',
    key='TATM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasPoochyena.Name',
    display_name="Team Magma's Poochyena",
    searchable_by=["Team Magma's Poochyena", 'Basic', 'TeamMagmasPoochyena'],
    subtypes=['Basic'],
    collector_number=17,
    set_code='TATM',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=261,
    abilities=[
        Attack(
            title='Infiltrate',
            game_text='Your opponent reveals his or her hand.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Bite',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
