from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='20dd936e-40b1-5e5c-9471-0775f72e1880',
    key='COL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Entei.Name',
    display_name='Entei',
    searchable_by=['Entei', 'Basic', 'Entei'],
    subtypes=['Basic'],
    collector_number=98,
    set_code='COL',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    attributes={200790: {'type': 'string', 'value': 'SL3'}},
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=244,
    abilities=[
        Ability(
            title='Extreme Speed',
            game_text="Entei's Retreat Cost is Colorless Energy less for each Fire Energy attached to Entei.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=standard_passive("Entei's Retreat Cost is Colorless Energy less for each Fire Energy attached to Entei."),
        ),
        Attack(
            title='Wild Blaze',
            game_text='Discard the top 3 cards of your deck.',
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=standard_attack,
        ),
    ],
)
