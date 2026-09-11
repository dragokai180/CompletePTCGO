from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d8692c9d-8051-5c1f-ba6a-4c1e84ee2a18',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sandslash.Name',
    display_name='Sandslash',
    searchable_by=['Sandslash', 'Stage 1', 'Sandslash'],
    subtypes=['Stage 1'],
    collector_number=28,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Sandshrew.Name',
    family_id=27,
    abilities=[
        Attack(
            title='Rumble',
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Spike Rend',
            game_text="If your opponent's Active Pokémon already has any damage counters on it, this attack does 100 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
