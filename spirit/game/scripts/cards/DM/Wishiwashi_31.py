from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1da33261-ee3b-512f-874e-13f25519c5ae',
    key='DM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Wishiwashi.Name',
    display_name='Wishiwashi',
    searchable_by=['Wishiwashi', 'Basic', 'Wishiwashi'],
    subtypes=['Basic'],
    collector_number=31,
    set_code='DM',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=746,
    abilities=[
        Ability(
            title='Meet Up',
            game_text="Your Wishiwashi-GX in play get +20 HP, and their attacks do 20 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).",
            passive=standard_passive("Your Wishiwashi-GX in play get +20 HP, and their attacks do 20 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance)."),
        ),
        Attack(
            title='Water Gun',
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
    ],
)
