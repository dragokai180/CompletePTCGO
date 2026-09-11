from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
    second_coat, second_coat_condition,
)


card = PokemonCardDef(
    guid='4b59e871-d207-577e-b5ba-2b8d9dec1794',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Smeargle.Name',
    display_name='Smeargle',
    searchable_by=['Smeargle', 'Basic', 'Smeargle'],
    subtypes=['Basic'],
    collector_number=123,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=235,
    abilities=[
        Ability(
            title='Second Coat',
            game_text='Once during your turn (before your attack), you may switch a basic Energy card attached to your Active Pokémon with a different type of basic Energy card from your discard pile.',
            effect=second_coat,
            condition=second_coat_condition,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Beat',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
