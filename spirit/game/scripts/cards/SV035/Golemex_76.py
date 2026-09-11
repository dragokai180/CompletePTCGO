from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='724bbb1d-9ea0-59ea-a6c1-cdb23bf0981a',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Golemex.Name',
    display_name='Golem ex',
    searchable_by=['Golem ex', 'Stage 2', 'ex', 'Golemex'],
    subtypes=['Stage 2', 'ex'],
    collector_number=76,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=330,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Graveler.Name',
    family_id=74,
    abilities=[
        Attack(
            title='Dynamic Roll',
            game_text="During your next turn, attacks used by this Pokémon do 120 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).",
            cost={PokemonTypes.FIGHTING: 1},
            damage=50,
            effect=standard_attack,
        ),
        Attack(
            title='Rock Blaster',
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=180,
            effect=standard_attack,
        ),
    ],
)
