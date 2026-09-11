from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e8d11dfe-d88f-5c6c-8e13-b2c84ca6a997',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Nidorino.Name',
    display_name='Nidorino',
    searchable_by=['Nidorino', 'Stage 1', 'Nidorino'],
    subtypes=['Stage 1'],
    collector_number=44,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Nidoran.Name',
    family_id=32,
    abilities=[
        Attack(
            title='Peck',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title='Nido Press',
            game_text='If Nidorina is on your Bench, this attack does 40 more damage.',
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
