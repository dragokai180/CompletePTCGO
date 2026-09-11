from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1dc323ae-fa85-50f0-bcf1-4fd614eebb63',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Darmanitan.Name',
    display_name='Darmanitan',
    searchable_by=['Darmanitan', 'Stage 1', 'Darmanitan'],
    subtypes=['Stage 1'],
    collector_number=35,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Darumaka.Name',
    family_id=554,
    abilities=[
        Attack(
            title='Damage Counterpunch',
            game_text='If this Pokémon has any damage counters on it, this attack does 60 more damage.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Heat Blast',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 3},
            damage=140,
        ),
    ],
)
