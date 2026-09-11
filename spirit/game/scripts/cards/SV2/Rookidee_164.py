from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='53df3ffd-f401-5045-b0d9-58d8cbd0e2eb',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Rookidee.Name',
    display_name='Rookidee',
    searchable_by=['Rookidee', 'Basic', 'Rookidee'],
    subtypes=['Basic'],
    collector_number=164,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=821,
    abilities=[
        Attack(
            title='Send Back',
            game_text="Switch out your opponent's Active Pokémon to the Bench.\xa0(Your opponent chooses the new Active Pokémon.)",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
