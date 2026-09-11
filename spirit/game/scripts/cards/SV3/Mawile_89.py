from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4de458b1-5a02-5503-bcf2-57a5276fa07c',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mawile.Name',
    display_name='Mawile',
    searchable_by=['Mawile', 'Basic', 'Mawile'],
    subtypes=['Basic'],
    collector_number=89,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=303,
    abilities=[
        Attack(
            title='Mischievous Crunch',
            game_text='This attack does 30 damage for each Psychic Energy attached to this Pokémon.',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
