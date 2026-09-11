from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f2ebb804-6a99-5201-8eea-59e9b8d21947',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Igglybuff.Name',
    display_name='Igglybuff',
    searchable_by=['Igglybuff', 'Basic', 'Igglybuff'],
    subtypes=['Basic'],
    collector_number=168,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    family_id=174,
    abilities=[
        Ability(
            title='Sleepy Voice',
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, your opponent's Active Pokémon is now Asleep. If you use this Ability, your turn ends.",
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
    ],
)
