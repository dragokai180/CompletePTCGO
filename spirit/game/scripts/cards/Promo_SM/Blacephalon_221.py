from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4b901b8f-0f4a-5b7b-b093-4412380ae085',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Blacephalon.Name',
    display_name='Blacephalon',
    searchable_by=['Blacephalon', 'Basic', 'Ultra Beast', 'Blacephalon'],
    subtypes=['Basic', 'Ultra Beast'],
    collector_number=221,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=806,
    abilities=[
        Attack(
            title='Fireworks Bomb',
            game_text="Put 4 damage counters on your opponent's Pokémon in any way you like. If your opponent has exactly 3 Prize cards remaining, put 12 damage counters on them instead.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
