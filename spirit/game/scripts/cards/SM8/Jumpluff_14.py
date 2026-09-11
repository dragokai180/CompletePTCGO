from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2d6a6c45-45ea-5c3c-842e-def1e6d966e4',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Jumpluff.Name',
    display_name='Jumpluff',
    searchable_by=['Jumpluff', 'Stage 2', 'Jumpluff'],
    subtypes=['Stage 2'],
    collector_number=14,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Skiploom.Name',
    family_id=187,
    abilities=[
        Attack(
            title='Lost March',
            game_text='This attack does 20 damage for each of your Pokémon, except ◇ (Prism Star) Pokémon, in the Lost Zone.',
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
