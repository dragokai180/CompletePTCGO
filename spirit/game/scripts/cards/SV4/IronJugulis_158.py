from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='530a39ff-0783-52b2-8f2f-5333a7e21f1f',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.IronJugulis.Name',
    display_name='Iron Jugulis',
    searchable_by=['Iron Jugulis', 'Basic', 'Future', 'IronJugulis'],
    subtypes=['Basic', 'Future'],
    collector_number=158,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=993,
    abilities=[
        Attack(
            title='Homing Headbutt',
            game_text="This attack does 50 damage to 3 of your opponent's Pokémon that have any damage counters on them. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 3},
            effect=standard_attack,
        ),
        Attack(
            title='Baryon Beam',
            game_text='If this Pokémon has a Future Booster Energy Capsule attached, this attack can be used for ColorlessColorlessColorless.',
            cost={PokemonTypes.COLORLESS: 5},
            damage=150,
            effect=standard_attack,
        ),
    ],
)
