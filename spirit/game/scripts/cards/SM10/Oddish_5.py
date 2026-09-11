from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='219f8c3c-bef8-5c52-82f8-cc69bb915854',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Oddish.Name',
    display_name='Oddish',
    searchable_by=['Oddish', 'Basic', 'Oddish'],
    subtypes=['Basic'],
    collector_number=5,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=43,
    abilities=[
        Attack(
            title='Stun Spore',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Seed Bomb',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
