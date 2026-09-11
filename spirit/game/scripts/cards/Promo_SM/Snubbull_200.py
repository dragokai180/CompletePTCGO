from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2fb4af3e-05bd-5071-9479-113a6a8407b6',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Snubbull.Name',
    display_name='Snubbull',
    searchable_by=['Snubbull', 'Basic', 'Snubbull'],
    subtypes=['Basic'],
    collector_number=200,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=209,
    abilities=[
        Attack(
            title='Bite',
            cost={PokemonTypes.FAIRY: 1},
            damage=10,
        ),
        Attack(
            title='Paralyzing Gaze',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
    ],
)
