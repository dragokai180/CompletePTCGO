from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9e0bc6c8-ca3c-58bb-ab13-2127d7078884',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lugia.Name',
    display_name='Lugia',
    searchable_by=['Lugia', 'Basic', 'Lugia'],
    subtypes=['Basic'],
    collector_number=156,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=120,
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
            title='Gust',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title='Aeroblast',
            game_text='Flip 2 coins. This attack does 20 more damage for each heads.',
            cost={PokemonTypes.COLORLESS: 4},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
