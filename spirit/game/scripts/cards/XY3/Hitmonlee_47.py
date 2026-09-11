from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5731512a-c45c-5acb-9740-45db6659d285',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Hitmonlee.Name',
    display_name='Hitmonlee',
    searchable_by=['Hitmonlee', 'Basic', 'Hitmonlee'],
    subtypes=['Basic'],
    collector_number=47,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=106,
    abilities=[
        Attack(
            title='Stretch Kick',
            game_text="This attack does 30 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIGHTING: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Spiral Kick',
            cost={PokemonTypes.FIGHTING: 2},
            damage=30,
        ),
    ],
)
