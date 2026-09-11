from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3d5f1a5b-d016-5c03-b005-2eb98b746e31',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MBeedrillEX.Name',
    display_name='M Beedrill-EX',
    searchable_by=['M Beedrill-EX', 'MEGA', 'EX', 'MBeedrillEX'],
    subtypes=['MEGA', 'EX'],
    collector_number=158,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=200,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.BeedrillEX.Name',
    family_id=15,
    abilities=[
        Attack(
            title='Hazard Stinger',
            game_text="Discard all Energy attached to this Pokémon. Your opponent's Active Pokémon is now Paralyzed and Poisoned. Put 4 damage counters instead of 1 on that Pokémon between turns.",
            cost={PokemonTypes.GRASS: 2},
            damage=40,
            effect=standard_attack,
        ),
    ],
)
