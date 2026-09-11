from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='374729a7-d56c-580f-9f5d-38daf420f121',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Barbaracle.Name',
    display_name='Barbaracle',
    searchable_by=['Barbaracle', 'Stage 1', 'Barbaracle'],
    subtypes=['Stage 1'],
    collector_number=49,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Binacle.Name',
    family_id=688,
    abilities=[
        Attack(
            title='Rock Rush',
            game_text='Discard as many Fighting Energy cards as you like from your hand. This attack does 30 damage times the number of Energy cards you discarded.',
            cost={PokemonTypes.FIGHTING: 2},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Boulder Crush',
            cost={PokemonTypes.FIGHTING: 3},
            damage=80,
        ),
    ],
)
