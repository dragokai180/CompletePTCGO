from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1f868748-8128-5b72-b0b0-bda379a54998',
    key='COL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MimeJr.Name',
    display_name='Mime Jr.',
    searchable_by=['Mime Jr.', 'Basic', 'MimeJr'],
    subtypes=['Basic'],
    collector_number=47,
    set_code='COL',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=30,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    family_id=439,
    abilities=[
        Ability(
            title='Sweet Sleeping Face',
            game_text='As long as Mime Jr. is Asleep, prevent all damage done to Mime Jr. by attacks.',
            ability_type=AbilityTypes.POKE_BODY,
            passive=standard_passive('As long as Mime Jr. is Asleep, prevent all damage done to Mime Jr. by attacks.'),
        ),
        Attack(
            title='Sleepy Lost',
            game_text="Put the top card of your opponent's deck in the Lost Zone. Mime Jr. is now Asleep.",
            cost={},
            effect=standard_attack,
        ),
    ],
)
