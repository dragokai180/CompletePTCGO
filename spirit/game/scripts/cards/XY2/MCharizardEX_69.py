from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f3f0dea4-804c-5484-88ed-3d1821821e54',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MCharizardEX.Name',
    display_name='M Charizard-EX',
    searchable_by=['M Charizard-EX', 'MEGA', 'EX', 'MCharizardEX'],
    subtypes=['MEGA', 'EX'],
    collector_number=69,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=230,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.CharizardEX.Name',
    family_id=6,
    abilities=[
        Attack(
            title='Wild Blaze',
            game_text='Discard the top 5 cards of your deck.',
            cost={PokemonTypes.FIRE: 2, PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=300,
            effect=standard_attack,
        ),
    ],
)
