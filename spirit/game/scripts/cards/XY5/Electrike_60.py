from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='61bfd6f4-407e-5946-8745-7477b67732c9',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Electrike.Name',
    display_name='Electrike',
    searchable_by=['Electrike', 'Basic', 'Electrike'],
    subtypes=['Basic'],
    collector_number=60,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=309,
    abilities=[
        Attack(
            title='Thunder Fang',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
    passive=standard_passive('Whenever your opponent plays a Trainer card (excluding Pokémon Tools and Stadium cards), prevent all effects of that card done to this Pokémon.'),
)
