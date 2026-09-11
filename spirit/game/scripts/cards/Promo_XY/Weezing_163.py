from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ba7a314d-c204-56b4-813b-ceb8dd24e5aa',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Weezing.Name',
    display_name='Weezing',
    searchable_by=['Weezing', 'Stage 1', 'Weezing'],
    subtypes=['Stage 1'],
    collector_number=163,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Koffing.Name',
    family_id=110,
    abilities=[
        Ability(
            title='Levitate',
            game_text='If this Pokémon has any Energy attached to it, this Pokémon has no Retreat Cost.',
            passive=standard_passive('If this Pokémon has any Energy attached to it, this Pokémon has no Retreat Cost.'),
        ),
        Attack(
            title='Smokescreen',
            game_text="If the Defending Pokémon tries to attack during your opponent's next turn, your opponent flips a coin. If tails, that attack does nothing.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
