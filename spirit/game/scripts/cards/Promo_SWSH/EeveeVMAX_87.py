from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='062feeb7-2bce-5553-8688-357fbf26787a',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.EeveeVMAX.Name',
    display_name='Eevee VMAX',
    searchable_by=['Eevee VMAX', 'VMAX', 'EeveeVMAX'],
    subtypes=['VMAX'],
    collector_number=87,
    set_code='Promo_SWSH',
    regulation_mark='D',
    rarity=Rarities.RarePromo,
    hp=300,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    attributes={200790: {'type': 'string', 'value': 'SWSH087'}},
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.EeveeV.Name',
    family_id=133,
    abilities=[
        Attack(
            title='G-Max Cuddle',
            game_text="During your opponent's next turn, if the Defending Pokémon tries to attack, your opponent flips a coin. If tails, that attack doesn't happen.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=150,
            effect=standard_attack,
        ),
    ],
)
