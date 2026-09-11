from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1b079145-bebb-5b21-9b6e-4246a9238241',
    key='Promo_HGSS',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lapras.Name',
    display_name='Lapras',
    searchable_by=['Lapras', 'Basic', 'Lapras'],
    subtypes=['Basic'],
    collector_number=14,
    set_code='Promo_HGSS',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    attributes={200790: {'type': 'string', 'value': 'HGSS14'}},
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=131,
    abilities=[
        Attack(
            title='Ferry',
            game_text='Search your discard pile for a Supporter card, show it to your opponent, and put it into your hand.',
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Surf',
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)
