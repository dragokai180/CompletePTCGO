from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='006b31a9-4af6-5003-aee5-306b8050a8d4',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cubone.Name',
    display_name='Cubone',
    searchable_by=['Cubone', 'Basic', 'Cubone'],
    subtypes=['Basic'],
    collector_number=104,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=104,
    abilities=[
        Ability(
            title='Cheering Bone',
            game_text="As long as this Pokémon is on your Bench, attacks used by your Marowak do 30 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).",
            passive=standard_passive("As long as this Pokémon is on your Bench, attacks used by your Marowak do 30 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance)."),
        ),
        Attack(
            title='Hit Twice',
            game_text='Flip 2 coins. This attack does 10 damage for each heads.',
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
