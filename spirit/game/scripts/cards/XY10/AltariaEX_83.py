from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f05b2223-b1f6-5ef6-951d-e7f65141eebc',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AltariaEX.Name',
    display_name='Altaria-EX',
    searchable_by=['Altaria-EX', 'Basic', 'EX', 'AltariaEX'],
    subtypes=['Basic', 'EX'],
    collector_number=83,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=334,
    abilities=[
        Attack(
            title='Powerful Gain',
            game_text='If this Pokémon was healed during this turn, this attack does 60 more damage and heal 30 damage from this Pokémon.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Shining Wind',
            game_text="During your opponent's next turn, this Pokémon has no Weakness.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
