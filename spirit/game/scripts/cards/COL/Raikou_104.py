from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='38dc39e8-48d4-5e70-8a49-3f3eb9714f46',
    key='COL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Raikou.Name',
    display_name='Raikou',
    searchable_by=['Raikou', 'Basic', 'Raikou'],
    subtypes=['Basic'],
    collector_number=104,
    set_code='COL',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    attributes={200790: {'type': 'string', 'value': 'SL9'}},
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=243,
    abilities=[
        Ability(
            title='Extreme Speed',
            game_text="Raikou's Retreat Cost is Colorless less for each Lightning Energy attached to Raikou.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=standard_passive("Raikou's Retreat Cost is Colorless less for each Lightning Energy attached to Raikou."),
        ),
        Attack(
            title='Raging Thunder',
            game_text="Does 20 damage to 1 of your Pokémon and don't apply Weakness and Resistance to this damage.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=standard_attack,
        ),
    ],
)
