from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='401d1c8b-d2c3-5ce9-a3dc-dc34aca4c3ee',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MCameruptEX.Name',
    display_name='M Camerupt-EX',
    searchable_by=['M Camerupt-EX', 'MEGA', 'EX', 'MCameruptEX'],
    subtypes=['MEGA', 'EX'],
    collector_number=198,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=230,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.CameruptEX.Name',
    family_id=323,
    abilities=[
        Attack(
            title='Magma Eruption',
            game_text="You may discard the top 3 cards of each player's deck. If you do, this attack does 40 more damage for each Energy card you discarded in this way.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=120,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
