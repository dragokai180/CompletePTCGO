from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='674560c8-db58-5bb9-8cf6-db0b0322f7e9',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lunala.Name',
    display_name='Lunala ◇',
    searchable_by=['Lunala ◇', 'Basic', 'Prism Star', 'Lunala'],
    subtypes=['Basic', 'Prism Star'],
    collector_number=62,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Prism,
    hp=160,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=792,
    abilities=[
        Attack(
            title='Full Moon Star',
            game_text="For each of your opponent's Pokémon in play, attach a Psychic Energy card from your discard pile to your Pokémon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Psystorm',
            game_text='This attack does 20 damage times the amount of Energy attached to all Pokémon.',
            cost={PokemonTypes.PSYCHIC: 4},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
