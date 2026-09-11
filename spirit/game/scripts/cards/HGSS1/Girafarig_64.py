from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='13dfb921-f553-5ae5-a928-ad2272c5c197',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Girafarig.Name',
    display_name='Girafarig',
    searchable_by=['Girafarig', 'Basic', 'Girafarig'],
    subtypes=['Basic'],
    collector_number=64,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=203,
    abilities=[
        Attack(
            title='Show Off',
            game_text='Search your deck for up to 2 basic Energy cards, show them to your opponent, and put them into your hand. Shuffle your deck afterward.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Psyshot',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
