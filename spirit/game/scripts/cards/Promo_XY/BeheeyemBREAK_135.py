from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3cd637f2-1e79-5c0c-8a22-54d6c7e4b1c7',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.BeheeyemBREAK.Name',
    display_name='Beheeyem BREAK',
    searchable_by=['Beheeyem BREAK', 'BREAK', 'BeheeyemBREAK'],
    subtypes=['BREAK'],
    collector_number=135,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Beheeyem.Name',
    family_id=606,
    abilities=[
        Attack(
            title='Cosmic Circle',
            game_text='Move as many Psychic Energy attached to your Pokémon to your other Pokémon in any way you like.',
            cost={PokemonTypes.PSYCHIC: 3},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
