from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1114fdbc-fc81-53f1-ae2e-1d0ab65d0c96',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Articuno.Name',
    display_name='Articuno',
    searchable_by=['Articuno', 'Basic', 'Articuno'],
    subtypes=['Basic'],
    collector_number=144,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=144,
    abilities=[
        Ability(
            title='Ice Float',
            game_text='If this Pokémon has any Water Energy attached, it has no Retreat Cost.',
            passive=standard_passive('If this Pokémon has any Water Energy attached, it has no Retreat Cost.'),
        ),
        Attack(
            title='Blizzard',
            game_text="This attack also does 10 damage to each of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 3},
            damage=110,
            effect=standard_attack,
        ),
    ],
)
