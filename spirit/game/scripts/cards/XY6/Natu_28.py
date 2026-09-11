from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='721ef39d-0f49-530e-b963-8dd9c3cf32e9',
    key='XY6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Natu.Name',
    display_name='Natu',
    searchable_by=['Natu', 'Basic', 'Natu'],
    subtypes=['Basic'],
    collector_number=28,
    set_code='XY6',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=177,
    abilities=[
        Attack(
            title='Psywave',
            game_text="This attack does 10 damage times the amount of Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
    passive=standard_passive("If your opponent's Pokémon is Knocked Out by damage from an attack of this Pokémon, take 1 more Prize card."),
)
