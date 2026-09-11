from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c8dd0179-be0f-5da0-a1cc-cf1004bf5f85',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Togepi.Name',
    display_name='Togepi',
    searchable_by=['Togepi', 'Basic', 'Togepi'],
    subtypes=['Basic'],
    collector_number=70,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=175,
    abilities=[
        Attack(
            title='Plead',
            game_text='Ask your opponent if you may draw 2 cards. If yes, draw 2 cards. If no, this attack does 20 damage to the Defending Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
