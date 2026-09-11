from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='47dded97-cfef-56eb-9fc1-b05373fbd140',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Psyduck.Name',
    display_name='Psyduck',
    searchable_by=['Psyduck', 'Basic', 'Psyduck'],
    subtypes=['Basic'],
    collector_number=74,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=54,
    abilities=[
        Attack(
            title='Tripping Headbutt',
            game_text="Flip a coin. If heads, this attack does 30 damage to 1 of your opponent's Pokémon. If tails, this attack does 30 damage to 1 of your Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
    ],
)
