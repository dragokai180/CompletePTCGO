from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='edce07d9-2384-5316-b5f5-44e4430a43f0',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MGyaradosEX.Name',
    display_name='M Gyarados-EX',
    searchable_by=['M Gyarados-EX', 'MEGA', 'EX', 'MGyaradosEX'],
    subtypes=['MEGA', 'EX'],
    collector_number=27,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=240,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.GyaradosEX.Name',
    family_id=130,
    abilities=[
        Attack(
            title='Blast Geyser',
            game_text='You may do 20 more damage for each Water Energy attached to this Pokémon. If you do, discard the top 2 cards of your deck.',
            cost={PokemonTypes.COLORLESS: 4},
            damage=120,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
