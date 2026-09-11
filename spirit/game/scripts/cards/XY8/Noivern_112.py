from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9701fb86-7c4a-5c4d-a9ae-3066a9c065dd',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Noivern.Name',
    display_name='Noivern',
    searchable_by=['Noivern', 'Stage 1', 'Noivern'],
    subtypes=['Stage 1'],
    collector_number=112,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Noibat.Name',
    family_id=714,
    abilities=[
        Attack(
            title='Tuning',
            game_text="Shuffle your hand into your deck. Then, draw a number of cards equal to the number of cards in your opponent's hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Air Slash',
            game_text='Discard an Energy attached to this Pokémon.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
