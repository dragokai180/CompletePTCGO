from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b2b67dbe-2733-5c8a-aa7b-6d01a2a4a652',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Braixen.Name',
    display_name='Braixen',
    searchable_by=['Braixen', 'Stage 1', 'Braixen'],
    subtypes=['Stage 1'],
    collector_number=26,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Fennekin.Name',
    family_id=653,
    abilities=[
        Attack(
            title='Flamethrower',
            game_text='Discard an Energy attached to this Pokémon.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=standard_attack,
        ),
    ],
)
