from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='15654150-8a3f-51c1-8d99-d9886bdfc225',
    key='TATM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasGrimer.Name',
    display_name="Team Aqua's Grimer",
    searchable_by=["Team Aqua's Grimer", 'Basic', 'TeamAquasGrimer'],
    subtypes=['Basic'],
    collector_number=7,
    set_code='TATM',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=88,
    abilities=[
        Attack(
            title='Pound',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
        Attack(
            title='Mud-Slap',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
