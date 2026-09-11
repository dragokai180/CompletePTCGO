from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9f657905-6a7f-5b0c-b8d7-c3878f8d1c57',
    key='COL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Relicanth.Name',
    display_name='Relicanth',
    searchable_by=['Relicanth', 'Basic', 'Relicanth'],
    subtypes=['Basic'],
    collector_number=69,
    set_code='COL',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=369,
    abilities=[
        Attack(
            title='Prehistoric Wisdom',
            game_text='Choose a card from your hand and put it in the Lost Zone. Then, draw 3 cards.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Granite Head',
            game_text="During your opponent's next turn, any damage done to Relicanth by attacks is reduced by 30 (after applying Weakness and Resistance).",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
