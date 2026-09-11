from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='92b3da31-b2a8-5f3b-bf0e-1ec7f6d92f37',
    key='SL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Reshiram.Name',
    display_name='Reshiram',
    searchable_by=['Reshiram', 'Basic', 'Reshiram'],
    subtypes=['Basic'],
    collector_number=14,
    set_code='SL',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=643,
    abilities=[
        Attack(
            title='Outrage',
            game_text='This attack does 10 more damage for each damage counter on this Pokémon.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Scorching Breath',
            game_text="This Pokémon can't attack during your next turn.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=standard_attack,
        ),
    ],
)
