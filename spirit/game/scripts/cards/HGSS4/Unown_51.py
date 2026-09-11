from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4c3566ff-dbba-52b1-9b71-4f2871e4e181',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Unown.Name',
    display_name='Unown',
    searchable_by=['Unown', 'Basic', 'Unown'],
    subtypes=['Basic'],
    collector_number=51,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=201,
    abilities=[
        Ability(
            title='CURE',
            game_text='Once during your turn, when you put Unown from your hand onto your Bench, remove all Special Conditions from your Active Pokémon.',
            ability_type=AbilityTypes.POKE_POWER,
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Hidden Power',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)
