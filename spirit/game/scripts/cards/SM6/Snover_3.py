from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7fafa0ec-4ea1-5453-9710-073353b79460',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Snover.Name',
    display_name='Snover',
    searchable_by=['Snover', 'Basic', 'Snover'],
    subtypes=['Basic'],
    collector_number=3,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=459,
    abilities=[
        Attack(
            title='Ice Shard',
            game_text="If your opponent's Active Pokémon is a Fighting Pokémon, this attack does 40 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
