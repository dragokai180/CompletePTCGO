from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ea66c540-510c-511d-8adc-cc1289b70d31',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tyrogue.Name',
    display_name='Tyrogue',
    searchable_by=['Tyrogue', 'Basic', 'Tyrogue'],
    subtypes=['Basic'],
    collector_number=100,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    family_id=236,
    abilities=[
        Ability(
            title='Bratty Kick',
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, put 3 damage counters on 1 of your opponent's Pokémon. If you use this Ability, your turn ends.",
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
    ],
)
