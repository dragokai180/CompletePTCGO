from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4b875cdf-d0c3-5eab-bb9d-ae1f452fd131',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Trevenant.Name',
    display_name='Trevenant',
    searchable_by=['Trevenant', 'Stage 1', 'Trevenant'],
    subtypes=['Stage 1'],
    collector_number=12,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Phantump.Name',
    family_id=708,
    abilities=[
        Ability(
            title='Forest Miasma',
            game_text="During Pokémon Checkup, if this Pokémon is in the Active Spot, put 1 damage counter on your opponent's Active Pokémon.",
            effect=standard_ability,
            trigger=Triggers.BETWEEN_TURNS,
        ),
        Attack(
            title='Lock Up',
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
