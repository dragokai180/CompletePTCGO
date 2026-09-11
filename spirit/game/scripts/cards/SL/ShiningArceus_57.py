from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e6147f47-b51d-5d5c-ad9e-b21b5b445a3f',
    key='SL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.ShiningArceus.Name',
    display_name='Shining Arceus',
    searchable_by=['Shining Arceus', 'Basic', 'ShiningArceus'],
    subtypes=['Basic'],
    collector_number=57,
    set_code='SL',
    regulation_mark=None,
    rarity=Rarities.Shining,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=493,
    abilities=[
        Ability(
            title='Fabled Defense',
            game_text="As long as this Pokémon is your Active Pokémon, prevent all damage done to your Benched Pokémon by your opponent's attacks.",
            passive=standard_passive("As long as this Pokémon is your Active Pokémon, prevent all damage done to your Benched Pokémon by your opponent's attacks."),
        ),
        Attack(
            title='Ultimate Arrow',
            game_text="This attack does 30 damage to each of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 4},
            effect=standard_attack,
        ),
    ],
)
