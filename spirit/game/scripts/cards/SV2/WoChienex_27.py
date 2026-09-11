from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c04dba26-bf02-5274-bbd6-0f5faaa87c0f',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.WoChienex.Name',
    display_name='Wo-Chien ex',
    searchable_by=['Wo-Chien ex', 'Basic', 'ex', 'WoChienex'],
    subtypes=['Basic', 'ex'],
    collector_number=27,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=230,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=1001,
    abilities=[
        Attack(
            title='Covetous Ivy',
            game_text="This attack does 60 damage to 1 of your opponent's Benched Pokémon for each Prize card your opponent has taken.\xa0(Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Forest Blast',
            cost={PokemonTypes.GRASS: 3, PokemonTypes.COLORLESS: 1},
            damage=220,
        ),
    ],
)
