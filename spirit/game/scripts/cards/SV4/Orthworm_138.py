from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b8ad65cb-9667-5bea-a7ac-fc55f65041d3',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Orthworm.Name',
    display_name='Orthworm',
    searchable_by=['Orthworm', 'Basic', 'Orthworm'],
    subtypes=['Basic'],
    collector_number=138,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=968,
    abilities=[
        Attack(
            title='Punch and Draw',
            game_text='Draw 2 cards.',
            cost={PokemonTypes.METAL: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Crunch-Time Rush',
            game_text='If there are 3 or fewer cards in your deck, this attack does 150 more damage.',
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
