from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ac215469-e2c6-5dc3-b74d-7f2df0b3c97b',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Heracross.Name',
    display_name='Heracross',
    searchable_by=['Heracross', 'Basic', 'Heracross'],
    subtypes=['Basic'],
    collector_number=6,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=214,
    abilities=[
        Attack(
            title='Tackle',
            cost={PokemonTypes.GRASS: 2},
            damage=50,
        ),
        Attack(
            title='Smashing Horn',
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.GRASS: 3},
            damage=110,
            effect=standard_attack,
        ),
    ],
)
