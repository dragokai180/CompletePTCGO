from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)
from spirit.game.card_effects.pokemon import TeraRulePassive


card = PokemonCardDef(
    guid='705fa3f6-c297-5eea-9553-c01ff67ee41c',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Arcanineex.Name',
    display_name='Arcanine ex',
    searchable_by=['Arcanine ex', 'Stage 1', 'Tera', 'ex', 'Arcanineex'],
    subtypes=['Stage 1', 'Tera', 'ex'],
    collector_number=32,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=280,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Growlithe.Name',
    family_id=58,
    abilities=[
        Attack(
            title='Raging Claws',
            game_text='This attack does 10 more damage for each damage counter on this Pokémon.',
            cost={PokemonTypes.FIRE: 2},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Bright Flame',
            game_text='Discard 2 Fire Energy from this Pokémon.',
            cost={PokemonTypes.FIRE: 3},
            damage=250,
            effect=standard_attack,
        ),
    ],
    passive=TeraRulePassive(),
)
