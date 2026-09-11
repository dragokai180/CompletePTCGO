from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2dc8c997-7dd3-5297-a80f-4c7dce6041ca',
    key='XY7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MachampEX.Name',
    display_name='Machamp-EX',
    searchable_by=['Machamp-EX', 'Basic', 'EX', 'MachampEX'],
    subtypes=['Basic', 'EX'],
    collector_number=37,
    set_code='XY7',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=68,
    abilities=[
        Attack(
            title='Steaming Mad',
            game_text='This attack does 20 damage times the number of damage counters on this Pokémon. This Pokémon is now Confused.',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Crazy Hammer',
            game_text='If this Pokémon is affected by a Special Condition, this attack does 80 more damage. Then, remove all Special Conditions from this Pokémon.',
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
