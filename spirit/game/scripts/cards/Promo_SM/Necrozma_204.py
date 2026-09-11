from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4109f69b-f261-59c8-8bed-2080e190560f',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Necrozma.Name',
    display_name='Necrozma',
    searchable_by=['Necrozma', 'Basic', 'Necrozma'],
    subtypes=['Basic'],
    collector_number=204,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=800,
    abilities=[
        Attack(
            title='Barrier Attack',
            game_text="During your opponent's next turn, this Pokémon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Special Laser',
            game_text='If this Pokémon has any Special Energy attached to it, this attack does 60 more damage.',
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
