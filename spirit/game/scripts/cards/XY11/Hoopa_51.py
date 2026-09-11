from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='27845058-498f-5310-998a-330d12ffef1b',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Hoopa.Name',
    display_name='Hoopa',
    searchable_by=['Hoopa', 'Basic', 'Hoopa'],
    subtypes=['Basic'],
    collector_number=51,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=720,
    abilities=[
        Attack(
            title='Hyperspace Punch',
            game_text="This attack does 20 damage to 2 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Portal Strike',
            game_text="This Pokémon can't use Portal Strike during your next turn.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=130,
            effect=standard_attack,
            locks_next_turn=True,
        ),
    ],
)
