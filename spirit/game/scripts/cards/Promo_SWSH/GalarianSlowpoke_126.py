from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4fa51737-a969-550e-a30e-650104fbd7f8',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.GalarianSlowpoke.Name',
    display_name='Galarian Slowpoke',
    searchable_by=['Galarian Slowpoke', 'Basic', 'GalarianSlowpoke'],
    subtypes=['Basic'],
    collector_number=126,
    set_code='Promo_SWSH',
    regulation_mark='E',
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    attributes={200790: {'type': 'string', 'value': 'SWSH126'}},
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=79,
    abilities=[
        Attack(
            title='Everyone Laze Around',
            game_text='Heal 10 damage from each of your Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Tail Whap',
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
        ),
    ],
)
