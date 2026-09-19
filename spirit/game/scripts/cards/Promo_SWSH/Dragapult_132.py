from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4b43ff10-fe1f-5903-8708-411a8e125774',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dragapult.Name',
    display_name='Dragapult',
    searchable_by=['Dragapult', 'Stage 2', 'Prime', 'Dragapult'],
    subtypes=['Stage 2', 'Prime'],
    collector_number=132,
    set_code='Promo_SWSH',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=150,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    attributes={200790: {'type': 'string', 'value': 'SWSH132'}},
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Drakloak.Name',
    family_id=885,
    abilities=[
        Attack(
            title='Mach Turn',
            game_text='You may switch this Pokémon with 1 of your Benched Pokémon.',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=60,
            effect=standard_attack,
        ),
        Attack(
            title='Diving Swipe',
            game_text="Discard a random card from your opponent's hand.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=standard_attack,
        ),
    ],
)
