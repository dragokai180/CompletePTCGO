from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3acc4bad-a40e-5c0c-bf2d-96f710290e08',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Yungoos.Name',
    display_name='Yungoos',
    searchable_by=['Yungoos', 'Basic', 'Yungoos'],
    subtypes=['Basic'],
    collector_number=176,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=734,
    abilities=[
        Attack(
            title='Knock Away',
            game_text='Flip a coin. If heads, this attack does 10 more damage.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
