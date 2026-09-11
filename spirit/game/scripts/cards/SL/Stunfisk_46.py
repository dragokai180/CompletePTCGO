from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c0fb9ae4-00f7-5db4-a266-b6bfb01bdf71',
    key='SL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Stunfisk.Name',
    display_name='Stunfisk',
    searchable_by=['Stunfisk', 'Basic', 'Stunfisk'],
    subtypes=['Basic'],
    collector_number=46,
    set_code='SL',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=618,
    abilities=[
        Attack(
            title='Thunder Shock',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Head Bolt',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)
