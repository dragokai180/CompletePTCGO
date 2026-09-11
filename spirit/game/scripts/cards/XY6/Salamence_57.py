from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e45a4374-b08b-5bf7-aac3-f0193dc09c9f',
    key='XY6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Salamence.Name',
    display_name='Salamence',
    searchable_by=['Salamence', 'Stage 2', 'Salamence'],
    subtypes=['Stage 2'],
    collector_number=57,
    set_code='XY6',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Shelgon.Name',
    family_id=371,
    abilities=[
        Attack(
            title='Shatter',
            game_text='Discard any Stadium card in play.',
            cost={PokemonTypes.FIRE: 1},
            damage=60,
            effect=standard_attack,
        ),
        Attack(
            title='Power Howl',
            game_text="This attack does 20 damage times the number of cards in your opponent's hand.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Steam Blast',
            game_text='Discard 3 Energy attached to this Pokémon.',
            cost={PokemonTypes.FIRE: 2, PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=170,
            effect=standard_attack,
        ),
    ],
)
