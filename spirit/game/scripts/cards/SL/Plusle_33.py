from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d77734e9-0084-5a36-a63e-25d5a483d010',
    key='SL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Plusle.Name',
    display_name='Plusle',
    searchable_by=['Plusle', 'Basic', 'Plusle'],
    subtypes=['Basic'],
    collector_number=33,
    set_code='SL',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=311,
    abilities=[
        Attack(
            title='Tag Team Boost',
            game_text='If Minun is on your Bench, this attack does 50 more damage.',
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
