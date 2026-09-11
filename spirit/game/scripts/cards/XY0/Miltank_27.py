from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5df010d2-c01d-512a-bf6e-4888bc5d6b2b',
    key='XY0',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Miltank.Name',
    display_name='Miltank',
    searchable_by=['Miltank', 'Basic', 'Miltank'],
    subtypes=['Basic'],
    collector_number=27,
    set_code='XY0',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=241,
    abilities=[
        Attack(
            title='Sitdown Splash',
            game_text='Flip a coin. If heads, this attack does 20 more damage.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
