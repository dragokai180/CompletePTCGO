from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ceda869a-8e3b-5fe0-8de3-ad58b94eec3e',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Seviper.Name',
    display_name='Seviper',
    searchable_by=['Seviper', 'Basic', 'Seviper'],
    subtypes=['Basic'],
    collector_number=46,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=336,
    abilities=[
        Ability(
            title='More Poison',
            game_text="Put 1 more damage counter on your opponent's Poisoned Pokémon between turns.",
            effect=standard_ability,
            trigger=Triggers.BETWEEN_TURNS,
        ),
        Attack(
            title='Venomous Fang',
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
