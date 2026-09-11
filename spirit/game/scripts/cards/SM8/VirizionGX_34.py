from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='40ef41fc-5f75-5868-9b58-ed8271a02bbd',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.VirizionGX.Name',
    display_name='Virizion-GX',
    searchable_by=['Virizion-GX', 'Basic', 'GX', 'VirizionGX'],
    subtypes=['Basic', 'GX'],
    collector_number=34,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=170,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=640,
    abilities=[
        Attack(
            title='Double Draw',
            game_text='Draw 2 cards.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Sensitive Blade',
            game_text='If you played a Supporter card from your hand during this turn, this attack does 80 more damage.',
            cost={PokemonTypes.GRASS: 2},
            damage=50,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Breeze Away-GX',
            game_text="Put any number of your Pokémon in play and all cards attached to them into your hand. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
            gx=True,
        ),
    ],
)
