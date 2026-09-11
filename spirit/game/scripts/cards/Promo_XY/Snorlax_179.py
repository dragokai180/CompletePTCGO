from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d6f40549-8270-5144-bfcd-9dfedb09e011',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Snorlax.Name',
    display_name='Snorlax',
    searchable_by=['Snorlax', 'Basic', 'Snorlax'],
    subtypes=['Basic'],
    collector_number=179,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=143,
    abilities=[
        Ability(
            title='Immunity',
            game_text="This Pokémon can't be affected by any Special Conditions. (Remove any Special Conditions affecting this Pokémon.)",
            passive=standard_passive("This Pokémon can't be affected by any Special Conditions. (Remove any Special Conditions affecting this Pokémon.)"),
        ),
        Attack(
            title='Body Slam',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
