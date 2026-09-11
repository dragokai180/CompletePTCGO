from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d99d9681-38d2-5a26-9c27-b00dfad97b1d',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Hitmonchan.Name',
    display_name='Hitmonchan',
    searchable_by=['Hitmonchan', 'Basic', 'Hitmonchan'],
    subtypes=['Basic'],
    collector_number=107,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=107,
    abilities=[
        Ability(
            title='Counterattack',
            game_text="If this Pokémon is in the Active Spot and is damaged by an attack from your opponent's Pokémon (even if this Pokémon is Knocked Out), put 3 damage counters on the Attacking Pokémon.",
            effect=standard_ability,
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
        ),
        Attack(
            title='Excited Punch',
            game_text="During your next turn, this Pokémon's Excited Punch attack does 60 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.FIGHTING: 2},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
