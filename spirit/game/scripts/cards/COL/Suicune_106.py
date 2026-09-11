from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0d8f382b-7491-5607-be06-343a5b3ef3a2',
    key='COL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Suicune.Name',
    display_name='Suicune',
    searchable_by=['Suicune', 'Basic', 'Suicune'],
    subtypes=['Basic'],
    collector_number=106,
    set_code='COL',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    attributes={200790: {'type': 'string', 'value': 'SL11'}},
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=245,
    abilities=[
        Ability(
            title='Extreme Speed',
            game_text="Suicune's Retreat Cost is Colorless less for each Water Energy attached to Suicune.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=standard_passive("Suicune's Retreat Cost is Colorless less for each Water Energy attached to Suicune."),
        ),
        Attack(
            title='Tsunami',
            game_text="This attack does 20 damage to each of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
