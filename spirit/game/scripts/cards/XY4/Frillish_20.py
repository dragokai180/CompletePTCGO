from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9d90c9c3-5cc1-55d5-9531-3a2fe1160515',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Frillish.Name',
    display_name='Frillish',
    searchable_by=['Frillish', 'Basic', 'Frillish'],
    subtypes=['Basic'],
    collector_number=20,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=592,
    abilities=[
        Attack(
            title='Confuse Ray',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
    ],
)
