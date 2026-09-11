from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='417967ae-36e9-5cf9-875a-54cdc8bcb9e0',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Hitmonlee.Name',
    display_name='Hitmonlee',
    searchable_by=['Hitmonlee', 'Basic', 'Hitmonlee'],
    subtypes=['Basic'],
    collector_number=106,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=106,
    abilities=[
        Attack(
            title='Twister Kick',
            game_text="This attack does 10 damage to each of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.) Switch this Pokémon with 1 of your Benched Pokémon.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Low Kick',
            cost={PokemonTypes.FIGHTING: 3},
            damage=100,
        ),
    ],
)
