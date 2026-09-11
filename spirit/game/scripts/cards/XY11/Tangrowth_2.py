from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1fdaf0d7-a7bf-5576-978e-a6c10b994df2',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tangrowth.Name',
    display_name='Tangrowth',
    searchable_by=['Tangrowth', 'Stage 1', 'Tangrowth'],
    subtypes=['Stage 1'],
    collector_number=2,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Tangela.Name',
    family_id=114,
    abilities=[
        Attack(
            title='Leaf Storm',
            game_text='Heal 40 damage from each of your Grass Pokémon.',
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=standard_attack,
        ),
        Attack(
            title='Flog',
            game_text='Flip a coin. If heads, this attack does 30 more damage.',
            cost={PokemonTypes.GRASS: 3, PokemonTypes.COLORLESS: 1},
            damage=110,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
