from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='55db7ec2-981f-59e7-9444-213676c99086',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Ivysaur.Name',
    display_name='Ivysaur',
    searchable_by=['Ivysaur', 'Stage 1', 'Ivysaur'],
    subtypes=['Stage 1'],
    collector_number=2,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Bulbasaur.Name',
    family_id=1,
    abilities=[
        Attack(
            title='Leech Seed',
            game_text='Heal 20 damage from this Pokémon.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Vine Whip',
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
        ),
    ],
)
