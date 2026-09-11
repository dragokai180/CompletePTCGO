from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='cd799952-d118-5156-b9df-f4076dee6a2f',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Masquerain.Name',
    display_name='Masquerain',
    searchable_by=['Masquerain', 'Stage 1', 'Masquerain'],
    subtypes=['Stage 1'],
    collector_number=14,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Surskit.Name',
    family_id=283,
    abilities=[
        Attack(
            title='Spiral Gyration',
            game_text="Your opponent's Active Pokémon is now Confused. Switch this Pokémon with 1 of your Benched Pokémon.",
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Air Slash',
            game_text='Discard an Energy attached to this Pokémon.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
