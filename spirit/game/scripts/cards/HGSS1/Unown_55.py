from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='dfe7d3bc-8854-5b95-b844-38dbd7d52f6e',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Unown.Name',
    display_name='Unown',
    searchable_by=['Unown', 'Basic', 'Unown'],
    subtypes=['Basic'],
    collector_number=55,
    set_code='HGSS1',
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
            title='FLASH',
            game_text='Once during your turn, when you put Unown from your hand onto your Bench, you may look at the top 5 cards of your deck and put them back on top of your deck in any order.',
            ability_type=AbilityTypes.POKE_POWER,
            effect=standard_ability,
            trigger=Triggers.ON_PLAY,
        ),
        Attack(
            title='Hidden Power',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)
