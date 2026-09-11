from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='18a72287-2603-59a2-883f-af81e767d2a4',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bayleef.Name',
    display_name='Bayleef',
    searchable_by=['Bayleef', 'Stage 1', 'Bayleef'],
    subtypes=['Stage 1'],
    collector_number=7,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Chikorita.Name',
    family_id=152,
    abilities=[
        Attack(
            title='Soothing Scent',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Razor Leaf',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)
