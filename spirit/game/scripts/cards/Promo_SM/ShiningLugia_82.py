from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='716075ec-3ba0-526f-87bd-7a4193e7cd93',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.ShiningLugia.Name',
    display_name='Shining Lugia',
    searchable_by=['Shining Lugia', 'Basic', 'ShiningLugia'],
    subtypes=['Basic'],
    collector_number=82,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=249,
    abilities=[
        Attack(
            title='Argent Wing',
            game_text="If your opponent's Active Pokémon has an Ability, this attack does 60 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Aero Force',
            game_text='Discard an Energy attached to this Pokémon.',
            cost={PokemonTypes.COLORLESS: 4},
            damage=130,
            effect=standard_attack,
        ),
    ],
)
