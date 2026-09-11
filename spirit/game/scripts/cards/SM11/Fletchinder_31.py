from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='87f7f48c-25f3-5a5f-91c9-822e823d5cd2',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Fletchinder.Name',
    display_name='Fletchinder',
    searchable_by=['Fletchinder', 'Stage 1', 'Fletchinder'],
    subtypes=['Stage 1'],
    collector_number=31,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Fletchling.Name',
    family_id=661,
    abilities=[
        Attack(
            title='Flame Charge',
            game_text='Search your deck for a Fire Energy card and attach it to this Pokémon. Then, shuffle your deck.',
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
