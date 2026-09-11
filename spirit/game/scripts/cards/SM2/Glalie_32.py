from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='46d4d965-63c3-54b1-a6e6-4634119c96e4',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Glalie.Name',
    display_name='Glalie',
    searchable_by=['Glalie', 'Stage 1', 'Glalie'],
    subtypes=['Stage 1'],
    collector_number=32,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Snorunt.Name',
    family_id=361,
    abilities=[
        Attack(
            title='Crunch',
            game_text="Flip a coin. If heads, discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.WATER: 2},
            damage=40,
            effect=standard_attack,
        ),
        Attack(
            title='Raging Floe',
            game_text='If this Pokémon has any damage counters on it, this attack does 80 more damage.',
            cost={PokemonTypes.WATER: 3},
            damage=70,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
