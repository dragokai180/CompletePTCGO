from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e2e7192d-711a-5ee4-b25a-8a28d6644f3b',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cetoddle.Name',
    display_name='Cetoddle',
    searchable_by=['Cetoddle', 'Basic', 'Cetoddle'],
    subtypes=['Basic'],
    collector_number=53,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=974,
    abilities=[
        Attack(
            title='Avalanche',
            game_text="This attack also does 10 damage to each of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
