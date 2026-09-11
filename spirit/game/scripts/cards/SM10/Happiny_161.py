from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='cb5427ab-f488-5c6e-9f81-8950e7ed6615',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Happiny.Name',
    display_name='Happiny',
    searchable_by=['Happiny', 'Basic', 'Happiny'],
    subtypes=['Basic'],
    collector_number=161,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    family_id=440,
    abilities=[
        Ability(
            title='Playhouse Heal',
            game_text='Once during your turn (before your attack), you may flip a coin. If heads, heal 60 damage from 1 of your Pokémon. If you use this Ability, your turn ends.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
    ],
)
