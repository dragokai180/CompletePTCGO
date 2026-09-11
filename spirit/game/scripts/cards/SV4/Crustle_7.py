from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='20682f78-2497-5e39-9080-875eb5b8e838',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Crustle.Name',
    display_name='Crustle',
    searchable_by=['Crustle', 'Stage 1', 'Crustle'],
    subtypes=['Stage 1'],
    collector_number=7,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Dwebble.Name',
    family_id=557,
    abilities=[
        Attack(
            title='Confront',
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title='Crag Bash',
            game_text="During your opponent's next turn, this Pokémon takes 100 less damage from attacks from Evolution Pokémon (after applying Weakness and Resistance).",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
