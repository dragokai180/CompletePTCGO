from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3fe533d2-cbc3-5384-b0be-eba42cb313c4',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Celebi.Name',
    display_name='Celebi',
    searchable_by=['Celebi', 'Basic', 'Celebi'],
    subtypes=['Basic'],
    collector_number=93,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=251,
    abilities=[
        Ability(
            title='Leap Through Time',
            game_text="When this Pokémon is Knocked Out, flip a coin. If heads, shuffle this Pokémon and all cards attached to it into your deck, and your opponent can't take any Prize cards for it.",
            effect=standard_ability,
            trigger=Triggers.ON_KNOCKED_OUT,
        ),
        Attack(
            title='Sparkle Motion',
            game_text="Put 1 damage counter on each of your opponent's Pokémon.",
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
    ],
    passive=standard_passive("Prevent all effects of your opponent's Pokémon's Abilities done to this Pokémon."),
)
