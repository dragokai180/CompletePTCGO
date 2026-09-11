from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='36915c51-45df-59d5-ad00-d3e59eead2c0',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Xerneas.Name',
    display_name='Xerneas',
    searchable_by=['Xerneas', 'Basic', 'Xerneas'],
    subtypes=['Basic'],
    collector_number=107,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=716,
    abilities=[
        Attack(
            title='Rainbow Force',
            game_text='This attack does 30 more damage for each different type of Pokémon on your Bench.',
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Power Creation',
            game_text='If this Pokémon was healed during this turn, this attack does 80 more damage.',
            cost={PokemonTypes.FAIRY: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
