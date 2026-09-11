from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='14935706-93e9-5140-99ff-00ad53ba6ffc',
    key='XY6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MRayquazaEX.Name',
    display_name='M Rayquaza-EX',
    searchable_by=['M Rayquaza-EX', 'MEGA', 'EX', 'MRayquazaEX'],
    subtypes=['MEGA', 'EX'],
    collector_number=61,
    set_code='XY6',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=230,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.RayquazaEX.Name',
    family_id=384,
    abilities=[
        Attack(
            title='Dragon Ascent',
            game_text='Discard 2 Energy attached to this Pokémon.',
            cost={PokemonTypes.FIRE: 3, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=300,
            effect=standard_attack,
        ),
    ],
    passive=standard_passive("Any damage done to this Pokémon by attacks from your opponent's Grass, Fire, Water, or Lightning Pokémon is reduced by 20 (after applying Weakness and Resistance)."),
)
