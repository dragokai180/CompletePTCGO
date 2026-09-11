from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='94b6ab43-268c-514e-88d5-f77713fa7109',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Houndstone.Name',
    display_name='Houndstone',
    searchable_by=['Houndstone', 'Stage 1', 'Houndstone'],
    subtypes=['Stage 1'],
    collector_number=101,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Greavard.Name',
    family_id=971,
    abilities=[
        Attack(
            title='Rear Kick',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title='Two Four-ocious',
            game_text='If your opponent has exactly 2 or 4 Prize cards remaining, this attack does 120 more damage.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
