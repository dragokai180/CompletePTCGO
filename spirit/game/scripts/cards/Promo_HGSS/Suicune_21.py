from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='891cec9e-dc79-57c4-b3cd-b12400ac967f',
    key='Promo_HGSS',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Suicune.Name',
    display_name='Suicune',
    searchable_by=['Suicune', 'Basic', 'Suicune'],
    subtypes=['Basic'],
    collector_number=21,
    set_code='Promo_HGSS',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    attributes={200790: {'type': 'string', 'value': 'HGSS21'}},
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=245,
    abilities=[
        Attack(
            title='Sheer Cold',
            game_text="Flip a coin. If heads, the Defending Pokémon can't attack during your opponent's next turn.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
