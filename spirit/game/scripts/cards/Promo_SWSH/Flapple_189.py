from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='48c0318c-68d3-5e34-8869-45c2b0fae48a',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Flapple.Name',
    display_name='Flapple',
    searchable_by=['Flapple', 'Stage 1', 'Flapple'],
    subtypes=['Stage 1'],
    collector_number=189,
    set_code='Promo_SWSH',
    regulation_mark='E',
    rarity=Rarities.RarePromo,
    hp=80,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    attributes={200790: {'type': 'string', 'value': 'SWSH189'}},
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Applin.Name',
    family_id=840,
    abilities=[
        Attack(
            title='Flight Up',
            game_text='Attach up to 3 basic Energy cards from your discard pile to 1 of your Benched Pokémon.',
            cost={PokemonTypes.FIRE: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Corrosive Acid',
            game_text="Your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.FIRE: 1},
            damage=70,
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.swsh_promos import configure_promo
configure_promo(card)
