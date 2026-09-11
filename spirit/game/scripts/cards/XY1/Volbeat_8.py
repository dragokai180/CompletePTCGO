from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f78f51bc-d2bf-55b2-aff4-3fca092828b5',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Volbeat.Name',
    display_name='Volbeat',
    searchable_by=['Volbeat', 'Basic', 'Volbeat'],
    subtypes=['Basic'],
    collector_number=8,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=313,
    abilities=[
        Attack(
            title='Luring Glow',
            game_text="Switch 1 of your opponent's Benched Pokémon with your opponent's Active Pokémon.",
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Signal Beam',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
