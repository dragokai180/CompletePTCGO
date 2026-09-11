from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0ba35622-a919-5902-8f7f-e18f7417c10c',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Elekid.Name',
    display_name='Elekid',
    searchable_by=['Elekid', 'Basic', 'Elekid'],
    subtypes=['Basic'],
    collector_number=59,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=239,
    abilities=[
        Attack(
            title='Crackling Shot',
            game_text="This attack does 30 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={},
            effect=standard_attack,
        ),
    ],
)
