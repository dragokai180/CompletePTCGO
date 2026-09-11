from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9525dcfb-8cb9-586a-9023-c563faef90b6',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Seismitoad.Name',
    display_name='Seismitoad',
    searchable_by=['Seismitoad', 'Stage 2', 'Seismitoad'],
    subtypes=['Stage 2'],
    collector_number=52,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=170,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Palpitoad.Name',
    family_id=535,
    abilities=[
        Ability(
            title='Quaking Zone',
            game_text="As long as this Pokémon is in the Active Spot, attacks used by your opponent's Active Pokémon cost Colorless more.",
            passive=standard_passive("As long as this Pokémon is in the Active Spot, attacks used by your opponent's Active Pokémon cost Colorless more."),
        ),
        Attack(
            title='Echoed Voice',
            game_text="During your next turn, this Pokémon's Echoed Voice attack does 100 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.WATER: 2},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
