from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='51828f4d-b3a1-55d9-8f9a-a2908109d60e',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Oranguru.Name',
    display_name='Oranguru',
    searchable_by=['Oranguru', 'Basic', 'Oranguru'],
    subtypes=['Basic'],
    collector_number=48,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=765,
    abilities=[
        Attack(
            title='Fixer of the Forest',
            game_text='Put 3 Pokémon Tool cards from your discard pile into your hand.',
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Zen Headbutt',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)
