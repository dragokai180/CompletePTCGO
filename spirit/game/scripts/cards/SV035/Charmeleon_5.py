from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='116d61e1-8b6a-5fcc-b704-363132cd6cae',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name',
    display_name='Charmeleon',
    searchable_by=['Charmeleon', 'Stage 1', 'Charmeleon'],
    subtypes=['Stage 1'],
    collector_number=5,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Charmander.Name',
    family_id=4,
    abilities=[
        Attack(
            title='Combustion',
            cost={PokemonTypes.FIRE: 1},
            damage=20,
        ),
        Attack(
            title='Fire Blast',
            game_text='Discard an Energy from this Pokémon.',
            cost={PokemonTypes.FIRE: 3},
            damage=90,
            effect=standard_attack,
        ),
    ],
)
