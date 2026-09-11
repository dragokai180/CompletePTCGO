from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0b686d2a-a400-5934-9339-10040300f93c',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Torkoal.Name',
    display_name='Torkoal',
    searchable_by=['Torkoal', 'Basic', 'Torkoal'],
    subtypes=['Basic'],
    collector_number=35,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=324,
    abilities=[
        Attack(
            title='Stampede',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title='Concentrated Fire',
            game_text='Flip a coin for each Fire Energy attached to this Pokémon. This attack does 80 damage for each heads.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
