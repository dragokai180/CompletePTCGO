from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='237d661f-0571-58a7-990b-70fde405120b',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tangela.Name',
    display_name='Tangela',
    searchable_by=['Tangela', 'Basic', 'Tangela'],
    subtypes=['Basic'],
    collector_number=16,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=114,
    abilities=[
        Attack(
            title='Tangle Drag',
            game_text="Switch 1 of your opponent's Benched Pokémon with their Active Pokémon.",
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Gentle Slap',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
