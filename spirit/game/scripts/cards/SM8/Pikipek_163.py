from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='93539eb7-75b3-5449-8811-25fc5140b839',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pikipek.Name',
    display_name='Pikipek',
    searchable_by=['Pikipek', 'Basic', 'Pikipek'],
    subtypes=['Basic'],
    collector_number=163,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=731,
    abilities=[
        Attack(
            title='Peck Off',
            game_text="Before doing damage, discard all Pokémon Tool cards from your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
