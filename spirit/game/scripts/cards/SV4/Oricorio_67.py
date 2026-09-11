from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='51d019a0-0f33-5836-8a56-9c8772ac6070',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Oricorio.Name',
    display_name='Oricorio',
    searchable_by=['Oricorio', 'Basic', 'Oricorio'],
    subtypes=['Basic'],
    collector_number=67,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=741,
    abilities=[
        Attack(
            title='Pep Up',
            game_text="Shuffle your hand into your deck. Then, draw a card for each Benched Pokémon (both yours and your opponent's).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Volt Wave',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
