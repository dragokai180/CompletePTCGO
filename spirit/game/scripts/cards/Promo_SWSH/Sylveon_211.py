from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e24d0209-4dbd-5614-b474-ec994d422837',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sylveon.Name',
    display_name='Sylveon',
    searchable_by=['Sylveon', 'Stage 1', 'Sylveon'],
    subtypes=['Stage 1'],
    collector_number=211,
    set_code='Promo_SWSH',
    regulation_mark='E',
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    attributes={200790: {'type': 'string', 'value': 'SWSH211'}},
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name',
    family_id=133,
    abilities=[
        Attack(
            title='Time Out Kick',
            game_text="You may put an Energy attached to your opponent's Active Pokémon into their hand.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Symphony Whip',
            game_text='If you played a Supporter card from your hand during this turn, this attack does 70 more damage.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
