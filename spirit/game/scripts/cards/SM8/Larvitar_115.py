from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6c519ee0-361a-5a27-be6e-6ab871a01496',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Larvitar.Name',
    display_name='Larvitar',
    searchable_by=['Larvitar', 'Basic', 'Larvitar'],
    subtypes=['Basic'],
    collector_number=115,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=246,
    abilities=[
        Attack(
            title='Second Strike',
            game_text="If your opponent's Active Pokémon already has 3 or more damage counters on it, this attack does 70 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
