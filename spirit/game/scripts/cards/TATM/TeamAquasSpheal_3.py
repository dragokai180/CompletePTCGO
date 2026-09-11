from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0746b827-e893-5ff8-a6b6-c597bfdb8e87',
    key='TATM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasSpheal.Name',
    display_name="Team Aqua's Spheal",
    searchable_by=["Team Aqua's Spheal", 'Basic', 'TeamAquasSpheal'],
    subtypes=['Basic'],
    collector_number=3,
    set_code='TATM',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=363,
    abilities=[
        Attack(
            title='Water Gun',
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)
