from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7a33fd4d-b73d-5f86-854d-920db7b07b63',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MAbsolEX.Name',
    display_name='M Absol-EX',
    searchable_by=['M Absol-EX', 'MEGA', 'EX', 'MAbsolEX'],
    subtypes=['MEGA', 'EX'],
    collector_number=63,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=210,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.AbsolEX.Name',
    family_id=359,
    abilities=[
        Attack(
            title='Disaster Wing',
            game_text="Discard the top card of your opponent's deck. If that card is a Trainer card, this attack does 80 more damage.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
