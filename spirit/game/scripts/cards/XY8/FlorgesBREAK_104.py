from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='be2e5392-8dcd-541f-adf8-153aa68d25bf',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.FlorgesBREAK.Name',
    display_name='Florges BREAK',
    searchable_by=['Florges BREAK', 'BREAK', 'FlorgesBREAK'],
    subtypes=['BREAK'],
    collector_number=104,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.BreakRare,
    hp=140,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Florges.Name',
    family_id=669,
    abilities=[
        Ability(
            title='Floral Breeze',
            game_text='Once during your turn (before your attack), you may heal 30 damage and remove a Special Condition from your Active Pokémon.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
    ],
)
