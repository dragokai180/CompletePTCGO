from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b24d5d37-682b-5b79-915c-c1c9c99e7473',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gloom.Name',
    display_name='Gloom',
    searchable_by=['Gloom', 'Stage 1', 'Gloom'],
    subtypes=['Stage 1'],
    collector_number=27,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Oddish.Name',
    family_id=43,
    abilities=[
        Attack(
            title='Miracle Powder',
            game_text='Flip a coin. If heads, choose 1 Special Condition. The Defending Pokémon is now affected by that Special Condition.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
