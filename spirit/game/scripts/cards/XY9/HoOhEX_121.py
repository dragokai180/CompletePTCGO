from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
    purifying_fire, purifying_fire_condition,
)


card = PokemonCardDef(
    guid='350461da-78bb-55a3-aaa8-6e68200c6809',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.HoOhEX.Name',
    display_name='Ho-Oh-EX',
    searchable_by=['Ho-Oh-EX', 'Basic', 'EX', 'HoOhEX'],
    subtypes=['Basic', 'EX'],
    collector_number=121,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=250,
    abilities=[
        Ability(
            title='Purifying Fire',
            game_text='Once during your turn (before your attack), if this Pokémon has any basic Fire Energy attached to it, you may heal 50 damage from it.',
            effect=purifying_fire,
            condition=purifying_fire_condition,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Elemental Feather',
            game_text="This attack does 30 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1},
            damage=130,
            effect=standard_attack,
        ),
    ],
)
